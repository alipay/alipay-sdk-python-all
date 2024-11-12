#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DamagesInfo(object):

    def __init__(self):
        self._create_time = None
        self._damages_cash = None
        self._damages_issue_type = None
        self._damages_rate = None
        self._damages_status = None
        self._damages_type = None
        self._deduction_order_id = None
        self._payment_no = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def damages_cash(self):
        return self._damages_cash

    @damages_cash.setter
    def damages_cash(self, value):
        self._damages_cash = value
    @property
    def damages_issue_type(self):
        return self._damages_issue_type

    @damages_issue_type.setter
    def damages_issue_type(self, value):
        self._damages_issue_type = value
    @property
    def damages_rate(self):
        return self._damages_rate

    @damages_rate.setter
    def damages_rate(self, value):
        self._damages_rate = value
    @property
    def damages_status(self):
        return self._damages_status

    @damages_status.setter
    def damages_status(self, value):
        self._damages_status = value
    @property
    def damages_type(self):
        return self._damages_type

    @damages_type.setter
    def damages_type(self, value):
        self._damages_type = value
    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value
    @property
    def payment_no(self):
        return self._payment_no

    @payment_no.setter
    def payment_no(self, value):
        self._payment_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.damages_cash:
            if hasattr(self.damages_cash, 'to_alipay_dict'):
                params['damages_cash'] = self.damages_cash.to_alipay_dict()
            else:
                params['damages_cash'] = self.damages_cash
        if self.damages_issue_type:
            if hasattr(self.damages_issue_type, 'to_alipay_dict'):
                params['damages_issue_type'] = self.damages_issue_type.to_alipay_dict()
            else:
                params['damages_issue_type'] = self.damages_issue_type
        if self.damages_rate:
            if hasattr(self.damages_rate, 'to_alipay_dict'):
                params['damages_rate'] = self.damages_rate.to_alipay_dict()
            else:
                params['damages_rate'] = self.damages_rate
        if self.damages_status:
            if hasattr(self.damages_status, 'to_alipay_dict'):
                params['damages_status'] = self.damages_status.to_alipay_dict()
            else:
                params['damages_status'] = self.damages_status
        if self.damages_type:
            if hasattr(self.damages_type, 'to_alipay_dict'):
                params['damages_type'] = self.damages_type.to_alipay_dict()
            else:
                params['damages_type'] = self.damages_type
        if self.deduction_order_id:
            if hasattr(self.deduction_order_id, 'to_alipay_dict'):
                params['deduction_order_id'] = self.deduction_order_id.to_alipay_dict()
            else:
                params['deduction_order_id'] = self.deduction_order_id
        if self.payment_no:
            if hasattr(self.payment_no, 'to_alipay_dict'):
                params['payment_no'] = self.payment_no.to_alipay_dict()
            else:
                params['payment_no'] = self.payment_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DamagesInfo()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'damages_cash' in d:
            o.damages_cash = d['damages_cash']
        if 'damages_issue_type' in d:
            o.damages_issue_type = d['damages_issue_type']
        if 'damages_rate' in d:
            o.damages_rate = d['damages_rate']
        if 'damages_status' in d:
            o.damages_status = d['damages_status']
        if 'damages_type' in d:
            o.damages_type = d['damages_type']
        if 'deduction_order_id' in d:
            o.deduction_order_id = d['deduction_order_id']
        if 'payment_no' in d:
            o.payment_no = d['payment_no']
        return o


