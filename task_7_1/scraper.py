import asyncio
import logging
import re
import aiohttp

from lxml import html
from data_store import DataStore


__author__ = "Andrew Gafiychuk"


class Scraper(object):
    """
    Class Scraper to asynchronous get and parse data from
    http://forum.overclockers.ua
    
    Takes 1 params - pages_count to async parse.
    start() - main method to start parsing.
    
    Return list of tuple-records, contains (author, title, link, post,)
    
    """
    def __init__(self, page_count):
        self.pages = page_count
        self.session = None

    async def _create_session(self):
        """
        Method to create client-server session for data transfer.
        Use aiohttp.TCPConnector()
            aiohttp.ClientSession()
        
        """
        logging.debug("[+]Create HEADERS/Sessions...")

        HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,'
                      'application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;'
                               'q=0.4,uk;q=0.2',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'forum.overclockers.ua',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/57.0.2987.133'
                          'Safari/537.36',
        }

        connector = aiohttp.TCPConnector(verify_ssl=True)
        self.session = aiohttp.ClientSession(connector=connector,
                                             headers=HEADERS)

        logging.debug("[+]Session created !!!")

    def urls_get(self):
        """
        Method to create URL's list for grabb and parse.
        Return url-list.
        
        """
        URL = 'http://forum.overclockers.ua/viewforum.php' \
              '?f=26&start={0}'

        urls = []

        start = 0
        for url in range(0, self.pages):
            urls.append(URL.format(start))
            start += 40

        return urls

    def start(self):
        """
        Main method to start async data get and parsing.
        Use asyncio.even_loop()
        
        Return data-list result.
        
        """
        logging.debug("[+]Starts _main even_loop...")

        event_loop = asyncio.get_event_loop()

        try:
            event_loop.run_until_complete(self._create_session())
            data = event_loop.run_until_complete(self._main())
        finally:
            logging.debug("[+]All coroutines complete !!!\n"
                          "[+]Close session/event_loop !!!")

            self.session.close()
            event_loop.close()

        return data

    async def _main(self):
        """
        
        """
        logging.debug("[+]Starting all tasks...")

        urls = self.urls_get()

        url_tasks = []
        topics_list = []

        for url in urls:
            url_tasks.append(self.get_topics_list(url))

        for task in asyncio.as_completed(url_tasks):
            topic = await task
            topics_list.extend(topic)
            task.close()

        logging.debug("[+]Topics load complete...")

        parse_tasks = []
        data_list = []

        for topic in topics_list:
            parse_tasks.append(self.get_posts_list(topic))

        for task in asyncio.as_completed(parse_tasks):
            post = await task
            data_list.append(post)
            task.close()

        logging.debug("[+]Posts data load complete...")
        logging.debug("[+]All tasks complete !!!")

        return data_list

    async def get_topics_list(self, url):
        """
        Method to get pages with topic list.
        Return topic-link list.
        
        """
        async with self.session.get(url) as response:
            if response.status == 200:
                page = await response.text()

                root = html.fromstring(page)

                class_list = ['forumbg announcement', 'forumbg']
                topics_list = []

                for cls in class_list:
                    topiclist = root.xpath(
                        '//div[@class="forum_wrapper"]'
                        '/div[@class="' + cls + '"]'
                        '/div[@class="inner"]'
                        '/ul[@class="topiclist topics"]'
                        '/li')

                    for topic in topiclist:
                        topic_link = str(topic.xpath(
                            './/dl/dt/'
                            'div[@class="list-inner"]'
                            '/a/@href')[0])

                        topics_list.append(topic_link)

                return topics_list
            else:
                logging.debug("[+]URL get error...\n"
                              "{0}".format(response.status))

    async def get_posts_list(self, url):
        """
        Method to get first post data from overclockers.ua.
        Parse author nick name, topic title, topic link, text.
        
        Return data-tuple.
        
        """

        # cut session id part from url
        url = url.split('&sid')[0]
        post_url = 'http://forum.overclockers.ua' + url

        async with self.session.get(post_url) as response:
            if response.status == 200:
                topic = await response.text()

                root = html.fromstring(topic)

                page_body = root.xpath(
                    '//div[@id="wrap"]'
                    '/div[@id="page-body"]')[0]

                title = page_body.xpath(
                    './/h2[@class="topic-title"]/a/text()')[0]

                topic_body = page_body.xpath(
                    './/div[@class="forum_wrapper"]'
                    '/div')[1]

                author = topic_body.xpath('.//div[@class="inner"]'
                                          '/dl/dt/a/text()')[0]

                post_content = topic_body.xpath(
                    './/div[@class="inner"]'
                    '/div[@class="postbody"]'
                    '/div/div[@class="content"]'
                    '/descendant-or-self::*/text()')

                text = "\n".join(post_content)\
                    .replace("спойлер", "").strip()

                re.sub(r'\\n{1,}', "", text)

                post_data = (author, title, post_url, text,)

                return post_data
            else:
                logging.debug("[+]Topic post 'get' error...\n"
                              "{0}".format(response.status))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("[+]App started...")

    # Starting scrapp posts
    parser = Scraper(1)
    data = parser.start()

    # Create DS, watch DS list...
    data_store = DataStore()
    data_store.get_ds_list()
    # Set DS type as json file and write first 21 records.
    data_store.set_ds_type("json")
    ds = data_store.create_data_store()
    ds.connect()

    for row in data[:21]:
        ds.insert_unique(*row)

    #Set DS type as csv file and write all remaining records.
    data_store.set_ds_type("csv")
    ds = data_store.create_data_store()
    for row in data[22:]:
        ds.insert_unique(*row)

    logging.debug("[+]App set_enable !!!")
