#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchAbilityOrderData import SearchAbilityOrderData


class AbilityPageQueryDTO(object):

    def __init__(self):
        self._page_data = None
        self._page_num = None
        self._page_size = None
        self._total_number = None

    @property
    def page_data(self):
        return self._page_data

    @page_data.setter
    def page_data(self, value):
        if isinstance(value, list):
            self._page_data = list()
            for i in value:
                if isinstance(i, SearchAbilityOrderData):
                    self._page_data.append(i)
                else:
                    self._page_data.append(SearchAbilityOrderData.from_alipay_dict(i))
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
    def total_number(self):
        return self._total_number

    @total_number.setter
    def total_number(self, value):
        self._total_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_data:
            if isinstance(self.page_data, list):
                for i in range(0, len(self.page_data)):
                    element = self.page_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.page_data[i] = element.to_alipay_dict()
            if hasattr(self.page_data, 'to_alipay_dict'):
                params['page_data'] = self.page_data.to_alipay_dict()
            else:
                params['page_data'] = self.page_data
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
        if self.total_number:
            if hasattr(self.total_number, 'to_alipay_dict'):
                params['total_number'] = self.total_number.to_alipay_dict()
            else:
                params['total_number'] = self.total_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AbilityPageQueryDTO()
        if 'page_data' in d:
            o.page_data = d['page_data']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'total_number' in d:
            o.total_number = d['total_number']
        return o


