moodle-book
============

A Course Creation tool for generating moodle books + a general moodle-independent static course web site from markdown content.

##Introduction

The `moodle book` command-line course creation tool will generate a set of moodle books:

- [Moodle Books](http://docs.moodle.org/26/en/Book)

based on folders and files of markdown content:

- [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

The tool also generates a static web site from the course materials, containing additional content encapsulating topic outlines, pdf slides and overall course structure. A demo of the system is visible here:

- [moodle-book-skeleton-site](http://edeleastar.github.io/moodle-book-skeleton/public)

The moodle books [are generated as zip archives, ready for upload to a Moodle virtual learning service

This 'source' for this demo course can be cloned from this public repo:

- [moodle-book-skeleton](https://github.com/edeleastar/moodle-book-skeleton)

or directly downloaded as a zip here:

- [moodle-book-skeleton.zip](https://github.com/edeleastar/moodle-book-skeleton/archive/master.zip)

The content is styled using the Semantic UI framework:

- <http://semantic-ui.com/>

Additionally, source code is syntax highlighted using the Highlight.js library:

- <http://highlightjs.org/>

This is incorporated as `fenced code blocks`, an example here:

- [code blocks](http://edeleastar.github.io/moodle-book-skeleton/public/topic01/book/index.html#/02)

##Installation

The system requires Python 2.7 to be installed. In addition, the python installation will need the 'easy_install' utility to be included on the path. If these are in place, then the following commands will include in python the requisite libraries:

~~~
easy_install markdown
easy_install jinja2
~~~

The system will not run unless these are installed successfully.  To install the moodle-book tool, clone this repository:

 - [moodle-book](https://github.com/edeleastar/moodle-book)

 or just download and unarchive a zipped version:

 - [moodle-book.zip](https://github.com/edeleastar/moodle-book/archive/master.zip)

Then place './moodle-book/app' on the path.

##Test

To test the system, clone the demo repository:

- [moodle-book-skeleton](https://github.com/edeleastar/moodle-book-skeleton) ([zip](https://github.com/edeleastar/moodle-book-skeleton/archive/master.zip))

Run a shell/command prompt and change into the moodle-demo-skeleton folder and enter:

~~~
mb.py
~~~

If all goes smoothly, you should see on the console a list of the topics as they are generated:

~~~
Publishing full course
Writing topic01
  -->Lab 01

Writing topic02
  -->Lab 02-A

  -->Lab 02-B

Writing topic03
  -->Lab 03
~~~

Open the ./public/index.html folder and it should resemble:

- [moodle-book-skeleton](https://github.com/edeleastar/moodle-book-skeleton)

##Structure

The course structure is derived from conventions represented in the directory and file names:

~~~
├── course.md
├── credits
├── topic01
│   ├── book
│   │   ├── 00.Lab-01.md
│   │   ├── 01.01.md
│   │   ├── 02.02.md
│   │   ├── 03.03.md
│   │   ├── 04.04.md
│   │   ├── 05.05.md
│   │   ├── 06.Exercises.md
│   │   ├── archives
│   │   │   └── archive.zip
│   │   └── img
│   │       ├── 01.png
│   │       ├── 02.png
│   │       └── 03.png
│   ├── pdf
│   │   ├── slides-1.pdf
│   │   ├── slides-2.pdf
│   │   └── slides-3.pdf
│   └── topic.md
~~~

(Just showing one topic)

- course.md: Course title + summary
- credits: list of contributors
- topic01: the first topic
- topic02: the second topic
- etc..

Each topic consists of:

- topic.md: Topic title + summary
- pdf: a collection of PDFs, usually slide decks or other documents
- book: the source for a `moodle book`, which will also be produced as a standalone web site. There can me several of these, each one must be named beginning with 'book', eg. book-01, book-02 etc...

Each book then contains the 'chapters' in the book, numbered as  `Number.Title.md`, where number is typically two digits starting with `00`. Eg:

- 00.Lab-01.md
- 01.01.md
- 02.02.md
- 03.03.md
- 04.04.md
- 05.05.md
- 06.Exercises.md

In the above lab, the static site will have titles 'Lab-01', '01', '02' ... 'Exercises' for each step/chapter. However, when loaded as a 'book' resource onto moodle, the actual content title (for each page) will be used. 

If one of the chapters needs images or other resources, then can be placed in subdirectories of the book and will be encapsulated into the generated site/resource. Use standard markdown relative linking (examples in the moodle-book-skeleton). 

##The mb.py command

The `mb.py` command can be run from any of the folders. If within a book, it will just generate the book resources. If in a topic, it will generate the topic resorce + all contained books. And if in the course (top level) folder, it will generate the complete course. It always generates this to the './public' folder.

##Customisation

The 'moodke-book/app/view' folder:

- [views](https://github.com/edeleastar/moodle-book/tree/master/app/views)

contains templates adhering to the [jinja2](http://jinja.pocoo.org/docs/templates/) templating language, and styled using [Semantic ui](http://semantic-ui.com/) These templates are defined:

- bookmain.html
- chapter.html
- course.html
- lab.html
- main.html
- topic.html

Representing different aspects of the generated resources. You can modify these to change style, introduce new elements etc. Please note, though, that if you edit these they may be overwritten if you pull on moodle-book repo again, so back them up before doing so.

Additionally, there are other opportunities for customisation in this folder '/moodle-book/public/custom/', where you can augment the existing main.css and main.js files. Again these will be overwritten by a pull on the repo, so do not loose your changes in that event.

##Hosting

###On Moodle:

There are two options for hosting the individual 'books' on moodle.

1. Use the Moodle `book` feature. To do this, create a 'book' resource in moodle, and, once created, select 'import chapter'. You can then drag/drop the book archive into the prompted pane in moodle. The book archive, which is in the appropriate folder in the './public' folder, will typically be called `book.zip` (or perhaps book-01.zip if you have several books per topic). Once you press 'import' and then 'continue' moodle will create a book resource in your topic, including a correct ToC based on actual chapter headers.

2. The generated lab folders (called book-archive.zip) can be dropped straight onto a moodle topic, and unarchived there. Set the 'main page' to the first html page of the lab. 

###On Github

The full course web can be hosted on an hosting service. On guthub, create repository, and create a branch called 'gh-pages'. Commit the './public' folder to this branch and push to github. The course will be available on 'yourname.github.io/repisitoryname/public'

###On Bitbucket:

Bitbucket have a similiar mechanism for hosting static sites:

- [Hosting Static Sites on Bitbucket](https://confluence.atlassian.com/display/BITBUCKET/Publishing+a+Website+on+Bitbucket)



