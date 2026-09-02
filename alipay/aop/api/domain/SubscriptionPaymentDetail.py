#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionBatchRefundDetail import SubscriptionBatchRefundDetail


class SubscriptionPaymentDetail(object):

    def __init__(self):
        self._gmt_occur = None
        self._order_no = None
        self._pay_status = None
        self._pay_type = None
        self._refund_details = None
        self._total_amount = None
        self._trade_no = None

    @property
    def gmt_occur(self):
        return self._gmt_occur

    @gmt_occur.setter
    def gmt_occur(self, value):
        self._gmt_occur = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def refund_details(self):
        return self._refund_details

    @refund_details.setter
    def refund_details(self, value):
        if isinstance(value, list):
            self._refund_details = list()
            for i in value:
                if isinstance(i, SubscriptionBatchRefundDetail):
                    self._refund_details.append(i)
                else:
                    self._refund_details.append(SubscriptionBatchRefundDetail.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_occur:
            if hasattr(self.gmt_occur, 'to_alipay_dict'):
                params['gmt_occur'] = self.gmt_occur.to_alipay_dict()
            else:
                params['gmt_occur'] = self.gmt_occur
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
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
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
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
        o = SubscriptionPaymentDetail()
        if 'gmt_occur' in d:
            o.gmt_occur = d['gmt_occur']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'refund_details' in d:
            o.refund_details = d['refund_details']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


