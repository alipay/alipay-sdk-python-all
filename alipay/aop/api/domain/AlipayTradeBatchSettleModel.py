#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleClause import SettleClause


class AlipayTradeBatchSettleModel(object):

    def __init__(self):
        self._biz_product = None
        self._extend_params = None
        self._out_request_no = None
        self._settle_clauses = None
        self._settle_type = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def settle_clauses(self):
        return self._settle_clauses

    @settle_clauses.setter
    def settle_clauses(self, value):
        if isinstance(value, list):
            self._settle_clauses = list()
            for i in value:
                if isinstance(i, SettleClause):
                    self._settle_clauses.append(i)
                else:
                    self._settle_clauses.append(SettleClause.from_alipay_dict(i))
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.settle_clauses:
            if isinstance(self.settle_clauses, list):
                for i in range(0, len(self.settle_clauses)):
                    element = self.settle_clauses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_clauses[i] = element.to_alipay_dict()
            if hasattr(self.settle_clauses, 'to_alipay_dict'):
                params['settle_clauses'] = self.settle_clauses.to_alipay_dict()
            else:
                params['settle_clauses'] = self.settle_clauses
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeBatchSettleModel()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'settle_clauses' in d:
            o.settle_clauses = d['settle_clauses']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        return o


