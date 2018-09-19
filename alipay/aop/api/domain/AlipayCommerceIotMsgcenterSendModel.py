#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMsgcenterSendModel(object):

    def __init__(self):
        self._content = None
        self._datetime = None
        self._ext_info = None
        self._is_support_link = None
        self._link = None
        self._title = None
        self._type = None
        self._user_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, value):
        self._datetime = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def is_support_link(self):
        return self._is_support_link

    @is_support_link.setter
    def is_support_link(self, value):
        self._is_support_link = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.datetime:
            if hasattr(self.datetime, 'to_alipay_dict'):
                params['datetime'] = self.datetime.to_alipay_dict()
            else:
                params['datetime'] = self.datetime
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.is_support_link:
            if hasattr(self.is_support_link, 'to_alipay_dict'):
                params['is_support_link'] = self.is_support_link.to_alipay_dict()
            else:
                params['is_support_link'] = self.is_support_link
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMsgcenterSendModel()
        if 'content' in d:
            o.content = d['content']
        if 'datetime' in d:
            o.datetime = d['datetime']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'is_support_link' in d:
            o.is_support_link = d['is_support_link']
        if 'link' in d:
            o.link = d['link']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


