#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceDdQueryModel(object):

    def __init__(self):
        self._amount = None
        self._qwe = None
        self._test_openid = None
        self._total = None
        self._weight = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def qwe(self):
        return self._qwe

    @qwe.setter
    def qwe(self, value):
        if isinstance(value, list):
            self._qwe = list()
            for i in value:
                self._qwe.append(i)
    @property
    def test_openid(self):
        return self._test_openid

    @test_openid.setter
    def test_openid(self, value):
        self._test_openid = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.qwe:
            if isinstance(self.qwe, list):
                for i in range(0, len(self.qwe)):
                    element = self.qwe[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qwe[i] = element.to_alipay_dict()
            if hasattr(self.qwe, 'to_alipay_dict'):
                params['qwe'] = self.qwe.to_alipay_dict()
            else:
                params['qwe'] = self.qwe
        if self.test_openid:
            if hasattr(self.test_openid, 'to_alipay_dict'):
                params['test_openid'] = self.test_openid.to_alipay_dict()
            else:
                params['test_openid'] = self.test_openid
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDdQueryModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'qwe' in d:
            o.qwe = d['qwe']
        if 'test_openid' in d:
            o.test_openid = d['test_openid']
        if 'total' in d:
            o.total = d['total']
        if 'weight' in d:
            o.weight = d['weight']
        return o


