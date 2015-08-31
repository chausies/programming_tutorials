cd Documents # change directory to the Documents directory

cd ~ # ~ is the name of your HOME directory

cd .. # .. is an alias which means "previous directory". 
      # Takes you back a directory. A single dot "." is 
      # an alias for "current directory"

ls # list all the shit in the current directory: Documents

rm FILE # removes a file. CAN'T BE UNDONE

rm -r DIR # removes a directory. CAN'T BE UNDONE

git status # check the status of your local
           # git repo (are there changes that you
           # haven't committed, files that you 
           # haven't added?

git pull # pull everything from origin (github)
         # to master (your local thingy)

git commit FILE -m "MESSAGE DESCRIBING CHANGES" # commits the 
                                                # changes you made to FILE

git commit -a -m "MESSAGE ABOUT CHANGES" # commits ALL changes 
                                         # you've made to TRACKED files
                                         # Note that only files that have
                                         # previously been added are
                                         # tracked.

git add FILE # Starts tracking a newly created file.

git add .  # Remember "." refers to the current directory.
           # This command tracks everything in the current 
           # directory that isn't.

git push origin master # pushes all committed changes on master
                       # (the local repo) to the origin (github)
                       # WARNING: ALWAYS make sure to run "git pull"
                       # right BEFORE running git push.
          # already being tracked
# :q quit vim
# :w save vim
# ctrl+r redo
# if anything goes wrong in vim, hit "escape" over and over again, and then "u" to undo as much as necessary


