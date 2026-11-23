#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalCustomerinfoModifyModel(object):

    def __init__(self):
        self._bd = None
        self._cid = None
        self._customer_short_name = None
        self._customer_source = None
        self._industry = None
        self._memo = None
        self._operator = None

    @property
    def bd(self):
        return self._bd

    @bd.setter
    def bd(self, value):
        self._bd = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def customer_short_name(self):
        return self._customer_short_name

    @customer_short_name.setter
    def customer_short_name(self, value):
        self._customer_short_name = value
    @property
    def customer_source(self):
        return self._customer_source

    @customer_source.setter
    def customer_source(self, value):
        self._customer_source = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd:
            if hasattr(self.bd, 'to_alipay_dict'):
                params['bd'] = self.bd.to_alipay_dict()
            else:
                params['bd'] = self.bd
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.customer_short_name:
            if hasattr(self.customer_short_name, 'to_alipay_dict'):
                params['customer_short_name'] = self.customer_short_name.to_alipay_dict()
            else:
                params['customer_short_name'] = self.customer_short_name
        if self.customer_source:
            if hasattr(self.customer_source, 'to_alipay_dict'):
                params['customer_source'] = self.customer_source.to_alipay_dict()
            else:
                params['customer_source'] = self.customer_source
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCustomerinfoModifyModel()
        if 'bd' in d:
            o.bd = d['bd']
        if 'cid' in d:
            o.cid = d['cid']
        if 'customer_short_name' in d:
            o.customer_short_name = d['customer_short_name']
        if 'customer_source' in d:
            o.customer_source = d['customer_source']
        if 'industry' in d:
            o.industry = d['industry']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        return o


