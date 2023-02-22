#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsIsvdataQueryModel(object):

    def __init__(self):
        self._condition_id = None
        self._condition_type = None
        self._page_num = None
        self._page_size = None
        self._query_type = None

    @property
    def condition_id(self):
        return self._condition_id

    @condition_id.setter
    def condition_id(self, value):
        self._condition_id = value
    @property
    def condition_type(self):
        return self._condition_type

    @condition_type.setter
    def condition_type(self, value):
        self._condition_type = value
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
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_id:
            if hasattr(self.condition_id, 'to_alipay_dict'):
                params['condition_id'] = self.condition_id.to_alipay_dict()
            else:
                params['condition_id'] = self.condition_id
        if self.condition_type:
            if hasattr(self.condition_type, 'to_alipay_dict'):
                params['condition_type'] = self.condition_type.to_alipay_dict()
            else:
                params['condition_type'] = self.condition_type
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
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsIsvdataQueryModel()
        if 'condition_id' in d:
            o.condition_id = d['condition_id']
        if 'condition_type' in d:
            o.condition_type = d['condition_type']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_type' in d:
            o.query_type = d['query_type']
        return o


