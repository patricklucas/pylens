pylens
======

A simple Alfred-like shortcut widget.

Doesn't work on osx. Requires TKinter.

Usage
=====

do some command
-----------

    o command_to_run

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
    hn http://news.ycombinator
    
    # edit the config for pylens
    conf o gedit ~/pylens.conf
    
    ff o firefox
