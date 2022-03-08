# This project is an example of WebScraping with a JavaScript Project

To execute the project in local, you need to setup a Splash server on port 8050

Then, if you have scrapy installed on your PC, you can run the command:

> `scrapy crawl quotes -o quotes.json`

To have an output of the website [Quotes](http://quotes.toscrape.com/js/) in a JSON file

Example of output :

```
[
{"quote": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”", "author": "Albert Einstein", "tags": ["change", "deep-thoughts", "thinking", "world"]},
{"quote": "“It is our choices, Harry, that show what we truly are, far more than our abilities.”", "author": "J.K. Rowling", "tags": ["abilities", "choices"]},
{"quote": "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”", "author": "Albert Einstein", "tags": ["inspirational", "life", "live", "miracle", "miracles"]},
{"quote": "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”", "author": "Jane Austen", "tags": ["aliteracy", "books", "classic", "humor"]},
{"quote": "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", "author": "Marilyn Monroe", "tags": ["be-yourself", "inspirational"]},
{"quote": "“Try not to become a man of success. Rather become a man of value.”", "author": "Albert Einstein", "tags": ["adulthood", "success", "value"]},
{"quote": "“It is better to be hated for what you are than to be loved for what you are not.”", "author": "André Gide", "tags": ["life", "love"]},
{"quote": "“I have not failed. I've just found 10,000 ways that won't work.”", "author": "Thomas A. Edison", "tags": ["edison", "failure", "inspirational", "paraphrased"]},
{"quote": "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", "author": "Eleanor Roosevelt", "tags": ["misattributed-eleanor-roosevelt"]},
{"quote": "“A day without sunshine is like, you know, night.”", "author": "Steve Martin", "tags": ["humor", "obvious", "simile"]}
]
```
