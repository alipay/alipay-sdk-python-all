#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayVoyagerPaymentsRefundQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._refund_order_id = None
        self._refund_request_id = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayVoyagerPaymentsRefundQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'refund_order_id' in d:
            o.refund_order_id = d['refund_order_id']
        if 'refund_request_id' in d:
            o.refund_request_id = d['refund_request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


