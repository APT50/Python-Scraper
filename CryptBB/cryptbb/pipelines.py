# -*- coding: utf-8 -*-


from config import OUTPUT_FILE


class SaveToFilePipeline(object):
    def __init__(self):
        self.output_file = open(OUTPUT_FILE, 'w')

    def process_item(self, item, spider):
        self.output_file.write(item['url'] + "\n")
        return item

    def close_spider(self, spider):
        self.output_file.close()
