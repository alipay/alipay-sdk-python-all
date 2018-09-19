#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsCertificateApiDTO import InsCertificateApiDTO


class InsCertificatePaginationList(object):

    def __init__(self):
        self._current_page = None
        self._list = None
        self._page_size = None
        self._total_count = None
        self._total_page_num = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, InsCertificateApiDTO):
                    self._list.append(i)
                else:
                    self._list.append(InsCertificateApiDTO.from_alipay_dict(i))
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
    def total_page_num(self):
        return self._total_page_num

    @total_page_num.setter
    def total_page_num(self, value):
        self._total_page_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.list:
            if isinstance(self.list, list):
                for i in range(0, len(self.list)):
                    element = self.list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.list[i] = element.to_alipay_dict()
            if hasattr(self.list, 'to_alipay_dict'):
                params['list'] = self.list.to_alipay_dict()
            else:
                params['list'] = self.list
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
        if self.total_page_num:
            if hasattr(self.total_page_num, 'to_alipay_dict'):
                params['total_page_num'] = self.total_page_num.to_alipay_dict()
            else:
                params['total_page_num'] = self.total_page_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsCertificatePaginationList()
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'list' in d:
            o.list = d['list']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'total_page_num' in d:
            o.total_page_num = d['total_page_num']
        return o


