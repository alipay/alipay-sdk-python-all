#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAppPageRes(object):

    def __init__(self):
        self._desc = None
        self._mini_app_id = None
        self._page_type = None
        self._url = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def page_type(self):
        return self._page_type

    @page_type.setter
    def page_type(self, value):
        self._page_type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.page_type:
            if hasattr(self.page_type, 'to_alipay_dict'):
                params['page_type'] = self.page_type.to_alipay_dict()
            else:
                params['page_type'] = self.page_type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAppPageRes()
        if 'desc' in d:
            o.desc = d['desc']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'page_type' in d:
            o.page_type = d['page_type']
        if 'url' in d:
            o.url = d['url']
        return o


