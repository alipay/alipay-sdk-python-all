#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO


class StandardRefundOrderDTO(object):

    def __init__(self):
        self._finish_time = None
        self._order_status = None
        self._refund_amount = None
        self._refund_order_id = None
        self._refund_request_id = None

    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
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
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value
    @property
    def refund_request_id(self):
        return self._refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, value):
        self._refund_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_order_id:
            if hasattr(self.refund_order_id, 'to_alipay_dict'):
                params['refund_order_id'] = self.refund_order_id.to_alipay_dict()
            else:
                params['refund_order_id'] = self.refund_order_id
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
        o = StandardRefundOrderDTO()
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_order_id' in d:
            o.refund_order_id = d['refund_order_id']
        if 'refund_request_id' in d:
            o.refund_request_id = d['refund_request_id']
        return o


