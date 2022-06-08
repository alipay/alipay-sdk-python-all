#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InterTradeBillConsultOpenApiResult(object):

    def __init__(self):
        self._create_opposite_bill = None
        self._inter_trade = None
        self._opposite_ou_code = None
        self._relation_type = None
        self._self_ou_code = None

    @property
    def create_opposite_bill(self):
        return self._create_opposite_bill

    @create_opposite_bill.setter
    def create_opposite_bill(self, value):
        self._create_opposite_bill = value
    @property
    def inter_trade(self):
        return self._inter_trade

    @inter_trade.setter
    def inter_trade(self, value):
        self._inter_trade = value
    @property
    def opposite_ou_code(self):
        return self._opposite_ou_code

    @opposite_ou_code.setter
    def opposite_ou_code(self, value):
        self._opposite_ou_code = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def self_ou_code(self):
        return self._self_ou_code

    @self_ou_code.setter
    def self_ou_code(self, value):
        self._self_ou_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_opposite_bill:
            if hasattr(self.create_opposite_bill, 'to_alipay_dict'):
                params['create_opposite_bill'] = self.create_opposite_bill.to_alipay_dict()
            else:
                params['create_opposite_bill'] = self.create_opposite_bill
        if self.inter_trade:
            if hasattr(self.inter_trade, 'to_alipay_dict'):
                params['inter_trade'] = self.inter_trade.to_alipay_dict()
            else:
                params['inter_trade'] = self.inter_trade
        if self.opposite_ou_code:
            if hasattr(self.opposite_ou_code, 'to_alipay_dict'):
                params['opposite_ou_code'] = self.opposite_ou_code.to_alipay_dict()
            else:
                params['opposite_ou_code'] = self.opposite_ou_code
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.self_ou_code:
            if hasattr(self.self_ou_code, 'to_alipay_dict'):
                params['self_ou_code'] = self.self_ou_code.to_alipay_dict()
            else:
                params['self_ou_code'] = self.self_ou_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterTradeBillConsultOpenApiResult()
        if 'create_opposite_bill' in d:
            o.create_opposite_bill = d['create_opposite_bill']
        if 'inter_trade' in d:
            o.inter_trade = d['inter_trade']
        if 'opposite_ou_code' in d:
            o.opposite_ou_code = d['opposite_ou_code']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'self_ou_code' in d:
            o.self_ou_code = d['self_ou_code']
        return o


