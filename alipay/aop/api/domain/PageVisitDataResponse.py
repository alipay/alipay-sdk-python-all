#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PageVisitDataResponse(object):

    def __init__(self):
        self._page_pv = None
        self._page_uv = None
        self._url = None

    @property
    def page_pv(self):
        return self._page_pv

    @page_pv.setter
    def page_pv(self, value):
        self._page_pv = value
    @property
    def page_uv(self):
        return self._page_uv

    @page_uv.setter
    def page_uv(self, value):
        self._page_uv = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_pv:
            if hasattr(self.page_pv, 'to_alipay_dict'):
                params['page_pv'] = self.page_pv.to_alipay_dict()
            else:
                params['page_pv'] = self.page_pv
        if self.page_uv:
            if hasattr(self.page_uv, 'to_alipay_dict'):
                params['page_uv'] = self.page_uv.to_alipay_dict()
            else:
                params['page_uv'] = self.page_uv
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
        o = PageVisitDataResponse()
        if 'page_pv' in d:
            o.page_pv = d['page_pv']
        if 'page_uv' in d:
            o.page_uv = d['page_uv']
        if 'url' in d:
            o.url = d['url']
        return o


