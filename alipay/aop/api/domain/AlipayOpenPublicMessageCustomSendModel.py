#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Article import Article
from alipay.aop.api.domain.Text import Text


class AlipayOpenPublicMessageCustomSendModel(object):

    def __init__(self):
        self._articles = None
        self._chat = None
        self._event_type = None
        self._msg_type = None
        self._text = None
        self._to_user_id = None

    @property
    def articles(self):
        return self._articles

    @articles.setter
    def articles(self, value):
        if isinstance(value, list):
            self._articles = list()
            for i in value:
                if isinstance(i, Article):
                    self._articles.append(i)
                else:
                    self._articles.append(Article.from_alipay_dict(i))
    @property
    def chat(self):
        return self._chat

    @chat.setter
    def chat(self, value):
        self._chat = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if isinstance(value, Text):
            self._text = value
        else:
            self._text = Text.from_alipay_dict(value)
    @property
    def to_user_id(self):
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, value):
        self._to_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.articles:
            if isinstance(self.articles, list):
                for i in range(0, len(self.articles)):
                    element = self.articles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.articles[i] = element.to_alipay_dict()
            if hasattr(self.articles, 'to_alipay_dict'):
                params['articles'] = self.articles.to_alipay_dict()
            else:
                params['articles'] = self.articles
        if self.chat:
            if hasattr(self.chat, 'to_alipay_dict'):
                params['chat'] = self.chat.to_alipay_dict()
            else:
                params['chat'] = self.chat
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.to_user_id:
            if hasattr(self.to_user_id, 'to_alipay_dict'):
                params['to_user_id'] = self.to_user_id.to_alipay_dict()
            else:
                params['to_user_id'] = self.to_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicMessageCustomSendModel()
        if 'articles' in d:
            o.articles = d['articles']
        if 'chat' in d:
            o.chat = d['chat']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'text' in d:
            o.text = d['text']
        if 'to_user_id' in d:
            o.to_user_id = d['to_user_id']
        return o


