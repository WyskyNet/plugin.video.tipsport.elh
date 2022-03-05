class UserData:
    def __init__(self, username, password, site, javtg_headers_url):
        self.username = username
        self.password = password
        self.site = 'https://www.' + site
        self.site_mobile = 'https://m.' + site
        self.javtg_headers_url = javtg_headers_url
