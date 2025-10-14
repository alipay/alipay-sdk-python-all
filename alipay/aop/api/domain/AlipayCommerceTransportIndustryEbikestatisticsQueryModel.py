#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportIndustryEbikestatisticsQueryModel(object):

    def __init__(self):
        self._brand_id = None
        self._date_str = None
        self._page_num = None
        self._page_size = None
        self._query_type = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def date_str(self):
        return self._date_str

    @date_str.setter
    def date_str(self, value):
        self._date_str = value
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
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.date_str:
            if hasattr(self.date_str, 'to_alipay_dict'):
                params['date_str'] = self.date_str.to_alipay_dict()
            else:
                params['date_str'] = self.date_str
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
        o = AlipayCommerceTransportIndustryEbikestatisticsQueryModel()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'date_str' in d:
            o.date_str = d['date_str']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_type' in d:
            o.query_type = d['query_type']
        return o


