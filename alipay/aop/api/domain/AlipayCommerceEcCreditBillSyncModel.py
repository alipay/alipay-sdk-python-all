#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcCreditBillSyncModel(object):

    def __init__(self):
        self._bill_date = None
        self._enterprise_id = None
        self._repayment_date = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def repayment_date(self):
        return self._repayment_date

    @repayment_date.setter
    def repayment_date(self, value):
        self._repayment_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.repayment_date:
            if hasattr(self.repayment_date, 'to_alipay_dict'):
                params['repayment_date'] = self.repayment_date.to_alipay_dict()
            else:
                params['repayment_date'] = self.repayment_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditBillSyncModel()
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'repayment_date' in d:
            o.repayment_date = d['repayment_date']
        return o


