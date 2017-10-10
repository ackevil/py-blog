import tornado.web

from handler.base_handler import BaseHandler
from model.models import *



class IndexHandler(BaseHandler):
    def get(self):
        try:
            terms = self.db.query(Term).all()
            print(terms[0].term_id)
            self.render("home.html",terms=terms,pager=None,talks_new=None, posts=None,posts_hot=None, psers=None, ptids=None, ptags=None)
        except Exception as e:
            self.db.rollback()
            print(e)

