#!/bin/bash

count=0
yml_count=0

process_project () {
	# Find returns the full path match everything up to a / followed by a filename
	# (e.g., contains no slashes) ending in yaml or yml
	ymls=`find . -type f -regex ".*/[^/]*serverless[^/]*\.y[a]?ml" | wc -l`
	#echo "$topdir/$user has $ymls yml files"
	((yml_count=yml_count+ymls))
	((count=count+1))
}

cd serverless-dataset/
topdir=$PWD

for user in */ ; do
        # -- necessary to prevent directories with leading - from breaking script
        cd -- "$user"
        for repo in */ ; do
                cd -- "$repo"
		process_project
                cd -- $topdir/$user
        done
        cd -- $topdir
done

echo "$count projects processed."
echo "$yml_count candidate ymls found."
