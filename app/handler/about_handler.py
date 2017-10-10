import tornado.web

from handler.base_handler import BaseHandler
from model.models import *



class AboutHandler(BaseHandler):
    def get(self):
        self.render("about.html")
