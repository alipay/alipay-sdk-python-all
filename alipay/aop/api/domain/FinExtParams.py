#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinExtParams(object):

    def __init__(self):
        self._inst_appid = None
        self._isv_code = None
        self._page_return_url = None
        self._source = None
        self._time_expire = None

    @property
    def inst_appid(self):
        return self._inst_appid

    @inst_appid.setter
    def inst_appid(self, value):
        self._inst_appid = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def page_return_url(self):
        return self._page_return_url

    @page_return_url.setter
    def page_return_url(self, value):
        self._page_return_url = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_appid:
            if hasattr(self.inst_appid, 'to_alipay_dict'):
                params['inst_appid'] = self.inst_appid.to_alipay_dict()
            else:
                params['inst_appid'] = self.inst_appid
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.page_return_url:
            if hasattr(self.page_return_url, 'to_alipay_dict'):
                params['page_return_url'] = self.page_return_url.to_alipay_dict()
            else:
                params['page_return_url'] = self.page_return_url
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinExtParams()
        if 'inst_appid' in d:
            o.inst_appid = d['inst_appid']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'page_return_url' in d:
            o.page_return_url = d['page_return_url']
        if 'source' in d:
            o.source = d['source']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        return o


