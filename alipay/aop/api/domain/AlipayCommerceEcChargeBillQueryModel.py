#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcChargeBillQueryModel(object):

    def __init__(self):
        self._bill_no = None
        self._enterprise_id = None
        self._pay_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def pay_no(self):
        return self._pay_no

    @pay_no.setter
    def pay_no(self, value):
        self._pay_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.pay_no:
            if hasattr(self.pay_no, 'to_alipay_dict'):
                params['pay_no'] = self.pay_no.to_alipay_dict()
            else:
                params['pay_no'] = self.pay_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcChargeBillQueryModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'pay_no' in d:
            o.pay_no = d['pay_no']
        return o


