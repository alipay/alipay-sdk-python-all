#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OutOperator import OutOperator


class OutMktAccount(object):

    def __init__(self):
        self._mkt_owner_id = None
        self._mkt_owner_name = None
        self._out_operators = None
        self._payment_owner_id = None
        self._payment_owner_name = None

    @property
    def mkt_owner_id(self):
        return self._mkt_owner_id

    @mkt_owner_id.setter
    def mkt_owner_id(self, value):
        self._mkt_owner_id = value
    @property
    def mkt_owner_name(self):
        return self._mkt_owner_name

    @mkt_owner_name.setter
    def mkt_owner_name(self, value):
        self._mkt_owner_name = value
    @property
    def out_operators(self):
        return self._out_operators

    @out_operators.setter
    def out_operators(self, value):
        if isinstance(value, list):
            self._out_operators = list()
            for i in value:
                if isinstance(i, OutOperator):
                    self._out_operators.append(i)
                else:
                    self._out_operators.append(OutOperator.from_alipay_dict(i))
    @property
    def payment_owner_id(self):
        return self._payment_owner_id

    @payment_owner_id.setter
    def payment_owner_id(self, value):
        self._payment_owner_id = value
    @property
    def payment_owner_name(self):
        return self._payment_owner_name

    @payment_owner_name.setter
    def payment_owner_name(self, value):
        self._payment_owner_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.mkt_owner_id:
            if hasattr(self.mkt_owner_id, 'to_alipay_dict'):
                params['mkt_owner_id'] = self.mkt_owner_id.to_alipay_dict()
            else:
                params['mkt_owner_id'] = self.mkt_owner_id
        if self.mkt_owner_name:
            if hasattr(self.mkt_owner_name, 'to_alipay_dict'):
                params['mkt_owner_name'] = self.mkt_owner_name.to_alipay_dict()
            else:
                params['mkt_owner_name'] = self.mkt_owner_name
        if self.out_operators:
            if isinstance(self.out_operators, list):
                for i in range(0, len(self.out_operators)):
                    element = self.out_operators[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_operators[i] = element.to_alipay_dict()
            if hasattr(self.out_operators, 'to_alipay_dict'):
                params['out_operators'] = self.out_operators.to_alipay_dict()
            else:
                params['out_operators'] = self.out_operators
        if self.payment_owner_id:
            if hasattr(self.payment_owner_id, 'to_alipay_dict'):
                params['payment_owner_id'] = self.payment_owner_id.to_alipay_dict()
            else:
                params['payment_owner_id'] = self.payment_owner_id
        if self.payment_owner_name:
            if hasattr(self.payment_owner_name, 'to_alipay_dict'):
                params['payment_owner_name'] = self.payment_owner_name.to_alipay_dict()
            else:
                params['payment_owner_name'] = self.payment_owner_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutMktAccount()
        if 'mkt_owner_id' in d:
            o.mkt_owner_id = d['mkt_owner_id']
        if 'mkt_owner_name' in d:
            o.mkt_owner_name = d['mkt_owner_name']
        if 'out_operators' in d:
            o.out_operators = d['out_operators']
        if 'payment_owner_id' in d:
            o.payment_owner_id = d['payment_owner_id']
        if 'payment_owner_name' in d:
            o.payment_owner_name = d['payment_owner_name']
        return o


