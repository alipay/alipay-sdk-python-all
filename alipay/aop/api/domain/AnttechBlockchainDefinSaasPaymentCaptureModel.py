#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId


class AnttechBlockchainDefinSaasPaymentCaptureModel(object):

    def __init__(self):
        self._capture_amount = None
        self._capture_currency = None
        self._out_order_id = None
        self._out_payer_id = None
        self._out_request_id = None
        self._platform_member_id = None

    @property
    def capture_amount(self):
        return self._capture_amount

    @capture_amount.setter
    def capture_amount(self, value):
        self._capture_amount = value
    @property
    def capture_currency(self):
        return self._capture_currency

    @capture_currency.setter
    def capture_currency(self, value):
        self._capture_currency = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_payer_id(self):
        return self._out_payer_id

    @out_payer_id.setter
    def out_payer_id(self, value):
        if isinstance(value, ReferenceId):
            self._out_payer_id = value
        else:
            self._out_payer_id = ReferenceId.from_alipay_dict(value)
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.capture_amount:
            if hasattr(self.capture_amount, 'to_alipay_dict'):
                params['capture_amount'] = self.capture_amount.to_alipay_dict()
            else:
                params['capture_amount'] = self.capture_amount
        if self.capture_currency:
            if hasattr(self.capture_currency, 'to_alipay_dict'):
                params['capture_currency'] = self.capture_currency.to_alipay_dict()
            else:
                params['capture_currency'] = self.capture_currency
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_payer_id:
            if hasattr(self.out_payer_id, 'to_alipay_dict'):
                params['out_payer_id'] = self.out_payer_id.to_alipay_dict()
            else:
                params['out_payer_id'] = self.out_payer_id
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        if self.platform_member_id:
            if hasattr(self.platform_member_id, 'to_alipay_dict'):
                params['platform_member_id'] = self.platform_member_id.to_alipay_dict()
            else:
                params['platform_member_id'] = self.platform_member_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinSaasPaymentCaptureModel()
        if 'capture_amount' in d:
            o.capture_amount = d['capture_amount']
        if 'capture_currency' in d:
            o.capture_currency = d['capture_currency']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_payer_id' in d:
            o.out_payer_id = d['out_payer_id']
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        return o


