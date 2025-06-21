AUTHOR = 'Kadek Hendra Darma Sastrawan'
SITENAME = 'Kadek Hendra - Personal Website'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ['images']

# Blogroll
# LINKS = (
#     ("LinkedIn", "https://linkedin.com/hendra16"),
#     ("Instagram", "https://www.instagram.com/hendradrma/"),
# )

DISPLAY_PAGES_ON_MENU = False
# DISPLAY_CATEGORIES_ON_MENU = True
# MENUITEMS = (
#     ('About', '/about.html'),
#     ('Portfolio', '/portfolio.html'),
#     ('Blog', '/category/blog.html'),
# )

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)



DEFAULT_PAGINATION = 5
THEME = 'themes/Flex'
THEME_COLOR = 'dark'
CUSTOM_CSS = 'static/css/custom.css'
SITETITLE = "Kadek's Blog"
FAVICON = 'images/icon.ico'
THEME_STATIC_DIR = "images"

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
