#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentRefundItemDTO import RentRefundItemDTO


class AlipayCommerceRentOrderPayRefundModel(object):

    def __init__(self):
        self._order_id = None
        self._out_request_no = None
        self._out_trade_no = None
        self._refund_amount = None
        self._refund_items = None
        self._refund_reason = None
        self._trade_no = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_items(self):
        return self._refund_items

    @refund_items.setter
    def refund_items(self, value):
        if isinstance(value, list):
            self._refund_items = list()
            for i in value:
                if isinstance(i, RentRefundItemDTO):
                    self._refund_items.append(i)
                else:
                    self._refund_items.append(RentRefundItemDTO.from_alipay_dict(i))
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_items:
            if isinstance(self.refund_items, list):
                for i in range(0, len(self.refund_items)):
                    element = self.refund_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_items[i] = element.to_alipay_dict()
            if hasattr(self.refund_items, 'to_alipay_dict'):
                params['refund_items'] = self.refund_items.to_alipay_dict()
            else:
                params['refund_items'] = self.refund_items
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderPayRefundModel()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_items' in d:
            o.refund_items = d['refund_items']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


