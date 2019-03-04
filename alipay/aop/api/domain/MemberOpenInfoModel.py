#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberOpenInfoModel(object):

    def __init__(self):
        self._open_url = None
        self._wechat_open_url = None

    @property
    def open_url(self):
        return self._open_url

    @open_url.setter
    def open_url(self, value):
        self._open_url = value
    @property
    def wechat_open_url(self):
        return self._wechat_open_url

    @wechat_open_url.setter
    def wechat_open_url(self, value):
        self._wechat_open_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_url:
            if hasattr(self.open_url, 'to_alipay_dict'):
                params['open_url'] = self.open_url.to_alipay_dict()
            else:
                params['open_url'] = self.open_url
        if self.wechat_open_url:
            if hasattr(self.wechat_open_url, 'to_alipay_dict'):
                params['wechat_open_url'] = self.wechat_open_url.to_alipay_dict()
            else:
                params['wechat_open_url'] = self.wechat_open_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberOpenInfoModel()
        if 'open_url' in d:
            o.open_url = d['open_url']
        if 'wechat_open_url' in d:
            o.wechat_open_url = d['wechat_open_url']
        return o


