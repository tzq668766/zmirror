# coding=utf-8
# 这是为Google和中文维基(无缝整合)镜像配置的示例配置文件
#
# 使用方法:
#   复制本文件到 zmirror.py 同级目录, 并重命名为 config.py
#
# 各项设置选项的详细介绍请看 config_default.py 中对应的部分
# 本配置文件假定你的服务器本身在墙外
# 如果服务器本身在墙内(或者在本地环境下测试, 请修改`Proxy Settings`中的设置
#
# 由于google搜索结果经常会出现中文维基, 所以顺便把它也加入了.
# google跟中文维基之间使用了本程序的镜像隔离功能, 可以保证中文维基站的正常使用
#
# 本配置文件试图还原出一个功能完整的google.
#   但是由于程序本身所限, 还是不能[完整]镜像过来整个[google站群]
#   在后续版本会不断增加可用的网站
#
# 以下google服务完全可用:
#   google网页搜索/学术/图片/新闻/图书/视频(搜索)/财经/APP搜索/翻译/网页快照/...
#   google搜索与中文维基百科无缝结合
# 以下服务部分可用:
#     gg地图(地图可看, 左边栏显示不正常)/G+(不能登录)
# 以下服务暂不可用(因为目前无法解决登录的问题):
#     所有需要登录的东西, docs之类的
#

# Github: https://github.com/aploium/zmirror

# ############## Local Domain Settings ##############
my_host_name = '127.0.0.1'
my_host_scheme = 'http://'
my_host_port = None  # None表示使用默认端口, 可以设置成非标准端口, 比如 81

# ############## Target Domain Settings ##############
target_domain = 'www.google.com.hk'
target_scheme = 'https://'

# 这里面大部分域名都是通过 `enable_automatic_domains_whitelist` 自动采集的, 我只是把它们复制黏贴到了这里
# 实际镜像一个新的站时, 手动只需要添加很少的几个域名就可以了.
# 自动采集(如果开启的话)会不断告诉你新域名
external_domains = (
    'www.google.com',
    'webcache.googleusercontent.com',  # Google网页快照
    'images.google.com.hk',
    'images.google.com',
    'apis.google.com',

    # Google学术
    'scholar.google.com.hk',
    'scholar.google.com',

    # 中文维基百科
    'zh.wikipedia.org',
    'zh.m.wikipedia.org',
    'upload.wikipedia.org',
    'meta.wikimedia.org',
    'login.wikimedia.org',

    # Google静态资源域名
    'ssl.gstatic.com',
    'www.gstatic.com',
    'encrypted-tbn0.gstatic.com',
    'encrypted-tbn1.gstatic.com',
    'encrypted-tbn2.gstatic.com',
    'encrypted-tbn3.gstatic.com',
    'csi.gstatic.com',
    'fonts.googleapis.com',

    # Google登陆支持
    'accounts.google.com',
    'accounts.youtube.com',
    'accounts.google.com.hk',
    'myaccount.google.com',
    'myaccount.google.com.hk',

    'ajax.googleapis.com',
    'translate.google.com',
    'translate.google.com.hk',
    'video.google.com.hk',
    'books.google.com',
    'cloud.google.com',
    'analytics.google.com',
    'security.google.com',
    'investor.google.com',
    'families.google.com',
    'clients1.google.com',
    'clients2.google.com',
    'clients3.google.com',
    'clients4.google.com',
    'clients5.google.com',
    'talkgadget.google.com',
    'news.google.com.hk',
    'news.google.com',
    'support.google.com',
    'docs.google.com',
    'books.google.com.hk',
    'chrome.google.com',
    'profiles.google.com',
    'feedburner.google.com',
    'cse.google.com',
    'sites.google.com',
    'productforums.google.com',
    'encrypted.google.com',
    'm.google.com',
    'research.google.com',
    'maps.google.com.hk',
    'hangouts.google.com',
    'developers.google.com',
    'get.google.com',
    'afp.google.com',
    'groups.google.com',
    'payments.google.com',
    'photos.google.com',
    'play.google.com',
    'mail.google.com',
    'code.google.com',
    'tools.google.com',
    'drive.google.com',
    'script.google.com',
    'goto.google.com',
    'calendar.google.com',
    'wallet.google.com',
    'privacy.google.com',
    'ipv4.google.com',
    'video.google.com',
    'store.google.com',
    'fi.google.com',
    'apps.google.com',
    'events.google.com',
    'notifications.google.com',
    'plus.google.com',

    'scholar.googleusercontent.com',
    'translate.googleusercontent.com',
    't0.gstatic.com',
    't1.gstatic.com',
    't2.gstatic.com',
    't3.gstatic.com',
    's-v6exp1-ds.metric.gstatic.com',
    'ci4.googleusercontent.com',
    'gp3.googleusercontent.com',
    'accounts.gstatic.com',

    # For Google Map (optional)
    'maps-api-ssl.google.com',
    'maps.gstatic.com',
    'maps.google.com',
    'fonts.gstatic.com',
    'lh1.googleusercontent.com',
    'lh2.googleusercontent.com',
    'lh3.googleusercontent.com',
    'lh4.googleusercontent.com',
    'lh5.googleusercontent.com',
    'lh6.googleusercontent.com',

    # 'upload.wikimedia.org',
    'id.google.com.hk',
    'id.google.com',
)

# 强制所有Google站点使用HTTPS
force_https_domains = 'ALL'

# 自动动态添加域名
enable_automatic_domains_whitelist = True
domains_whitelist_auto_add_glob_list = (
    '*.google.com', '*.gstatic.com', '*.google.com.hk', '*.googleapis.com')

# ############## Proxy Settings ##############
# 如果你在墙内使用本配置文件, 请指定一个墙外的http代理
is_use_proxy = False
# 代理的格式及SOCKS代理, 请看 http://docs.python-requests.org/en/latest/user/advanced/#proxies
requests_proxies = dict(
    http='http://127.0.0.1:8123',
    https='https://127.0.0.1:8123',
)

# ############## Sites Isolation ##############
enable_individual_sites_isolation = True

# 镜像隔离, 用于支持Google和维基共存
isolated_domains = {'zh.wikipedia.org', 'zh.m.wikipedia.org'}

# ############## URL Custom Redirect ##############
# 这是一个方便的设置, 如果你访问 /wiki ,程序会自动重定向到后面这个长长的wiki首页
url_custom_redirect_enable = True
url_custom_redirect_list = {'/wiki': '/extdomains/https-zh.wikipedia.org/'}
