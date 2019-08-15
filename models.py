from manage import db
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(32))
    email = db.Column(db.String(64))
# class Article(db.Model):
#     __tablename__ = "article"
#     id = db.Column(db.Integer,primary_key = True)
#     title = db.Column(db.String(32))
#     author = db.Column(db.String(32))
#     picture = db.Column(db.String(32))
#     time = db.Column(db.DATETIME)
#     types = db.Column(db.String(32))
#     content  = db.Column(db.TEXT)
#     description = db.Column(db.TEXT)
#
#     def __repr__(self):
#         return self.title
#
#
# class Image(db.Model):
#     __tablename__ = "image"
#     id = db.Column(db.Integer, primary_key=True)
#     label = db.Column(db.String(32))
#     picture = db.Column(db.String(32))
#     time = db.Column(db.DATETIME)
#     description = db.Column(db.TEXT)
#
#     def __repr__(self):
#         return self.label
class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)  #id
    nickname = db.Column(db.String(32))           #昵称
    qq = db.Column(db.String(32))            #qq
    email   = db.Column(db.String(64))            #邮箱
    time = db.Column(db.DATETIME)                 #时间
    description = db.Column(db.TEXT)              #留言内容
    def __repr__(self):
        return self.nickname
db.create_all()