#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinanceQuotationQuotetradeMetadataQueryModel(object):

    def __init__(self):
        self._biz_query = None
        self._biz_type = None

    @property
    def biz_query(self):
        return self._biz_query

    @biz_query.setter
    def biz_query(self, value):
        self._biz_query = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_query:
            if hasattr(self.biz_query, 'to_alipay_dict'):
                params['biz_query'] = self.biz_query.to_alipay_dict()
            else:
                params['biz_query'] = self.biz_query
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceQuotationQuotetradeMetadataQueryModel()
        if 'biz_query' in d:
            o.biz_query = d['biz_query']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        return o


