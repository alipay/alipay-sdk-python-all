#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantshopCommentResult(object):

    def __init__(self):
        self._comment = None
        self._comment_time = None
        self._face = None
        self._imgs = None
        self._nick_name = None
        self._order_no = None
        self._reply = None
        self._reply_time = None
        self._score = None
        self._shop_id = None
        self._user_id = None
        self._user_name = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def comment_time(self):
        return self._comment_time

    @comment_time.setter
    def comment_time(self, value):
        self._comment_time = value
    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value
    @property
    def imgs(self):
        return self._imgs

    @imgs.setter
    def imgs(self, value):
        self._imgs = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def reply(self):
        return self._reply

    @reply.setter
    def reply(self, value):
        self._reply = value
    @property
    def reply_time(self):
        return self._reply_time

    @reply_time.setter
    def reply_time(self, value):
        self._reply_time = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.comment_time:
            if hasattr(self.comment_time, 'to_alipay_dict'):
                params['comment_time'] = self.comment_time.to_alipay_dict()
            else:
                params['comment_time'] = self.comment_time
        if self.face:
            if hasattr(self.face, 'to_alipay_dict'):
                params['face'] = self.face.to_alipay_dict()
            else:
                params['face'] = self.face
        if self.imgs:
            if hasattr(self.imgs, 'to_alipay_dict'):
                params['imgs'] = self.imgs.to_alipay_dict()
            else:
                params['imgs'] = self.imgs
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.reply:
            if hasattr(self.reply, 'to_alipay_dict'):
                params['reply'] = self.reply.to_alipay_dict()
            else:
                params['reply'] = self.reply
        if self.reply_time:
            if hasattr(self.reply_time, 'to_alipay_dict'):
                params['reply_time'] = self.reply_time.to_alipay_dict()
            else:
                params['reply_time'] = self.reply_time
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantshopCommentResult()
        if 'comment' in d:
            o.comment = d['comment']
        if 'comment_time' in d:
            o.comment_time = d['comment_time']
        if 'face' in d:
            o.face = d['face']
        if 'imgs' in d:
            o.imgs = d['imgs']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'reply' in d:
            o.reply = d['reply']
        if 'reply_time' in d:
            o.reply_time = d['reply_time']
        if 'score' in d:
            o.score = d['score']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


