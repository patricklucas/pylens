pylens
======

A simple Alfred-like shortcut widget.

Requires TKinter.

Usage
=====

do some command
-----------

    o some_command

go to a website
---------------

    www.website.biz

search google
-------------

    search_term

custom lenses
-------------

you can create macros to define custom queries and searches like this:

    conjugate deber

which will then be interpreted as

    http://www.spanishdict.com/translate/deber#conjugation

for this you will need to create the config file *~/pylens.conf*

a lens takes the form of:

    command macro

and in your macro string you will put the toke *{query}*, which will be replaced with the user's query when they run your macro. To make the macro above, I put

    conjugate http://www.spanishdict.com/translate/{query}#conjugation

in my config file. You can put comments with *#*.

You can use lenses to create "shortcuts":

    # cool website
    hn http://news.ycombinator.com
    
    # edit the config for pylens
    conf o gedit ~/pylens.conf
    
    ff o firefox

getting the most out of pylens
==========================

In your distro settings, assign a keyboard shortcut you find intuitive (I like Alt+Space), and have python call *pylens.py*. The program closes if it loses focus or gets no/bad input.
