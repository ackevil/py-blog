import json
import os
import binascii
import tornado.web




class BaseHandler(tornado.web.RequestHandler):

    __TOKEN_LIST = {}

    @property
    def db(self):
        return self.application.db


    def generate_token(self):
        while True:
            new_token = binascii.hexlify(os.urandom(16)).decode("utf-8")
            if new_token not in self.__TOKEN_LIST:
                return new_token

    def set_token(self,user_id):
        token = self.generate_token();
        self.__TOKEN_LIST[token] = user_id
        self.set_secure_cookie('_token', token)
        self.set_secure_cookie('_user_id',user_id)
    
    def get_current_user(self):
        token = self.get_secure_cookie("_token")
        user_id = self.get_secure_cookie("_user_id")
        if user_id and token and token in self.__TOKEN_LIST:
            return user_id == self.__TOKEN_LIST[token]
        return None
