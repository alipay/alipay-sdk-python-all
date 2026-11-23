#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JSON(object):

    def __init__(self):
        self._pages = None
        self._total_count = None

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.pages:
            if hasattr(self.pages, 'to_alipay_dict'):
                params['pages'] = self.pages.to_alipay_dict()
            else:
                params['pages'] = self.pages
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JSON()
        if 'pages' in d:
            o.pages = d['pages']
        if 'total_count' in d:
            o.total_count = d['total_count']
        return o


