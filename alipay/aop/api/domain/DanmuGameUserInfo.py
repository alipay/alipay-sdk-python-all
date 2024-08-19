#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DanmuGameUserInfo(object):

    def __init__(self):
        self._head_url = None
        self._open_id = None
        self._user_name = None

    @property
    def head_url(self):
        return self._head_url

    @head_url.setter
    def head_url(self, value):
        self._head_url = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.head_url:
            if hasattr(self.head_url, 'to_alipay_dict'):
                params['head_url'] = self.head_url.to_alipay_dict()
            else:
                params['head_url'] = self.head_url
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = DanmuGameUserInfo()
        if 'head_url' in d:
            o.head_url = d['head_url']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


