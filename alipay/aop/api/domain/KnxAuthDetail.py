#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KnxAuthDetail(object):

    def __init__(self):
        self._auth_content = None
        self._auth_name = None
        self._auth_time = None

    @property
    def auth_content(self):
        return self._auth_content

    @auth_content.setter
    def auth_content(self, value):
        self._auth_content = value
    @property
    def auth_name(self):
        return self._auth_name

    @auth_name.setter
    def auth_name(self, value):
        self._auth_name = value
    @property
    def auth_time(self):
        return self._auth_time

    @auth_time.setter
    def auth_time(self, value):
        self._auth_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_content:
            if hasattr(self.auth_content, 'to_alipay_dict'):
                params['auth_content'] = self.auth_content.to_alipay_dict()
            else:
                params['auth_content'] = self.auth_content
        if self.auth_name:
            if hasattr(self.auth_name, 'to_alipay_dict'):
                params['auth_name'] = self.auth_name.to_alipay_dict()
            else:
                params['auth_name'] = self.auth_name
        if self.auth_time:
            if hasattr(self.auth_time, 'to_alipay_dict'):
                params['auth_time'] = self.auth_time.to_alipay_dict()
            else:
                params['auth_time'] = self.auth_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KnxAuthDetail()
        if 'auth_content' in d:
            o.auth_content = d['auth_content']
        if 'auth_name' in d:
            o.auth_name = d['auth_name']
        if 'auth_time' in d:
            o.auth_time = d['auth_time']
        return o


