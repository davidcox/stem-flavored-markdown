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

% Comments are terribly useful, so we're adding them back in with the "%" character

# This is a test of "STEM-flavored" markdown [@intro]

Here is a paragraph la la la, blah dee blee dee bloo bloo. It can contain
references to [sections][ref-link].

Wouldn't it be cool if we could just cite papers like you would in real life [Cox et al., 2011].  Ambiguous matches could be resolved via interactive queries (possibly even run lint-style in the editor) and "letter"-style citations [Cox et al., 2007b]. It should also be possible to cite things by bibtex-style keys [@PiDoDiCo09, @PiCo12].

I'm going to try and put in a figure now:

% The figure co-opts the fenced code block structure with the "figure" language.
% the contents will be parsed as a stem-md document.
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

% Ref-links and footnotes are processed normally
[ref-link]: blah.com

