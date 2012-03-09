title: A Test Document
authors:
    - David Cox (cox@rowland.harvard.edu) +,o,^
    - John Doe (doe@rowland.harvard.edu) +,^
institutions:
    +: The Rowland Institute at Harvard
       100 Edwin H. Land Blvd.
       Cambridge, MA 02142
       http://www.rowland.harvard.edu
    o: Planet Earth
notes:
    ^: Contributed equally


# This is a test of "STEM-flavored" markdown [@intro]

Here is a paragraph la la la, blah dee blee dee bloo bloo. It can contain
references to sections: [this-is-a-test].

Wouldn't it be cool if we could just cite papers like you would in real life [Cox et al., 2011].  Ambiguous matches could be resolved via interactive queries (possibly even run lint-style in the editor) and "letter"-style citations [Cox et al., 2007b]

I'm going to try and put in a figure now:


~~~ figure

![](test.png)

Its caption could occupy arbitrarily many paragraphs.

And it could contain *formatting*.  Imagine that!

~~~


~~~ figure
![multipart1](test.png)
![multipart2](test.png)

Its caption could occupy arbitrarily many paragraphs.

And it could contain *formatting*.  Imagine that!
~~~

