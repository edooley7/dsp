# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>pwd: print where you are on the computer 

>hostname: display name of computer and network you’re on

>mkdir: make a new folder (-p creates a whole path of files)

>cd: change which folder you’re in (just cd goes to home directory.   cd with folder/file name can go to that location below where you currently are.  Use cd ../.. to go up two levels.  Use cd /foldername to go up levels.)

>ls: list the files and folders in the folder you’re currently in

>rmdir: remove a folder (only when folder is empty.  Use rm to delete files.  Use rm -i to make sure you don’t accidentally delete something you need!)

>pushd: save the location where you currently are and go somewhere else

>popd: return to last location pushed

>cp: copy a file or folder (cp -r copies folders with files in them.)

>mv: move a file or folder (rename)

>less: page through a file (while in file, spacebar pages down, w pages up, q quits)	

>cat: print the whole file (Cmd-d to exit)

>rm: remove file (rm -rf deletes folder and contents. Careful here.)

>xargs: execute arguments

>find: find files (find STARTDIR -name “WILDCARD.filetype” -print)

>grep: find inside files (Use quotes to find words.)

>man: read a manual page

>apropos: find what manual page is appropriate

>env: look at your environment

>echo: print some arguments

>export: export/set new environment variable (unset to remove)

>exit: exit the shell

>xargs: execute arguments 

>chmod: change permission modifiers

>chown: change ownership of a file

>sudo: run programs with the security privileges of another user, including the super user. 

>#Other notes:
>Need to include quotes around folders and files with spaces in the name

>$|$ Uses output from command on left as input for the command on the right

>$>$ Takes the output from the command on the left and writes it into the file on the right

>$<$ Takes the input from the file on the right and sends to the program on the left.

>$>>$ Takes the output from the command on the left and appends it to the file on the right

>* - wildcard


---


---

>What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>`ls` lists all the files and folders contained in the folder you are currently in.  

>`ls -a` will list the same files and folders, plus any hidden files (hidden files contain a dot)

>`ls -l` will list files and folders in long format.  This includes permissions and date/time last modified, among other things.

>`ls -lh` uses unit suffixes (Byte, KB, MB, GB, TB, PB) to display the file size to reduce number of digits shown

>`ls -la` will list all files and folders (including hidden ones) in long format.

>`ls -lha` or `ls -lah` will both give long format, with reduced file size, for all files and folders, including hidden ones.

---


---

What does `xargs` do? Give an example of how to use it.

>`xargs` is used to pass the output of one command as an argument to another command.  You could use it to rename a batch of files at one time.  `ls *.log | xargs -i mv {} {}_bkp`  will take all log files and add _bkp to the end of the file names.  

---
