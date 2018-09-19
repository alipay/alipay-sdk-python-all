#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitInfoDetail(object):

    def __init__(self):
        self._amount = None
        self._benefit_type = None
        self._count = None
        self._description = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitInfoDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'count' in d:
            o.count = d['count']
        if 'description' in d:
            o.description = d['description']
        return o


