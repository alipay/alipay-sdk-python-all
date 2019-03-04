#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundDescriptionDTO(object):

    def __init__(self):
        self._buyer_amount = None
        self._fail_code = None
        self._kb_order_discount = None
        self._online_payment_no = None
        self._payable_amount = None
        self._payment_id = None
        self._payment_method = None
        self._refund_status = None
        self._seller_amount = None

    @property
    def buyer_amount(self):
        return self._buyer_amount

    @buyer_amount.setter
    def buyer_amount(self, value):
        self._buyer_amount = value
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def kb_order_discount(self):
        return self._kb_order_discount

    @kb_order_discount.setter
    def kb_order_discount(self, value):
        self._kb_order_discount = value
    @property
    def online_payment_no(self):
        return self._online_payment_no

    @online_payment_no.setter
    def online_payment_no(self, value):
        self._online_payment_no = value
    @property
    def payable_amount(self):
        return self._payable_amount

    @payable_amount.setter
    def payable_amount(self, value):
        self._payable_amount = value
    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def seller_amount(self):
        return self._seller_amount

    @seller_amount.setter
    def seller_amount(self, value):
        self._seller_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_amount:
            if hasattr(self.buyer_amount, 'to_alipay_dict'):
                params['buyer_amount'] = self.buyer_amount.to_alipay_dict()
            else:
                params['buyer_amount'] = self.buyer_amount
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.kb_order_discount:
            if hasattr(self.kb_order_discount, 'to_alipay_dict'):
                params['kb_order_discount'] = self.kb_order_discount.to_alipay_dict()
            else:
                params['kb_order_discount'] = self.kb_order_discount
        if self.online_payment_no:
            if hasattr(self.online_payment_no, 'to_alipay_dict'):
                params['online_payment_no'] = self.online_payment_no.to_alipay_dict()
            else:
                params['online_payment_no'] = self.online_payment_no
        if self.payable_amount:
            if hasattr(self.payable_amount, 'to_alipay_dict'):
                params['payable_amount'] = self.payable_amount.to_alipay_dict()
            else:
                params['payable_amount'] = self.payable_amount
        if self.payment_id:
            if hasattr(self.payment_id, 'to_alipay_dict'):
                params['payment_id'] = self.payment_id.to_alipay_dict()
            else:
                params['payment_id'] = self.payment_id
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.seller_amount:
            if hasattr(self.seller_amount, 'to_alipay_dict'):
                params['seller_amount'] = self.seller_amount.to_alipay_dict()
            else:
                params['seller_amount'] = self.seller_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundDescriptionDTO()
        if 'buyer_amount' in d:
            o.buyer_amount = d['buyer_amount']
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'kb_order_discount' in d:
            o.kb_order_discount = d['kb_order_discount']
        if 'online_payment_no' in d:
            o.online_payment_no = d['online_payment_no']
        if 'payable_amount' in d:
            o.payable_amount = d['payable_amount']
        if 'payment_id' in d:
            o.payment_id = d['payment_id']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'seller_amount' in d:
            o.seller_amount = d['seller_amount']
        return o


