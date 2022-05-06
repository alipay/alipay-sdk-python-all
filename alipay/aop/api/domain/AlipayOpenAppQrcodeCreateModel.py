#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppQrcodeCreateModel(object):

    def __init__(self):
        self._color = None
        self._describe = None
        self._query_param = None
        self._size = None
        self._url_param = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def describe(self):
        return self._describe

    @describe.setter
    def describe(self, value):
        self._describe = value
    @property
    def query_param(self):
        return self._query_param

    @query_param.setter
    def query_param(self, value):
        self._query_param = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def url_param(self):
        return self._url_param

    @url_param.setter
    def url_param(self, value):
        self._url_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.describe:
            if hasattr(self.describe, 'to_alipay_dict'):
                params['describe'] = self.describe.to_alipay_dict()
            else:
                params['describe'] = self.describe
        if self.query_param:
            if hasattr(self.query_param, 'to_alipay_dict'):
                params['query_param'] = self.query_param.to_alipay_dict()
            else:
                params['query_param'] = self.query_param
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.url_param:
            if hasattr(self.url_param, 'to_alipay_dict'):
                params['url_param'] = self.url_param.to_alipay_dict()
            else:
                params['url_param'] = self.url_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppQrcodeCreateModel()
        if 'color' in d:
            o.color = d['color']
        if 'describe' in d:
            o.describe = d['describe']
        if 'query_param' in d:
            o.query_param = d['query_param']
        if 'size' in d:
            o.size = d['size']
        if 'url_param' in d:
            o.url_param = d['url_param']
        return o


