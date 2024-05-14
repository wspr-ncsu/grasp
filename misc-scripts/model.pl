% be careful with long names.

:-style_check(-discontiguous).
:-style_check(-singleton).
:- autoload(library(option), [option/3]).
% Basic facts expected to be output by YML parser (TODO is this okay?) 
% function(name, public_invoke)
function('', false).
% resource(type, name, public_read, public_write).
resource('', '', false, false).
% permission(function, permission, resource).
permission('', '', '').
% event_sns_msg(sns_stream_arn, triggered_function).
event_sns_msg('', '').
% event_stream_msg(stream_arn, triggered_function).
event_stream_msg('', '').
% event_s3(s3_trigger, resource_arn, triggered_function).
event_s3('', '', '').
% event_iot(triggered_function).
event_iot('').

% Helpers
% Determines if an element is already in a list
nonmember(Arg,[Arg|_]) :-
        !,
        fail.
nonmember(Arg,[_|Tail]) :-
        !,
        nonmember(Arg,Tail).
nonmember(_,[]).


:- predicate_options(wildcards/4, 4,
                    [ perm(oneof([any,nowildcard,halfwildcard,fullwildcard])),
                      res(oneof([any,nowildcard,halfwildcard,fullwildcard]))
                    ]).

% Predicate that finds all permissions with a wildcard pattern. Five patterns can be specified for
% both the permission and the resource:
%   1. any - the value can be any of the below patterns. This is the default behavior.
%   2. nowildcard - an explicit permission (string does not contain '*')
%   3. halfwildcard - a partial permission that ends with '*' (e.g., s3:Get*)
%   4. fullwildcard - the value '*'
%   5. anywildcard - either 3 or 4 above
% options are passed to the predicate as a list in the following format:
%  [perm(value), res(value)]
%  e.g., wildcards(F, P, R, [perm(fullwildcard), res(halfwildcard)]).
%  an empty options list [] is interpreted as:
%    wildcards(F, P, R, [perm(any), res(any)]).
wildcards_helper(Value, any) :- true.
wildcards_helper(Value, nowildcard) :- not(strip_star(Value, _)).
wildcards_helper(Value, halfwildcard) :- sub_string(Value, Before, _, _, '*'), Before > 0.
wildcards_helper(Value, fullwildcard) :- Value == '*'.
wildcards_helper(Value, anywildcard) :- sub_string(Value, _, _, _, '*'). 

wildcards(Func, Perm, Resource, Options) :-
    permission(Func, Perm, Resource), Func\=='', Perm\=='', Resource\=='',
    option(perm(PermOpt), Options, any),
    option(res(ResOpt), Options, any),
    wildcards_helper(Perm, PermOpt),
    wildcards_helper(Resource, ResOpt).

% Checks if '*' is in the Input string and returns everything preceeding the '*'
% otherwise returns false.
strip_star(Input, Output) :-
    sub_string(Input, Before, _, 0, '*'),
    !,
    sub_atom(Input, 0, Before, _, Output).

% Hard coded facts to define read and write permissions for various resources
read_perm('s3', 's3:GetObject').
read_perm('dynamodb', 'dynamodb:BatchGetItem').
read_perm('dynamodb', 'dynamodb:GetItem').
read_perm('dynamodb', 'dynamodb:PartiQLSelect').
read_perm('dynamodb', 'dynamodb:Query').
read_perm('dynamodb', 'dynamodb:Scan').
read_perm('dynamodb', 'dynamodb:GetRecords').
read_perm('sns', 'sns:Subscribe').
read_perm('sqs', 'sqs:ReceiveMessage').
read_perm('iot', 'iot:Receive').
read_perm('cloudwatch', 'cloudwatch:GetMetricData').
read_perm('logs', 'logs:GetLogEvents').
read_perm('logs', 'logs:GetLogRecord').
read_perm('kinesis', 'kinesis:GetRecord').
read_perm('sagemaker', 'sagemaker:GetRecord').
read_perm('sdb', 'sdb:Select').
read_perm('sdb', 'sdb:GetAttributes').
read_perm('appsync', 'appsync:GraphQL').
read_perm('rds-data', 'rds-data:BatchExecuteStatement').
read_perm('rds-data', 'rds-data:ExecuteSql').
read_perm('rds-data', 'rds-data:ExecuteStatement').
read_perm('neptune-db', 'neptune-db:Connect').
write_perm('s3', 's3:PutObject').
write_perm('dynamodb', 'dynamodb:BatchWriteItem').
write_perm('dynamodb', 'dynamodb:PartiQLInsert').
write_perm('dynamodb', 'dynamodb:PartiQLUpdate').
write_perm('dynamodb', 'dynamodb:PutItem').
write_perm('dynamodb', 'dynamodb:UpdateItem').
write_perm('sns', 'sns:Publish').
write_perm('sqs', 'sqs:SendMessage').
write_perm('iot', 'iot:Publish').
write_perm('cloudwatch', 'cloudwatch:PutMetricData').
write_perm('logs', 'logs:PutLogEvents').
write_perm('kinesis', 'kinesis:PutRecord').
write_perm('kinesis', 'kinesis:PutRecords').
write_perm('sagemaker', 'sagemaker:PutRecord').
write_perm('sdb', 'sdb:BatchPutAttributes').
write_perm('sdb', 'sdb:PutAttributes').
write_perm('appsync', 'appsync:GraphQL').
write_perm('rds-data', 'rds-data:BatchExecuteStatement').
write_perm('rds-data', 'rds-data:ExecuteSql').
write_perm('rds-data', 'rds-data:ExecuteStatement').
write_perm('neptune-db', 'neptune-db:Connect').




% Main Logic
% can_read determines if there is a function with a permission to read a resource Res of type
% ResType.
% There are four possibilities to check
%  1. An explicitly named permission on an explicitly named resource
%  2. An explicitly named permission on a wildcard resource
%  3. A wildcard permission on an explicitly named resource
%  4. A wildcard permission on a wildcard resource
%     re_match() does not handle '*' in the strings so it must be removed by strip_star. Note that
%     strip_star returns false if the string does not contain a '*' which prevents wrongly matching
%     atoms that are substrings of other atoms. e.g., example will not match example-test but
%     example* will match example-test.
%     Further, case 1 will never match a permission(_, 'contains*', _) since
%     read_perm(_, 'cointains*') will never exist
%     The set value of Perm will be the actual permission value used. e.g., this will be either the
%     explicit permission or a permission that satisfies the wildcard constraint

% Case 1 explicit permission on explicity resource
can_read(Func, ResType, Res, Perm) :- 
    read_perm(ResType, Perm),
    permission(Func, Perm, Res),
    !.
% Case 2 explicit permission on wildcard resource
can_read(Func, ResType, Res, Perm) :-
    read_perm(ResType, Perm),
    permission(Func, Perm, CandidateRes),
    strip_star(CandidateRes, ResRoot),
    re_match(ResRoot, Res, [anchored]),
    !.
% Case 3 wildcard permission on explicit resource
can_read(Func, ResType, Res, Perm) :-
    read_perm(ResType, Perm),
    permission(Func, CandidatePerm, Res),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, Perm, [anchored]),
    !.
% Case 4 wildcard permission on wildcard resource
can_read(Func, ResType, Res, Perm) :-
    read_perm(ResType, Perm),
    permission(Func, CandidatePerm, CandidateRes),
    strip_star(CandidatePerm, PermRoot),
    strip_star(CandidateRes, ResRoot),
    re_match(PermRoot, Perm, [anchored]),
    re_match(ResRoot, Res, [anchored]),
    !.

% can_write same as can_read but for writes
% Case 1
can_write(Func, ResType, Res, Perm) :-
    write_perm(ResType, Perm),
    permission(Func, Perm, Res),
    !.
% Case 2
can_write(Func, ResType, Res, Perm) :-
    write_perm(ResType, Perm),
    permission(Func, Perm, CandidateRes),
    strip_star(CandidateRes, ResRoot),
    re_match(ResRoot, Res, [anchored]),
    !.
% Case 3
can_write(Func, ResType, Res, Perm) :-
    write_perm(ResType, Perm),
    permission(Func, CandidatePerm, Res),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, Perm, [anchored]),
    !.
% Case 4
can_write(Func, ResType, Res, Perm) :-
    write_perm(ResType, Perm),
    permission(Func, CandidatePerm, CandidateRes),
    strip_star(CandidatePerm, PermRoot),
    strip_star(CandidateRes, ResRoot),
    re_match(PermRoot, Perm, [anchored]),
    re_match(ResRoot, Res, [anchored]),
    !.

% Can function A directly invoke function B
% To avoid lateral movement between public functions, we enforce that the second function must be
% private. Similar to can_read/can_write, there are 4 cases in which a function has permission to
% invoke another function.
%  1. function A has explicit permission on an explicit function
%  2. function A has explicit permission on a wildcard function
%  3. function A has wildcard permission on an explicit funciton
%  4. funcion A has wildcard permission on a wildcard function
%  * Note that there are no "all resources have all permissions on all resources" type of rules.
%    Rules are defined and attached to functions  
% Case 1
control_flow(A, B) :-
    function(A, _), function(B, false), A\==B, A\=='',B\=='',
    permission(A, 'lambda:InvokeAsync', B).
control_flow(A, B) :-
    function(A, _), function(B, false), A\==B, A\=='',B\=='',
    permission(A, 'lambda:InvokeFunction', B).
% Case 2
control_flow(A, B) :-
    function(A, _), function(B, false), A\==B, A\=='',B\=='',
    permission(A, 'lambda:InvokeAsync', CandidateB),
    strip_star(CandidateB, BRoot),
    re_match(BRoot, B, [anchored]).
control_flow(A, B) :-
    function(A, _), function(B, false), A\==B, A\=='',B\=='',
    permission(A, 'lambda:InvokeFunction', CandidateB),
    strip_star(CandidateB, BRoot),
    re_match(BRoot, B, [anchored]).
% Case 3
control_flow(A, B) :-
    function(A, _), function(B, false), A\==B, A\=='',B\=='',
    permission(A, CandidatePerm, B),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, 'lambda:InvokeAsync', [anchored]).
control_flow(A, B) :-
    function(A, _), function(B, false), A\==B, A\=='',B\=='',
    permission(A, CandidatePerm, B),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, 'lambda:InvokeFunction', [anchored]).
% Case 4
control_flow(A, B) :-
    function(A, _), function(B, false), A\==B, A\=='',B\=='',
    permission(A, CandidatePerm, CandidateB),
    strip_star(CandidatePerm, PermRoot),
    strip_star(CandidateB, BRoot),
    re_match(PermRoot, 'lambda:InvokeAsync', [anchored]),
    re_match(BRoot, B, [anchored]).
control_flow(A, B) :-
    function(A, _), function(B, false), A\==B, A\=='',B\=='',
    permission(A, CandidatePerm, CandidateB),
    strip_star(CandidatePerm, PermRoot),
    strip_star(CandidateB, BRoot),
    re_match(PermRoot, 'lambda:InvokeFunction', [anchored]),
    re_match(BRoot, B, [anchored]).


% Can function A write to a resource C that function B can read from
data_flow(A, B, Resource, A_Perm, B_Perm) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    resource(ResType, Resource, _, false),
    can_write(A, ResType, Resource, A_Perm),
    can_read(B, ResType, Resource, B_Perm).

% event_sns_msg(topic, function).
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 'sns publish',
    Event = 'sns new message',
    resource('sns', Resource, _, false),
    can_write(A, 'sns', Resource, _),
    event_sns_msg(Resource, B).
% event_stream_msg(stream_arn, function).
% event stream: sqs
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 'sqs send message',
    Event = 'sqs new message',
    resource('sqs', Resource, _, false),
    can_write(A, 'sqs', Resource, _),
    event_stream_msg(Resource, B).
% event stream: kinesis
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 'kinesis put records',
    Event = 'kinesis new records',
    resource('kinesis', Resource, _, false),
    can_write(A, 'kinesis', Resource, _),
    event_stream_msg(Resource, B).
% event stream: dynamodb
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 'dynamodb modify records',
    Event = 'dynamodb modified records',
    resource('dynamodb', Resource, _, false),
    can_write(A, 'dynamodb', Resource, _),
    event_stream_msg(Resource, B).
% event_s3(trigger, bucket_name, function).
% Similar to can_read/can_write there are two cases for each of the 3 identified triggers
%  1. The s3 event is explicity defined
%  2. The s3 event is a wildcard
% s3:OjbectCreated:Put Case 1
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 's3 put object',
    Event = 's3 object created',
    resource('s3', Resource, _, false),
    permission(A, 's3:PutObject', Resource),
    event_s3('s3:ObjectCreated:Put', Resource, B).
% s3:OjbectCreated:Put Case 2
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 's3 put object',
    Event = 's3 object created',
    resource('s3', Resource, _, false),
    permission(A, CandidatePerm, Resource),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, 's3:PutObject'),
    event_s3('s3:ObjectCreated:Put', Resource, B).
% s3:ObjectCreated:Post Case 1
event_flow(A, B, Resource, Action, Event) :- 
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 's3 post object',
    Event = 's3 object created',
    resource('s3', Resource, _, false),
    permission(A, 's3:PutObject', Resource),
    event_s3('s3:ObjectCreated:Post', Resource, B).
% s3:ObjectCreated:Post Case 2
event_flow(A, B, Resource, Action, Event) :- 
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 's3 post object',
    Event = 's3 object created',
    resource('s3', Resource, _, false),
    permission(A, CandidatePerm, Resource),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, 's3:PutObject'),
    event_s3('s3:ObjectCreated:Post', Resource, B).
% s3:OjbectRemoved:Delete Case 1
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 's3 delete object',
    Event = 's3 object deleted',
    resource('s3', Resource, _, false),
    permission(A, 's3:DeleteObject', Resource),
    event_s3('s3:ObjectRemoved:Delete', Resource, B).
% s3:OjbectRemoved:Delete Case 2
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 's3 delete object',
    Event = 's3 object deleted',
    resource('s3', Resource, _, false),
    permission(A, CandidatePerm, Resource),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, 's3:DeleteObject'),
    event_s3('s3:ObjectRemoved:Delete', Resource, B).
% event_iot(function).
% Similar to above, 2 cases are explicit iot:Publish and wildcard
% Case 1 explicit
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 'iot publish',
    Event = 'iot new event',
    Resource='iot',
    permission(A, 'iot:Publish', Resource),
    event_iot(B).
% Case 2 wildcard
event_flow(A, B, Resource, Action, Event) :-
    function(A, _), function(B, false), A\==B, A\=='', B\=='',
    Action = 'iot publish',
    Event = 'iot new event',
    Resource='iot',
    permission(A, CandidatePerm, Resource),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, 'iot:Publish'),
    event_iot(B).


% Defines event flows directly from public
% event_sns_msg(topic, function).
public_event_flow(Func, HopRes, Action, Event) :-
    Action = 'public sns publish',
    Event = 'sns new message',
    function(Func, false), Func\=='',
    resource(sns, HopRes, _, true), HopRes\=='',
    event_sns_msg(HopRes, Func).
% event_stream_msg(stream_arn, function).
% event stream: sqs
public_event_flow(Func, HopRes, Action, Event) :-
    Action = 'public sqs send message',
    Event = 'sqs new message',
    function(Func, false), Func\=='',
    resource(sqs, HopRes, _, true), HopRes\=='',
    event_stream_msg(HopRes, Func).
% event stream: kinesis
public_event_flow(Func, HopRes, Action, Event) :-
    Action = 'public kinesis put records',
    Event = 'kinesis new records',
    function(Func, false), Func\=='',
    resource(kinesis, HopRes, _, true), HopRes\=='',
    event_stream_msg(HopRes, Func).
% event stream: dynamodb
public_event_flow(Func, HopRes, Action, Event) :-
    Action = 'public dynamodb modify records',
    Event = 'dynamodb modified records',
    function(Func, false), Func\=='',
    resource(dynamodb, HopRes, _, true), HopRes\=='',
    event_stream_msg(HopRes, Func).
% event_s3(trigger, bucket_name, function).
public_event_flow(Func, HopRes, Action, Event) :-
    Action = 'public s3 put object',
    Event = 's3 object created',
    function(Func, false), Func\=='',
    resource(s3, HopRes, _, true), HopRes\=='',
    event_s3('s3:ObjectCreated:Put', HopRes, Func).
public_event_flow(Func, HopRes, Action, Event) :-
    Action = 'public s3 post object',
    Event = 's3 object created',
    function(Func, false), Func\=='',
    resource(s3, HopRes, _, true), HopRes\=='',
    event_s3('s3:ObjectCreated:Post', HopRes, Func).
public_event_flow(Func, HopRes, Action, Event) :-
    Action = 'public s3 delete object',
    Event = 's3 object deleted',
    function(Func, false), Func\=='',
    resource(s3, HopRes, _, true), HopRes\=='',
    event_s3('s3:ObjectRemoved:Delete', HopRes, Func).
% event_iot(function).
public_event_flow(Func, HopRes, Action, Event) :-
    Action = 'public iot publish',
    Event = 'iot new event',
    function(Func, false), Func\=='',
    HopRes='iot',
    event_iot(Func).


% Function has direct read access to resource BASE CASE 
read_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :- 
    can_read(Func, ResType, TargetRes, Perm),
    atom_concat('read=', Perm, ReadAction),
    Path = [Func, TargetRes],
    Edges = [ReadAction],
    Funcs = [Func],
    CFs is 0, DFs is 0, EFs is 0,
    Length is 1, % must compromise this function to access to resource
    !.  % if direct access, do not backtrack to check for other hops
% Function does not have read access but can invoke another function (control flow)
read_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    control_flow(Func, IFunc),
    nonmember(IFunc, Visited),
    read_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, ICFs, DFs, EFs),
    Edges = ['control flow' | IEdges],
    Path = [Func | IPath],
    Funcs = [Func | IFuncs],
    CFs is ICFs + 1,
    Length is 1 + ILength. % must compromise this function + functions on the internal path
% Function does not have read access but can flow through another resource (data flow)
read_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    data_flow(Func, IFunc, HopRes, WritePerm, ReadPerm),
    HopRes \== TargetRes, 
    nonmember(IFunc, Visited),
    atom_concat('data flow write=', WritePerm, EdgeWrite),
    atom_concat('data flow read=', ReadPerm, EdgeRead),
    read_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, CFs, IDFs, EFs),
    Edges = [EdgeWrite, EdgeRead | IEdges],
    Path = [Func, HopRes | IPath],
    Funcs = [Func | IFuncs],
    DFs is 1 + IDFs, 
    Length is 1 + ILength. % must compromise this function + functions on the internal path
% Function does not have read access but can trigger event to an internal function (event flow)
read_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    event_flow(Func, IFunc, HopRes, Action, Event),
    HopRes \== TargetRes, 
    nonmember(IFunc, Visited),
    atom_concat('event flow action=', Action, EdgeAction),
    atom_concat('event flow event=', Event, EdgeEvent),
    read_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, CFs, DFs, IEFs),
    Edges = [EdgeAction, EdgeEvent | IEdges],
    Path = [Func, HopRes | IPath],
    Funcs = [Func | IFuncs],
    EFs is 1 + IEFs,
    Length is 1 + ILength. % must compromise this function + functions on the internal path

% Find all read paths from a publicly accessible function to an internal resource
find_read_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    function(EntryPoint, true),
    read_path(EntryPoint, ResType, TargetRes, Path, IEdges, [EntryPoint], Funcs, Length, ICFs, DFs, EFs),
    Edges = ['public invoke' | IEdges],
    CFs is 1 + ICFs.
% Find all read paths through a publicly accessible resource to an internal resource (public data flow)
% When dealing with permission(_, P, R). we must account for the 4 cases of wildcards for P and R
% Case 1: explicit permission, explicit first hop resource
find_read_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, Perm, EntryPoint),
    read_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 2: explicit permission, wildcard first hop resource
find_read_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, Perm, CandidateEntryPoint),
    strip_star(CandidateEntryPoint, EntryPointRoot),
    re_match(EntryPointRoot, EntryPoint),
    read_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 3: wildcard permission, explicit first hop resource
find_read_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, CandidatePerm, EntryPoint),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, Perm),
    read_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 4: wildcard permission, wildcard first hop resource
find_read_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, CandidatePerm, CandidateEntryPoint),
    strip_star(CandidatePerm, PermRoot),
    strip_star(CandidateEntryPoint, EntryPointRoot),
    re_match(PermRoot, Perm),
    re_match(EntryPointRoot, EntryPoint),
    read_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.

% Find all read paths from a publicly accessible resource that triggers a function (public event flow)
find_read_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    public_event_flow(Func, EntryPoint, Action, Event),
    EntryPoint \== TargetRes,
    read_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, DFs, IEFs),
    Edges = [Action, Event | IEdges],
    Path = [EntryPoint | IPath],
    EFs is 1 + IEFs.

% Function has direct write access to resource BASE CASE 
write_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :- 
    can_write(Func, ResType, TargetRes, Perm),
    atom_concat('write=', Perm, WriteAction),
    Path = [Func, TargetRes],
    Edges = [WriteAction],
    Funcs = [Func],
    CFs is 0, DFs is 0, EFs is 0,
    Length is 1,
    !. % if direct access, do not backtrack to check for other hops
% Function does not have write access but can invoke another function (control flow)
write_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    control_flow(Func, IFunc),
    nonmember(IFunc, Visited),
    write_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, ICFs, DFs, EFs),
    Edges = ['control flow' | IEdges],
    Path = [Func | IPath],
    Funcs = [Func | IFuncs],
    CFs is ICFs + 1,
    Length is 1 + ILength. % must compromise this function to access to resource
% Function does not have write access but can flow through another resource (data flow)
write_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    data_flow(Func, IFunc, HopRes, WritePerm, ReadPerm),
    HopRes \== TargetRes, 
    nonmember(IFunc, Visited),
    atom_concat('data flow write=', WritePerm, EdgeWrite),
    atom_concat('data flow read=', ReadPerm, EdgeRead),
    write_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, CFs, IDFs, EFs),
    Edges = [EdgeWrite, EdgeRead | IEdges],
    Path = [Func, HopRes | IPath],
    Funcs = [Func | IFuncs],
    DFs is 1 + IDFs,
    Length is 1 + ILength. % must compromise this function to access to resource
% Function does not have write access but can trigger event to an internal function (event flow)
write_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    event_flow(Func, IFunc, HopRes, Action, Event),
    HopRes \== TargetRes, 
    nonmember(IFunc, Visited),
    atom_concat('event flow action=', Action, EdgeAction),
    atom_concat('event flow event=', Event, EdgeEvent),
    write_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, CFs, DFs, IEFs),
    Edges = [EdgeAction, EdgeEvent | IEdges],
    Path = [Func, HopRes | IPath],
    Funcs = [Func | IFuncs],
    EFs is 1 + IEFs,
    Length is 1 + ILength. % must compromise this function to access to resource

% Find all write paths from a publicly accessible function to an internal resource
find_write_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    function(EntryPoint, true),
    write_path(EntryPoint, ResType, TargetRes, Path, IEdges, [EntryPoint], Funcs, Length, ICFs, DFs, EFs),
    Edges = ['public invoke' | IEdges],
    CFs is 1 + ICFs.
% Find all write paths through a publicly accessible resource to an internal resource (public data flow)
% Case 1 explicit permission, explicit resource
find_write_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, Perm, EntryPoint),
    write_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 2 explicit permission, wildcard resource
find_write_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, Perm, CandidateEntryPoint),
    strip_star(CandidateEntryPoint, EntryPointRoot),
    re_match(EntryPointRoot, EntryPoint),
    write_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 3 wildcard permission, explicit resource
find_write_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, CandidatePerm, EntryPoint),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, Perm),
    write_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 4 wildcard permission, wildcard resource
find_write_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, CandidatePerm, CandidateEntryPoint),
    strip_star(CandidatePerm, PermRoot),
    strip_star(CandidateEntryPoint, EntryPointRoot),
    re_match(PermRoot, Perm),
    re_match(EntryPointRoot, EntryPoint),
    write_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Find all write paths from a publicly accessible resource that triggers a function (public event flow)
find_write_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    public_event_flow(Func, EntryPoint, Action, Event),
    EntryPoint \== TargetRes,
    write_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, DFs, IEFs),
    Edges = [Action, Event | IEdges],
    Path = [EntryPoint | IPath],
    EFs is 1 + IEFs.

% Function has direct read and write access to resource BASE CASE 
rw_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :- 
    can_read(Func, ResType, TargetRes, RPerm),
    can_write(Func, ResType, TargetRes, WPerm),
    atom_concat('read=', RPerm, ReadAction),
    atom_concat(' & write=', WPerm, WriteAction),
    Path = [Func, TargetRes],
    atom_concat(ReadAction, WriteAction, LastEdge),
    Edges = [LastEdge],
    Funcs = [Func],
    CFs is 0, DFs is 0, EFs is 0,
    Length is 1, % must compromise this function to access to resource
    !.  % if direct access, do not backtrack to check for other hops
% Function does not have read and write access but can invoke another function (control flow)
rw_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    control_flow(Func, IFunc),
    nonmember(IFunc, Visited),
    rw_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, ICFs, DFs, EFs),
    Edges = ['control flow' | IEdges],
    Path = [Func | IPath],
    Funcs = [Func | IFuncs],
    CFs is ICFs + 1,
    Length is 1 + ILength. % must compromise this function + functions on the internal path
% Function does not have read and write access but can flow through another resource (data flow)
rw_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    data_flow(Func, IFunc, HopRes, WritePerm, ReadPerm),
    HopRes \== TargetRes, 
    nonmember(IFunc, Visited),
    atom_concat('data flow write=', WritePerm, EdgeWrite),
    atom_concat('data flow read=', ReadPerm, EdgeRead),
    rw_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, CFs, IDFs, EFs),
    Edges = [EdgeWrite, EdgeRead | IEdges],
    Path = [Func, HopRes | IPath],
    Funcs = [Func | IFuncs],
    DFs is 1 + IDFs, 
    Length is 1 + ILength. % must compromise this function + functions on the internal path
% Function does not have read and write access but can trigger event to an internal function (event flow)
rw_path(Func, ResType, TargetRes, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    event_flow(Func, IFunc, HopRes, Action, Event),
    HopRes \== TargetRes, 
    nonmember(IFunc, Visited),
    atom_concat('event flow action=', Action, EdgeAction),
    atom_concat('event flow event=', Event, EdgeEvent),
    rw_path(IFunc, ResType, TargetRes, IPath, IEdges, [Func | Visited], IFuncs, ILength, CFs, DFs, IEFs),
    Edges = [EdgeAction, EdgeEvent | IEdges],
    Path = [Func, HopRes | IPath],
    Funcs = [Func | IFuncs],
    EFs is 1 + IEFs,
    Length is 1 + ILength. % must compromise this function + functions on the internal path

% Find all read/write paths from a publicly accessible function to an internal resource
find_rw_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    function(EntryPoint, true),
    rw_path(EntryPoint, ResType, TargetRes, Path, IEdges, [EntryPoint], Funcs, Length, ICFs, DFs, EFs),
    Edges = ['public invoke' | IEdges],
    CFs is 1 + ICFs.
% Find all read/write paths through a publicly accessible resource to an internal resource (public data flow)
% Case 1 explicit permission, explicit resource
find_rw_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, Perm, EntryPoint),
    rw_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 2 explicit permission, wildcard resource
find_rw_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, Perm, CandidateEntryPoint),
    strip_star(CandidateEntryPoint, EntryPointRoot),
    re_match(EntryPointRoot, EntryPoint),
    rw_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 3 wildcard permission, explicit resource
find_rw_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, CandidatePerm, EntryPoint),
    strip_star(CandidatePerm, PermRoot),
    re_match(PermRoot, Perm),
    rw_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.
% Case 4 wildcard permission, wildcard resource
find_rw_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    resource(EPType, EntryPoint, _, true),
    EntryPoint \== '',
    function(Func, false), Func\=='',
    read_perm(EPType, Perm),
    permission(Func, CandidatePerm, CandidateEntryPoint),
    strip_star(CandidatePerm, PermRoot),
    strip_star(CandidateEntryPoint, EntryPointRoot),
    re_match(PermRoot, Perm),
    re_match(EntryPointRoot, EntryPoint),
    rw_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, IDFs, EFs),
    atom_concat('data flow read=', Perm, ReadEdge),
    Edges = ['public write', ReadEdge | IEdges],
    Path = [EntryPoint | IPath],
    DFs is 1 + IDFs.

% Find all read/write paths from a publicly accessible resource that triggers a function (public event flow)
find_rw_paths(EntryPoint, TargetRes, TargetRead, TargetWrite, Path, Edges, Visited, Funcs, Length, CFs, DFs, EFs) :-
    resource(ResType, TargetRes, TargetRead, TargetWrite),
    TargetRes \== '',
    public_event_flow(Func, EntryPoint, Action, Event),
    EntryPoint \== TargetRes,
    rw_path(Func, ResType, TargetRes, IPath, IEdges, [], Funcs, Length, CFs, DFs, IEFs),
    Edges = [Action, Event | IEdges],
    Path = [EntryPoint | IPath],
    EFs is 1 + IEFs.

% Find path with read access to a non-public resource and write access to a public resource
exfil_to_public_res(EntryPoint, PrivateRes, PublicRes,
  ReadPath, ReadEdges, ReadLength, RCFs, RDFs, REFs,
  WritePath, WriteEdges, WriteLength, WCFs, WDFs, WEFs) :-
    resource(PrivateResType, PrivateRes, false, false),
    PrivateRes \== '',
    resource(PublicResType, PublicRes, true, _),
    PublicRes \== '',
    PrivateRes \== PublicRes,
    find_read_paths(EntryPoint, PrivateRes, false, false, ReadPath, ReadEdges, [], RFuncs, ReadLength, RCFs, RDFs, REFs),
    find_write_paths(EntryPoint, PublicRes, true, false, WritePath, WriteEdges, [], WFuncs, WriteLength, WCFs, WDFs, WEFs).

% Note Visited can be used in the future to exclude certain functions if desired.

% find_read_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs).
% find_read_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, 1, CFs, DFs, EFs). % can fix lengths etc.

% find_write_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs).

% find_rw_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs).

% exfil_to_public_res(EntryPoint, PrivRes, PubRes, RPath, REdges, RLength, RCFs, RDFs, REFs, WPath, WEdges, WLength, WCFs, WDFs, WEFs).

