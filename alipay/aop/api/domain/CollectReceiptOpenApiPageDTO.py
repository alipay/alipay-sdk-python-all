#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CollectReceiptOpenApiDTO import CollectReceiptOpenApiDTO


class CollectReceiptOpenApiPageDTO(object):

    def __init__(self):
        self._current_page = None
        self._datas = None
        self._page_size = None
        self._total_count = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def datas(self):
        return self._datas

    @datas.setter
    def datas(self, value):
        if isinstance(value, CollectReceiptOpenApiDTO):
            self._datas = value
        else:
            self._datas = CollectReceiptOpenApiDTO.from_alipay_dict(value)
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


    def to_alipay_dict(self):
        params = dict()
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.datas:
            if hasattr(self.datas, 'to_alipay_dict'):
                params['datas'] = self.datas.to_alipay_dict()
            else:
                params['datas'] = self.datas
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CollectReceiptOpenApiPageDTO()
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'datas' in d:
            o.datas = d['datas']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'total_count' in d:
            o.total_count = d['total_count']
        return o


