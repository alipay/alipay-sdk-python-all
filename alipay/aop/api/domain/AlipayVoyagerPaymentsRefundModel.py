#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO


class AlipayVoyagerPaymentsRefundModel(object):

    def __init__(self):
        self._pay_order_id = None
        self._refund_amount = None
        self._refund_notify_url = None
        self._refund_reason = None
        self._refund_request_id = None

    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._refund_amount = value
        else:
            self._refund_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def refund_notify_url(self):
        return self._refund_notify_url

    @refund_notify_url.setter
    def refund_notify_url(self, value):
        self._refund_notify_url = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_request_id(self):
        return self._refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self._refund_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_notify_url:
            if hasattr(self.refund_notify_url, 'to_alipay_dict'):
                params['refund_notify_url'] = self.refund_notify_url.to_alipay_dict()
            else:
                params['refund_notify_url'] = self.refund_notify_url
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_request_id:
            if hasattr(self.refund_request_id, 'to_alipay_dict'):
                params['refund_request_id'] = self.refund_request_id.to_alipay_dict()
            else:
                params['refund_request_id'] = self.refund_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayVoyagerPaymentsRefundModel()
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_notify_url' in d:
            o.refund_notify_url = d['refund_notify_url']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_request_id' in d:
            o.refund_request_id = d['refund_request_id']
        return o


