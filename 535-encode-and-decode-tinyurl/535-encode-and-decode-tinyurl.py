class Codec:
    def __init__(self):
        self.storedUrls = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = 'http://tinyurl.com/' + hex(hash(longUrl))[2:]
        self.storedUrls[shortUrl] = longUrl
        return shortUrl
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.storedUrls[shortUrl]