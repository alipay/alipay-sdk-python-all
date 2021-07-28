#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MorphoPaginator(object):

    def __init__(self):
        self._page_count = None
        self._page_num = None
        self._page_size = None
        self._total = None

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        self._page_count = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
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
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
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
        o = MorphoPaginator()
        if 'page_count' in d:
            o.page_count = d['page_count']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'total' in d:
            o.total = d['total']
        return o


