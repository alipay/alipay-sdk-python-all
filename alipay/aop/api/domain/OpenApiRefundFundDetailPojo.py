#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiRefundFundDetailPojo(object):

    def __init__(self):
        self._funds = None
        self._trans_in = None
        self._trans_in_type = None
        self._type = None

    @property
    def funds(self):
        return self._funds

    @funds.setter
    def funds(self, value):
        if isinstance(value, list):
            self._funds = list()
            for i in value:
                self._funds.append(i)
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def trans_in_type(self):
        return self._trans_in_type

    @trans_in_type.setter
    def trans_in_type(self, value):
        self._trans_in_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.funds:
            if isinstance(self.funds, list):
                for i in range(0, len(self.funds)):
                    element = self.funds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.funds[i] = element.to_alipay_dict()
            if hasattr(self.funds, 'to_alipay_dict'):
                params['funds'] = self.funds.to_alipay_dict()
            else:
                params['funds'] = self.funds
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.trans_in_type:
            if hasattr(self.trans_in_type, 'to_alipay_dict'):
                params['trans_in_type'] = self.trans_in_type.to_alipay_dict()
            else:
                params['trans_in_type'] = self.trans_in_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiRefundFundDetailPojo()
        if 'funds' in d:
            o.funds = d['funds']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        if 'type' in d:
            o.type = d['type']
        return o


