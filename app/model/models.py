# coding: utf-8
from sqlalchemy import BigInteger, Column, Index, Integer, String, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Alog(Base):
    __tablename__ = 'alogs'

    alog_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, server_default=text("'0'"))
    user_ip = Column(String(255))
    user_name = Column(String(255))
    alog_text = Column(Text)
    alog_data = Column(Text)
    alog_ctms = Column(BigInteger)


class Conf(Base):
    __tablename__ = 'confs'

    conf_name = Column(String(255), primary_key=True)
    conf_vals = Column(Text)
    conf_ctms = Column(BigInteger)


class File(Base):
    __tablename__ = 'files'

    file_id = Column(Integer, primary_key=True)
    file_hash = Column(String(255))
    file_base = Column(String(255))
    file_path = Column(String(255))
    file_type = Column(String(255))
    file_memo = Column(String(255))
    file_ctms = Column(BigInteger, nullable=False)


class Link(Base):
    __tablename__ = 'links'
    __table_args__ = (
        Index('index_linkRank_linkId', 'link_id', 'link_rank'),
    )

    link_id = Column(Integer, primary_key=True)
    link_name = Column(String(255))
    link_href = Column(String(255))
    link_desc = Column(Text)
    link_rank = Column(Integer, server_default=text("'99'"))
    link_ctms = Column(BigInteger)
    link_utms = Column(BigInteger)


class Mail(Base):
    __tablename__ = 'mails'
    __table_args__ = (
        Index('index_mailStat_mailId', 'mail_id', 'mail_stat'),
    )

    mail_id = Column(Integer, primary_key=True)
    user_ip = Column(String(64))
    user_name = Column(String(255))
    user_email = Column(String(64), nullable=False)
    mail_text = Column(Text)
    mail_stat = Column(Integer, server_default=text("'0'"))
    mail_ctms = Column(BigInteger, nullable=False)
    mail_utms = Column(BigInteger, nullable=False)


t_post_terms = Table(
    'post_terms', metadata,
    Column('post_id', Integer),
    Column('term_id', Integer),
    Index('index_postId_termId', 'post_id', 'term_id')
)


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = (
        Index('index_userId_postPtms_postStat', 'user_id', 'post_ptms', 'post_stat'),
        Index('index_postPtms_postStat_postRank', 'post_ptms', 'post_rank', 'post_stat'),
        Index('index_postPtms_postStat', 'post_ptms', 'post_stat'),
        Index('index_postId_postPtms_postStat', 'post_id', 'post_ptms', 'post_stat'),
        Index('index_postPtms_postStat_postRefc', 'post_ptms', 'post_refc', 'post_stat')
    )

    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, server_default=text("'0'"))
    post_title = Column(String(255))
    post_desc = Column(String(255))
    post_author = Column(String(255))
    post_source = Column(String(1024))
    post_summart = Column(Text)
    post_content = Column(Text)
    post_type = Column(Integer, server_default=text("'0'"))
    post_ctms = Column(BigInteger, nullable=False)
    post_utms = Column(BigInteger, nullable=False)
    post_ptms = Column(BigInteger, nullable=False)
    post_refc = Column(Integer, server_default=text("'0'"))
    post_rank = Column(Integer, server_default=text("'99'"))
    post_plus = Column(Integer, server_default=text("'0'"))
    post_mins = Column(Integer, server_default=text("'0'"))
    post_stat = Column(Integer, nullable=False, server_default=text("'0'"))


class Talk(Base):
    __tablename__ = 'talks'
    __table_args__ = (
        Index('index_postId_talkRank_talkId', 'talk_id', 'post_id', 'talk_rank'),
        Index('index_talkRank_talkId', 'talk_id', 'talk_rank')
    )

    talk_id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    user_id = Column(Integer, nullable=False, server_default=text("'0'"))
    user_ip = Column(String(255))
    talk_ptid = Column(Integer, nullable=False, server_default=text("'0'"))
    user_name = Column(String(255))
    user_email = Column(String(255))
    talk_text = Column(Text)
    talk_plus = Column(Integer, nullable=False, server_default=text("'0'"))
    talk_rank = Column(Integer, nullable=False, server_default=text("'100'"))
    talk_mins = Column(Integer, nullable=False, server_default=text("'0'"))
    talk_ctms = Column(BigInteger)
    talk_utms = Column(BigInteger)


class Term(Base):
    __tablename__ = 'terms'

    term_id = Column(Integer, primary_key=True)
    term_name = Column(String(255), nullable=False)
    term_refc = Column(Integer, server_default=text("'0'"))
    term_ctms = Column(Integer)


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_auid = Column(String(64), nullable=False, server_default=text("''"))
    user_name = Column(String(64), nullable=False)
    user_salt = Column(String(8), nullable=False)
    user_password = Column(String(32), nullable=False)
    user_perm = Column(Integer, nullable=False, server_default=text("'0'"))
    user_email = Column(String(255), nullable=False)
    user_sign = Column(String(255), nullable=False, server_default=text("''"))
    user_logo = Column(String(512), nullable=False, server_default=text("''"))
    user_meta = Column(Text)
    user_ctms = Column(BigInteger)
    user_utms = Column(BigInteger)
    user_atms = Column(BigInteger)
