#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeTicketTicketcodeCheckavailableModel(object):

    def __init__(self):
        self._order_no = None
        self._quantity = None
        self._request_id = None
        self._send_order_no = None
        self._send_token = None
        self._shop_id = None
        self._ticket_code = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
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
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        self._ticket_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
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
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.ticket_code:
            if hasattr(self.ticket_code, 'to_alipay_dict'):
                params['ticket_code'] = self.ticket_code.to_alipay_dict()
            else:
                params['ticket_code'] = self.ticket_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeTicketTicketcodeCheckavailableModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'send_order_no' in d:
            o.send_order_no = d['send_order_no']
        if 'send_token' in d:
            o.send_token = d['send_token']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'ticket_code' in d:
            o.ticket_code = d['ticket_code']
        return o


