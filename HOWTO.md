# Guide to Forking and Editing on GitHub

The following will guide you through the steps for "forking" the pre-work repository, which is where all of the material and exercises live. When you _fork_ a repository, you&apos;re making a personal copy of the pre-work. Everything you fork will show up in your **Repositories** section.

##Forking the repository 

Click the **Fork** button on the upper right hand corner of the repository:

![fork](img/forking_repo.png)

You&apos;ve successfully forked the pre-work repository. 

##Submitting answers

As you read through the pre-work, you will see the exercises that we **require** you to complete before your first day at Metis. There's two ways of submitting your answers: through the web interface in or through the terminal. 

###To submit using the web interface

It's as easy as clicking the **Edit this file** button:

![fork](img/edit_file.png)

Writing your answer in there and clicking on the Green **Commit changes** button.   

![fork](img/commit_file.png)

###To submit through Github

__*CLI knowledge is necessary*__

This will give you an overview of some very basic Git functionality, including **cloning, adding, committing and pushing.**

**Set up Git**    

__Only applicable if you&apos;ve never used Git before__

1. Download Git: http://git-scm.com/downloads
2. Go to the terminal. Type:

`git config --global user.name "YOUR NAME"`  
`git config --global user.email "YOUR EMAIL ADDRESS"`

**Create a local clone of your fork**

Right now, you&apos;ve got a copy of the pre-work repository, but you do not have the files on your comnputer. This is where a **clone** comes in.

1. In your fork of the pre-work repository, go the the right sidebar and click on the icon to copy the clone URL. 
2. On the terminal, type `git clone` and paste the URL. It should look like this now:  
`git clone https://github.com/YOUR_USERNAME/dsprework.git`  Press Enter.

You&apos;ve now got a copy of the pre-work in your computer.

**Sumbitting your work**

Once you are done writing out your answer, you will have to do three things in the terminal:
**DO THIS AFTER EVERY ANSWER**  

1. **Add** your work. Type:  

`git add .`  
_The dot after the word add will add all the files that you've modified._  

The file name you just modified should show up. It will say something like:  
 
`modified: python.md` 

2. **Commit** your work. Type:

`git commit -m 'brief description of commit'`  

3. **Push** your work up to GitHub.



