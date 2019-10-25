toencode="https://leetcode.com/problems/design-tinyurl"
egEncoded="http://tinyurl.com/4e9iAk"
import random
class EncoderDecoder:
    def __init__(self):
        self.allowedChar="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.maxLengthAllowed=6
        self.prefix="http://tinyurl.com/"
        self.lookup={}

    def encoderHelper(self,url):


        def encoderGenerator():
            encodedURL=''
            for i in range(self.maxLengthAllowed):
                encodedURL+=self.allowedChar[random.randint(0,len(self.allowedChar)-1)]
            return encodedURL
        key=encoderGenerator()
        while key in self.lookup:
            key=encoderGenerator()

        self.lookup[key]=url
        return self.prefix+key


    def decoderHelper(self,key):
        return self.lookup[key[len(self.prefix):]]

obj=EncoderDecoder()

a=(obj.encoderHelper(toencode))
print(a)
print(obj.decoderHelper(a))


