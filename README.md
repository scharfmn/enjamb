# prettyparse

### Uses the wonderful spaCy to do sentential and phrasal parsing, and produce and display an svg. 

The eventual goal is to develop an application that allows arguments about the effects of various sentence structures to have an ostensive basis. 

To put in another way: right now prettyparse does one best parse, and diagrams the input text. The goal is for this tool to be configurable to produce alternate parses when a sentence or phrase is grammatically ambiguous. 

Alternate parses can be especially useful in the discussion of enjambment: ambiguities among different grammatical resolutions for particular sentences, when broken in different ways, could be easily produced and displayed. 

Adapting Thomas Bever's classic example: “The horse raced past/ the barn fell.// Everyone was distraught.” might be parsed several ways. The first two lines might mean: “The horse raced past. The barn fell.” Or they might mean: “The horse, [that was] raced past the barn, fell.” The competing parses would be shown, allowing easy reference during a discussion. 

A second phase of development using the parse functionality would allow for stylistic analysis, such that a a poetic oeuvre could be uploaded via PDF (or other format) and parsed, with a report on the most common phrasal structures used, and the contexts or points in the poem where they generally appear. For example, a poet might turn to the conditional as inflection point three-quarters through a poem, and this might be a kind of signature, demonstrable across more poems in the oeuvre than not.

There are many suggestive possibilities for stylistic analysis of uploaded poems, but doing so would require that the uploaded poems be encoded in some sort of markup language. A recent pedagogical experiment within The Text Encoding Initiative (TEI) documents the “painstaking process of selecting bits of text and wrapping them with tags reframed reading as slow, iterative, and filled with formal choices” in putting together a digital edition of a poem using “the Text Encoding Initiative’s broad- based humanities tag set” (Singer). 

If the set of tags could be restricted to getting the title, stanzas, line-breaks, and sentences correct, then it’s possible that some form of machine learning (ML) could be used to do markup. A natural language processing (NLP) pipeline specific to phenomena like enjambment could then be developed utilizing the tags. I’m wary of advocating this, however, as I think it would be abused and be used to draw meaningless conclusions. The simple diagramming functionality, in contrast, can be used to teach the (lost art of) sentence diagramming, whereby one's hand-parses can be quickly compared with machine parses.
