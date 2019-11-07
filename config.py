import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

config_data = {
    'site': {
        'title': 'Nitratine',
        'url': 'https://nitratine.net',
        'domain': 'nitratine.net',
        'about': 'Owner of <a href=\"https://www.youtube.com/PyTutorials\">PyTurorials</a> and creator of <a href=\"https://github.com/brentvollebregt/auto-py-to-exe\">auto-py-to-exe</a>. I enjoy making quick tutorials for people new to particular topics in Python and  tools that help fix small things.',
        'theme_colour': '#343a40',
        'email': 'brent@nitratine.net',
        'youtube_link': 'https://www.youtube.com/PyTutorials',
        'github_username': 'brentvollebregt',
        'default_author': 'Brent Vollebregt',
        'disqus_shortname': 'nitratine',
        'google_analytics_id': 'UA-117153268-2',
        'google_adsense_publisher_id': 'pub-6407227183932047',
        'youtube_channel_name': 'PrivateSplat',
        'youtube_channel_id': 'UCesEknt3SRX9R9W_f93Tb7g',
        'youtube_data_api_key': os.getenv('YOUTUBE_DATA_API_KEY'),
        'category-extra': {
            'YouTube': '&#x1F3A5;',
            'Projects': '&#x1F4BE;',
            'Tutorials': '&#x1F4D6;',
            'Apps': '&#x1F4F1;',
            'Investigations': '&#x1F50D;',
            'Tools': '&#x1F6E0;',
            'Snippets': '&#x2702;',
            'General': '&#x1F4F0;'
        }
    },
    'redirects': {
        'tag': 'blog/tags',
        'category': 'blog/categories',
        'archive': 'blog/archive',
        'donations': 'about',
        'blog/post': 'blog',
        'colour': 'blog/post/colour',
        'finding-emotion-in-music-with-python': 'blog/post/finding-emotion-in-music-with-python',
        'interesting-sites': 'blog/post/interesting-sites',
        'randomly-generating-numbers-to-fulfil-an-integer-range': 'blog/post/randomly-generating-numbers-to-fulfil-an-integer-range',
        'convert-py-to-exe': 'blog/post/convert-py-to-exe',
        'get-wifi-passwords-with-python': 'blog/post/get-wifi-passwords-with-python',
        'how-to-setup-pythons-pip': 'blog/post/how-to-setup-pythons-pip',
        'how-to-get-mouse-clicks-with-python': 'blog/post/how-to-get-mouse-clicks-with-python',
        'python-keylogger': 'blog/post/python-keylogger',
        'simulate-keypresses-in-python': 'blog/post/simulate-keypresses-in-python',
        'quick-script': 'blog/post/quick-script',
        'lucy-in-the-sky-with-emotion': 'blog/post/lucy-in-the-sky-with-emotion',
        'monopoly-money': 'blog/post/monopoly-money',
        'mp3-itunes-downloader': 'blog/post/mp3-itunes-downloader',
        'spotify-playlist-downloader': 'blog/post/spotify-playlist-downloader',
        'adding-snow-to-your-website': 'blog/post/adding-snow-to-your-website',
        'change-file-modification-time-in-python': 'blog/post/change-file-modification-time-in-python',
        'the-nitratine-project': 'blog/post/the-nitratine-project',
        'how-to-make-hotkeys-in-python': 'blog/post/how-to-make-hotkeys-in-python',
        'simulate-mouse-events-in-python': 'blog/post/simulate-mouse-events-in-python',
        'how-to-send-an-email-with-python': 'blog/post/how-to-send-an-email-with-python',
        'python-retweet-bot': 'blog/post/python-retweet-bot',
        'python-auto-clicker': 'blog/post/python-auto-clicker',
        'auto-py-to-exe': 'blog/post/auto-py-to-exe',
        'hit-counter': 'blog/post/hit-counter',
        'github-badges': 'blog/post/github-badges',
        'my-desktop-backgrounds': 'blog/post/my-desktop-backgrounds',
        'how-to-add-a-custom-domain-to-a-github-pages-site': 'blog/post/how-to-add-a-custom-domain-to-a-github-pages-site',
        'python-threading-basics': 'blog/post/python-threading-basics',
        'python-gui-using-chrome': 'blog/post/python-gui-using-chrome',
        'python-sqlite3-basics': 'blog/post/python-sqlite3-basics',
        'price-per-unit': 'blog/post/price-per-unit',
        'putting-auto-py-to-exe-on-pypi': 'blog/post/putting-auto-py-to-exe-on-pypi',
        'media-picker': 'blog/post/media-picker',
        'python-guis-with-pyqt': 'blog/post/python-guis-with-pyqt',
        'how-to-clean-a-twitter-account-with-jquery': 'blog/post/how-to-clean-a-twitter-account-with-jquery',
        'multi-clipboard': 'blog/post/multi-clipboard',
        'uow-moodle-rwa-ignorer': 'blog/post/uow-moodle-rwa-ignorer',
        'am-i-a-participant': 'blog/post/am-i-a-participant',
        'asymmetric-encryption-and-decryption-in-python': 'blog/post/asymmetric-encryption-and-decryption-in-python',
        'common-issues-when-using-auto-py-to-exe': 'blog/post/common-issues-when-using-auto-py-to-exe',
        'encryption-and-decryption-in-python': 'blog/post/encryption-and-decryption-in-python',
        'blog/post/common-issues-when-using-auto-py-to-exe': 'blog/post/issues-when-using-auto-py-to-exe'
    },
    'home-tiles': [
        {
            'type': 'img-content',
            'link': 'https://github.com/brentvollebregt/auto-py-to-exe',
            'image_url': '/post-assets/auto-py-to-exe/feature.png',
            'content_raw': '<div class=\"text-center\"> <h5 class=\"card-title mb-1\">Auto Py to Exe</h5> <img alt=\"Total downloads for auto-py-to-exe project\" src=\"https://pepy.tech/badge/auto-py-to-exe\"> <br> <small class=\"text-muted\">pip install auto-py-to-exe</small> </div>'
        },
        {
            'type': 'image',
            'link': 'https://youtu.be/H8t4DJ3Tdrg',
            'image_url': 'https://img.youtube.com/vi/H8t4DJ3Tdrg/mqdefault.jpg'
        },
        {
            'type': 'post',
            'post': 'issues-when-using-auto-py-to-exe',
            'reason': 'Popular'
        },
        {
            'type': 'raw',
            'link': 'https://emotionify.nitratine.net/',
            'content': "<div class=\"text-center\"> <img class=\"card-img-top\" src=\"/post-assets/emotionify/emotionify-banner.png\" alt=\"Emotionify Banner\" style=\"padding: 20px 10px 20px 10px\"> <p class=\"mx-2\">Sort Spotify playlists using Spotify's pre-calculated audio features to attempt to emotionally gradient playlists.</p> </div>"
        },
        {
            'type': 'post',
            'post': 'python-encryption-and-decryption-with-pycryptodome',
            'reason': 'New'
        },
        {
            'type': 'image',
            'link': 'https://youtu.be/ksW59gYEl6Q',
            'image_url': 'https://img.youtube.com/vi/ksW59gYEl6Q/mqdefault.jpg'
        },
        {
            'type': 'image',
            'link': 'https://youtu.be/YPiHBtddefI',
            'image_url': 'https://img.youtube.com/vi/YPiHBtddefI/mqdefault.jpg'
        },
        {
            'type': 'post',
            'post': 'python-requests-tutorial',
            'reason': 'New'
        },
        {
            'type': 'post',
            'post': 'encryption-and-decryption-in-python',
            'reason': 'Popular'
        },
        {
            'type': 'image',
            'link': 'https://youtu.be/OZSZHmWSOeM',
            'image_url': 'https://img.youtube.com/vi/OZSZHmWSOeM/mqdefault.jpg'
        },
        {
            'type': 'raw',
            'link': 'https://spotify-lyrics-viewer.nitratine.net/',
            'content': "<div class=\"text-center\"> <img class=\"card-img-top\" src=\"/post-assets/spotify-lyrics-viewer/spotify-lyrics-viewer-banner.png\" alt=\"Spotify Lyrics Viewer\" style=\"padding: 20px 10px 20px 10px\"> <p class=\"mx-2\">Spotify Lyrics Viewer is a tool that allows you to view the lyrics of the current playing song on Spotify by simply signing in.</p> </div>"
        },
        {
            'type': 'post',
            'post': 'how-to-hash-passwords-in-python',
            'reason': 'New'
        },
        {
            'type': 'post',
            'post': 'simulate-keypresses-in-python',
            'reason': 'Popular'
        }
    ]
}


def get(*args):
    """ Traverse the config data to get a value """
    traversal = config_data
    try:
        for arg in args:
            traversal = traversal[arg]
    except KeyError:
        raise KeyError(f'Invalid key {args}')
    return traversal
