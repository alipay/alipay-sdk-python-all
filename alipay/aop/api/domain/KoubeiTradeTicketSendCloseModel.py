#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeTicketSendCloseModel(object):

    def __init__(self):
        self._order_no = None
        self._reason = None
        self._request_id = None
        self._send_order_no = None
        self._send_token = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def send_order_no(self):
        return self._send_order_no

    @send_order_no.setter
    def send_order_no(self, value):
        self._send_order_no = value
    @property
    def send_token(self):
        return self._send_token

    @send_token.setter
    def send_token(self, value):
        self._send_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.send_order_no:
            if hasattr(self.send_order_no, 'to_alipay_dict'):
                params['send_order_no'] = self.send_order_no.to_alipay_dict()
            else:
                params['send_order_no'] = self.send_order_no
        if self.send_token:
            if hasattr(self.send_token, 'to_alipay_dict'):
                params['send_token'] = self.send_token.to_alipay_dict()
            else:
                params['send_token'] = self.send_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeTicketSendCloseModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'reason' in d:
            o.reason = d['reason']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'send_order_no' in d:
            o.send_order_no = d['send_order_no']
        if 'send_token' in d:
            o.send_token = d['send_token']
        return o


