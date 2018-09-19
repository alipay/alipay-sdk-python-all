#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingToolFengdieSitesBatchqueryModel(object):

    def __init__(self):
        self._operator = None
        self._page_number = None
        self._page_size = None
        self._space_id = None

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
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
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
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
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolFengdieSitesBatchqueryModel()
        if 'operator' in d:
            o.operator = d['operator']
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'space_id' in d:
            o.space_id = d['space_id']
        return o


