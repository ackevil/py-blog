from tornado.web import url
from handler.index_handler import IndexHandler
from handler.post_handler import PostHandler
from handler.about_handler import AboutHandler
routes = [
        url(r"/", IndexHandler, name='index'),
        url(r"/posts/([1-9]+[0-9]*)",PostHandler,name="post"),
        url(r"/about",AboutHandler,name="about")
        ]
