#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServicepackageRefundInfo(object):

    def __init__(self):
        self._operator_role = None
        self._refund_amount = None
        self._refund_status = None

    @property
    def operator_role(self):
        return self._operator_role

    @operator_role.setter
    def operator_role(self, value):
        self._operator_role = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator_role:
            if hasattr(self.operator_role, 'to_alipay_dict'):
                params['operator_role'] = self.operator_role.to_alipay_dict()
            else:
                params['operator_role'] = self.operator_role
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServicepackageRefundInfo()
        if 'operator_role' in d:
            o.operator_role = d['operator_role']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        return o


