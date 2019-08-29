# Introduction

The spider scrapes the website by using scrapy framework. To setup the project:

- Install project dependencies with ```pip install -r requirements.txt```
- Open config.py and configure the proxy settings and the output path where to save scraped webpages
- Run the spider with ```scrapy run cryptbb```


# Design

The spider makes use of Scrapy framework. The parse method in the spider class discovers all links on the current page
starting the home page.

The SaveToFilePipeline is the pipeline that receives scraped items and saves the URL in a file (one URL per line). 

The ProxyMiddleware is the middleware responsible to proxy all requests through the configured proxy.
