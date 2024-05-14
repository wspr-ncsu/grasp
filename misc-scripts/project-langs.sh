#!/bin/bash

count=0

process_project () {
	# Do some kind of processing
	toplang=`github-linguist | awk '{print $3; exit}'`
	echo "$user$repo,$toplang"
	((count=count+1))
}

cd serverless-dataset/
topdir=$PWD

echo "Full Name,Top Language"
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
