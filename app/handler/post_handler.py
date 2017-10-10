import tornado.web

from handler.base_handler import BaseHandler
from model.models import *



class PostHandler(BaseHandler):
    def get(self,post_id):
        self.render("post.html",pager=None,talks_new=None, post=None,posts_hot=None, psers=None, ptids=None, ptags=None)
