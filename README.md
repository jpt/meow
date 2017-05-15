# Meow
Meow is a font for cats designed by <a href="https://tribby.com/">Jeremy Tribby</a> and Jay Weiler.

Look what happens when a cat types using Meow:

![Cat Typing](https://raw.githubusercontent.com/jpt/meow/master/documentation/cat.png)

![Meow](https://raw.githubusercontent.com/jpt/meow/master/documentation/meow.gif)

# Limitations

This font works by using 7.3 million programmatically generated ligatures. We discovered some limitations of the OpenType features spec in creatinng it (including a hardcoded timeout in makeotf), so it is buggy -- we had to hack things a bit by using ranges of letters in classes within named lookups.
