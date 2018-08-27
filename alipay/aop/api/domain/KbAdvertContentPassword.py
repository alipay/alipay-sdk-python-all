#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertContentPassword(object):

    def __init__(self):
        self._password = None
        self._share_page_url = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    @property
    def share_page_url(self):
        return self._share_page_url

    @share_page_url.setter
    def share_page_url(self, value):
        self._share_page_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        if self.share_page_url:
            if hasattr(self.share_page_url, 'to_alipay_dict'):
                params['share_page_url'] = self.share_page_url.to_alipay_dict()
            else:
                params['share_page_url'] = self.share_page_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertContentPassword()
        if 'password' in d:
            o.password = d['password']
        if 'share_page_url' in d:
            o.share_page_url = d['share_page_url']
        return o


