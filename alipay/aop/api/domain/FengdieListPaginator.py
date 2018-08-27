#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FengdieListPaginator(object):

    def __init__(self):
        self._page_count = None
        self._page_number = None
        self._page_size = None
        self._total = None

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        self._page_count = value
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_count:
            if hasattr(self.page_count, 'to_alipay_dict'):
                params['page_count'] = self.page_count.to_alipay_dict()
            else:
                params['page_count'] = self.page_count
        if self.page_number:
            if hasattr(self.page_number, 'to_alipay_dict'):
                params['page_number'] = self.page_number.to_alipay_dict()
            else:
                params['page_number'] = self.page_number
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieListPaginator()
        if 'page_count' in d:
            o.page_count = d['page_count']
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'total' in d:
            o.total = d['total']
        return o


