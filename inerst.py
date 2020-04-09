# -*- coding: utf-8 -*-
from app import User
from app import db


# m1 = Movie(title='Leon', year='1994')  # 创建一个 Movie 记录
# m2 = Movie(title='Mahjong', year='1996')  # 再创建一个 Movie 记录
# db.session.add(m1)  # 把新创建的记录添加到数据库会话
# db.session.add(m2)  # 把新创建的记录添加到数据库会话
# db.session.commit()  # 提交数据库会话，只需要在最后调用一次即可
# print(Movie.query.all() )
#
# movie = Movie.query.get(2)
# movie.title = 'WALL-E'  # 直接对实例属性赋予新的值即可
# movie.year = '2008'
# db.session.commit()  # 注意仍然需要调用这一行来提交改动
#
# movie = Movie.query.get(1)
# db.session.delete(movie)  # 使用 db.session.delete() 方法删除记录，传入模型实例
# db.session.commit()  # 提交改动