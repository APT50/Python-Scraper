# -*- coding: utf-8 -*-

BOT_NAME = 'cryptbb'

SPIDER_MODULES = ['cryptbb.spiders']
NEWSPIDER_MODULE = 'cryptbb.spiders'

DOWNLOADER_MIDDLEWARES = {
    'cryptbb.middlewares.ProxyMiddleware': 350
}

ITEM_PIPELINES = {
    'cryptbb.pipelines.SaveToFilePipeline': 300
}