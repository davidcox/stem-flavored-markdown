
# STEM (science, technology, engineering and math) -Flavored Markdown

## What is it?

This project is an attempt to gently augment the syntax of the popular Markdown lightweight markup language to better suit the needs of science/math/scholarly publishing.  The goal is to add some of the critical LaTeX-like features that Markdown currently lacks, which make Markdown, in its original form, unsuitable for composing scholarly communications.

The principle missing features are:

* **Full-fledged figure support:** currently things like multipart figures and multi-paragraph captions are not possible.  Even semi-long captions are weird and cumbersome.

* **Author, Institutition, etc. Meta-Data**: fields for specifying authorship, contact info, etc. a la Multimarkdown, but more full featured.  In particular, we'd like author institution annotations to be easy to specify in a human readable way.

* **In-line "plain text" citations:** many cite-while-you-write reference managers exist, with varying degrees of cumbersomeness and rigidity.  The SFM philosophy, following on the original Markdown philosophy, is that you should be able to write the citation more or less the way you would in an email, and the software should take care of formatting it the rest of the way.

* **Internal reference support:** LaTeX style "\ref{}" referencing for sections and figures is missing from most markdown dialects

## Example

The following is an illustrative example of the features I'm imagining:

```markdown

title: A Test Document
authors: David Cox (cox@rowland.harvard.edu) +,o,^
		 John Doe (doe@rowland.harvard.edu) +,^
institutions:
	+: The Rowland Institute at Harvard
	   100 Edwin H. Land Blvd.
	   Cambridge, MA 02142
	   http://www.rowland.harvard.edu
	o: Planet Earth
notes:
	^: Contributed equally


# This is a test of "STEM-flavored" markdown

Here is a paragraph la la la, blah dee blee dee bloo bloo. It can contain
references to sections: [this-is-a-test].

Wouldn't it be cool if we could just cite papers like you would in real life [Cox et al., 2011].  Ambiguous matches could be resolved via interactive queries (possibly even run lint-style in the editor) and "letter"-style citations [Cox et al., 2007b]

Proposed figure syntax:

 ~~~.figure
![test_figure](test.png)

Its caption could occupy arbitrarily many paragraphs.

And it could contain *formatting*.  Imagine that!
 ~~~


```