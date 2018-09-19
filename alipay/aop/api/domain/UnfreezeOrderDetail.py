#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnfreezeOrderDetail(object):

    def __init__(self):
        self._alipay_order_no = None
        self._create_time = None
        self._memo = None
        self._merchant_order_no = None
        self._modified_time = None
        self._order_amount = None
        self._order_status = None
        self._unfreeze_amount = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def unfreeze_amount(self):
        return self._unfreeze_amount

    @unfreeze_amount.setter
    def unfreeze_amount(self, value):
        self._unfreeze_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.unfreeze_amount:
            if hasattr(self.unfreeze_amount, 'to_alipay_dict'):
                params['unfreeze_amount'] = self.unfreeze_amount.to_alipay_dict()
            else:
                params['unfreeze_amount'] = self.unfreeze_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnfreezeOrderDetail()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'unfreeze_amount' in d:
            o.unfreeze_amount = d['unfreeze_amount']
        return o


