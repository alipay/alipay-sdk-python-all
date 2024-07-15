#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateVersionDTO import TemplateVersionDTO


class PageDTO(object):

    def __init__(self):
        self._data = None
        self._page = None
        self._size = None
        self._total = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, TemplateVersionDTO):
                    self._data.append(i)
                else:
                    self._data.append(TemplateVersionDTO.from_alipay_dict(i))
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if isinstance(self.data, list):
                for i in range(0, len(self.data)):
                    element = self.data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data[i] = element.to_alipay_dict()
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
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
        o = PageDTO()
        if 'data' in d:
            o.data = d['data']
        if 'page' in d:
            o.page = d['page']
        if 'size' in d:
            o.size = d['size']
        if 'total' in d:
            o.total = d['total']
        return o


