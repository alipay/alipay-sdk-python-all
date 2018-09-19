#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarCarmodelBatchqueryModel(object):

    def __init__(self):
        self._brand_id = None
        self._company_id = None
        self._query_type = None
        self._serie_id = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def serie_id(self):
        return self._serie_id

    @serie_id.setter
    def serie_id(self, value):
        self._serie_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.serie_id:
            if hasattr(self.serie_id, 'to_alipay_dict'):
                params['serie_id'] = self.serie_id.to_alipay_dict()
            else:
                params['serie_id'] = self.serie_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarCarmodelBatchqueryModel()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'serie_id' in d:
            o.serie_id = d['serie_id']
        return o


