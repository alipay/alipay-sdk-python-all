#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceCaasMerchantlevelConsultModel(object):

    def __init__(self):
        self._amount = None
        self._app_name = None
        self._app_token = None
        self._biz_type = None
        self._event_code = None
        self._merchant_name = None
        self._merchant_pid = None
        self._order_count = None
        self._request_id = None
        self._uscc = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def order_count(self):
        return self._order_count

    @order_count.setter
    def order_count(self, value):
        self._order_count = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.order_count:
            if hasattr(self.order_count, 'to_alipay_dict'):
                params['order_count'] = self.order_count.to_alipay_dict()
            else:
                params['order_count'] = self.order_count
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceCaasMerchantlevelConsultModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'order_count' in d:
            o.order_count = d['order_count']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


