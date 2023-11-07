#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductionOrderPageProcessorResponse(object):

    def __init__(self):
        self._card_name = None
        self._deduction_amount = None
        self._deduction_order_date = None
        self._deduction_order_id = None
        self._deduction_status = None
        self._deduction_time = None
        self._merchant_name = None
        self._open_id = None
        self._settle_status = None
        self._user_id = None

    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def deduction_order_date(self):
        return self._deduction_order_date

    @deduction_order_date.setter
    def deduction_order_date(self, value):
        self._deduction_order_date = value
    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value
    @property
    def deduction_status(self):
        return self._deduction_status

    @deduction_status.setter
    def deduction_status(self, value):
        self._deduction_status = value
    @property
    def deduction_time(self):
        return self._deduction_time

    @deduction_time.setter
    def deduction_time(self, value):
        self._deduction_time = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.deduction_order_date:
            if hasattr(self.deduction_order_date, 'to_alipay_dict'):
                params['deduction_order_date'] = self.deduction_order_date.to_alipay_dict()
            else:
                params['deduction_order_date'] = self.deduction_order_date
        if self.deduction_order_id:
            if hasattr(self.deduction_order_id, 'to_alipay_dict'):
                params['deduction_order_id'] = self.deduction_order_id.to_alipay_dict()
            else:
                params['deduction_order_id'] = self.deduction_order_id
        if self.deduction_status:
            if hasattr(self.deduction_status, 'to_alipay_dict'):
                params['deduction_status'] = self.deduction_status.to_alipay_dict()
            else:
                params['deduction_status'] = self.deduction_status
        if self.deduction_time:
            if hasattr(self.deduction_time, 'to_alipay_dict'):
                params['deduction_time'] = self.deduction_time.to_alipay_dict()
            else:
                params['deduction_time'] = self.deduction_time
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductionOrderPageProcessorResponse()
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_order_date' in d:
            o.deduction_order_date = d['deduction_order_date']
        if 'deduction_order_id' in d:
            o.deduction_order_id = d['deduction_order_id']
        if 'deduction_status' in d:
            o.deduction_status = d['deduction_status']
        if 'deduction_time' in d:
            o.deduction_time = d['deduction_time']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


