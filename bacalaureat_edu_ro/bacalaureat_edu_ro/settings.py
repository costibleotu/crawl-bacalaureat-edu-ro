# -*- coding: utf-8 -*-

# Scrapy settings for bacalaureat_edu_ro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bacalaureat_edu_ro'

SPIDER_MODULES = ['bacalaureat_edu_ro.spiders']
NEWSPIDER_MODULE = 'bacalaureat_edu_ro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bacalaureat_edu_ro (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5


FEED_EXPORTERS = {
    'csv': 'bacalaureat_edu_ro.exporters.bacalaureatCsvItemExporter',
}


FEED_FORMAT = 'csv'
CSV_DELIMITER = ';'
CSV_QUOTECHAR = '"'

CSV_FIELDS_TO_EXPORT = ['an','judet','nume','pozitia_pe_judet','pozitia_pe_tara','unitate_de_invatamant','promotie_anterioara','forma_invatamant','specializare','lb_romana_oral','lb_romana_scris','lb_romana_contestatie','lb_romana_final','lb_materna','lb_materna_oral','lb_materna_scris','lb_materna_contestatie','lb_materna_final','lb_moderna','lb_moderna_oral','disciplina_obligatorie_scris','disciplina_obligatorie_scris_nota','disciplina_obligatorie_scris_contestatie','disciplina_obligatorie_scris_final','disciplina_alegere_aria_culiculara','disciplina_alegere_aria_culiculara_nota','disciplina_alegere_aria_culiculara_contestatie','disciplina_alegere_aria_culiculara_final','disciplina_alegere_celelalte_arii_culiculare','disciplina_alegere_celelalte_arii_culiculare_nota','disciplina_alegere_celelalte_arii_culiculare_contestatie','disciplina_alegere_celelalte_arii_culiculare_final','competente_digitale','media','rezultat','url']

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bacalaureat_edu_ro.middlewares.BacalaureatEduRoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'bacalaureat_edu_ro.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bacalaureat_edu_ro.pipelines.BacalaureatEduRoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
