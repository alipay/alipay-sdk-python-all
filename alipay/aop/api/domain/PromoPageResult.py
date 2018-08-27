#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoPageResult(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._total_count = None
        self._total_pages = None

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
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.total_pages:
            if hasattr(self.total_pages, 'to_alipay_dict'):
                params['total_pages'] = self.total_pages.to_alipay_dict()
            else:
                params['total_pages'] = self.total_pages
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoPageResult()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'total_pages' in d:
            o.total_pages = d['total_pages']
        return o


