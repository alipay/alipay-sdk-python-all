#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeTicketTicketcodeSyncModel(object):

    def __init__(self):
        self._code_type = None
        self._gmt_biz = None
        self._order_no = None
        self._quantity = None
        self._request_id = None
        self._sync_shop_id = None
        self._ticket_code = None

    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def gmt_biz(self):
        return self._gmt_biz

    @gmt_biz.setter
    def gmt_biz(self, value):
        self._gmt_biz = value
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
    def sync_shop_id(self):
        return self._sync_shop_id

    @sync_shop_id.setter
    def sync_shop_id(self, value):
        self._sync_shop_id = value
    @property
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        self._ticket_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.gmt_biz:
            if hasattr(self.gmt_biz, 'to_alipay_dict'):
                params['gmt_biz'] = self.gmt_biz.to_alipay_dict()
            else:
                params['gmt_biz'] = self.gmt_biz
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
        if self.sync_shop_id:
            if hasattr(self.sync_shop_id, 'to_alipay_dict'):
                params['sync_shop_id'] = self.sync_shop_id.to_alipay_dict()
            else:
                params['sync_shop_id'] = self.sync_shop_id
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
        o = KoubeiTradeTicketTicketcodeSyncModel()
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'gmt_biz' in d:
            o.gmt_biz = d['gmt_biz']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sync_shop_id' in d:
            o.sync_shop_id = d['sync_shop_id']
        if 'ticket_code' in d:
            o.ticket_code = d['ticket_code']
        return o


