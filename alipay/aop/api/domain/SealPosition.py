#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SealPosition(object):

    def __init__(self):
        self._keyword = None
        self._page_no = None
        self._type = None
        self._x = None
        self._y = None

    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


    def to_alipay_dict(self):
        params = dict()
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.x:
            if hasattr(self.x, 'to_alipay_dict'):
                params['x'] = self.x.to_alipay_dict()
            else:
                params['x'] = self.x
        if self.y:
            if hasattr(self.y, 'to_alipay_dict'):
                params['y'] = self.y.to_alipay_dict()
            else:
                params['y'] = self.y
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SealPosition()
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'type' in d:
            o.type = d['type']
        if 'x' in d:
            o.x = d['x']
        if 'y' in d:
            o.y = d['y']
        return o


