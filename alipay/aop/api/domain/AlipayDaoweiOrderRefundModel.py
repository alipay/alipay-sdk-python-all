#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderRefundInfo import OrderRefundInfo


class AlipayDaoweiOrderRefundModel(object):

    def __init__(self):
        self._memo = None
        self._order_no = None
        self._out_refund_id = None
        self._refund_amount = None
        self._refund_details = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_refund_id(self):
        return self._out_refund_id

    @out_refund_id.setter
    def out_refund_id(self, value):
        self._out_refund_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_details(self):
        return self._refund_details

    @refund_details.setter
    def refund_details(self, value):
        if isinstance(value, list):
            self._refund_details = list()
            for i in value:
                if isinstance(i, OrderRefundInfo):
                    self._refund_details.append(i)
                else:
                    self._refund_details.append(OrderRefundInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_refund_id:
            if hasattr(self.out_refund_id, 'to_alipay_dict'):
                params['out_refund_id'] = self.out_refund_id.to_alipay_dict()
            else:
                params['out_refund_id'] = self.out_refund_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_details:
            if isinstance(self.refund_details, list):
                for i in range(0, len(self.refund_details)):
                    element = self.refund_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_details[i] = element.to_alipay_dict()
            if hasattr(self.refund_details, 'to_alipay_dict'):
                params['refund_details'] = self.refund_details.to_alipay_dict()
            else:
                params['refund_details'] = self.refund_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDaoweiOrderRefundModel()
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_refund_id' in d:
            o.out_refund_id = d['out_refund_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_details' in d:
            o.refund_details = d['refund_details']
        return o


