class UrlShortener:
    def __init__(self):
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.base = len(self.chars)

    def shorten(self, url_id):
        """
        :param url_id:
        :return: str
        """
        short_str = ""
        if url_id == 0:
            return [url_id]

        while url_id > 0:
            short_str += self.chars[url_id % self.base]
            url_id //= self.base

        short_str = short_str[len(short_str):: -1]

        return short_str

    def un_shorten(self, short_str):
        """
        :param short_str:
        :return:
        """
        val_hash = []
        for shrt in short_str:
            try:
                val_hash.append(self.chars.index(shrt))
            except ValueError:
                continue

        val_hash = list(reversed(val_hash))
        url_id = 0
        for idx, val in enumerate(val_hash):
            url_id += (val * (self.base ** idx))

        return url_id
