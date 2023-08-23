#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleOrderBaseInfo(object):

    def __init__(self):
        self._assess_amount = None
        self._estimate_result_id = None
        self._merchant_order_no = None
        self._order_create_time = None
        self._order_status = None
        self._pre_assess_amount = None

    @property
    def assess_amount(self):
        return self._assess_amount

    @assess_amount.setter
    def assess_amount(self, value):
        self._assess_amount = value
    @property
    def estimate_result_id(self):
        return self._estimate_result_id

    @estimate_result_id.setter
    def estimate_result_id(self, value):
        self._estimate_result_id = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pre_assess_amount(self):
        return self._pre_assess_amount

    @pre_assess_amount.setter
    def pre_assess_amount(self, value):
        self._pre_assess_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.assess_amount:
            if hasattr(self.assess_amount, 'to_alipay_dict'):
                params['assess_amount'] = self.assess_amount.to_alipay_dict()
            else:
                params['assess_amount'] = self.assess_amount
        if self.estimate_result_id:
            if hasattr(self.estimate_result_id, 'to_alipay_dict'):
                params['estimate_result_id'] = self.estimate_result_id.to_alipay_dict()
            else:
                params['estimate_result_id'] = self.estimate_result_id
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pre_assess_amount:
            if hasattr(self.pre_assess_amount, 'to_alipay_dict'):
                params['pre_assess_amount'] = self.pre_assess_amount.to_alipay_dict()
            else:
                params['pre_assess_amount'] = self.pre_assess_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleOrderBaseInfo()
        if 'assess_amount' in d:
            o.assess_amount = d['assess_amount']
        if 'estimate_result_id' in d:
            o.estimate_result_id = d['estimate_result_id']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pre_assess_amount' in d:
            o.pre_assess_amount = d['pre_assess_amount']
        return o


