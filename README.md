# Meow
Meow is a font for cats designed by <a href="https://tribby.com/">Jeremy Tribby</a> and Jay Weiler.

Look what happens when a cat types using Meow:

![Cat Typing](https://raw.githubusercontent.com/jpt/meow/master/documentation/cat.png)

![Meow](https://raw.githubusercontent.com/jpt/meow/master/documentation/meow.gif)

# Limitations

This was a project done in an evening for the third annual San Francisco Stupid Shit No One Needs And Terrible Ideas Hackathon. The font works by using 7.3 million programmatically generated ligatures. We discovered some limitations when compiling OpenType features (including a hardcoded timeout in makeotf), so it is buggy -- we had to hack things a bit by using ranges of letters (classes) along with named lookups, which results in that recusion thing. The font is also super slow. Font renderers aren't exactly optimized for 7.3 million ligatures (for comparison, Helvetica has three).
