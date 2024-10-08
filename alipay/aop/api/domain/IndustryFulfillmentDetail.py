#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryFulfillmentDetail(object):

    def __init__(self):
        self._fulfillment_amount = None
        self._gmt_payment = None
        self._out_request_no = None

    @property
    def fulfillment_amount(self):
        return self._fulfillment_amount

    @fulfillment_amount.setter
    def fulfillment_amount(self, value):
        self._fulfillment_amount = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_amount:
            if hasattr(self.fulfillment_amount, 'to_alipay_dict'):
                params['fulfillment_amount'] = self.fulfillment_amount.to_alipay_dict()
            else:
                params['fulfillment_amount'] = self.fulfillment_amount
        if self.gmt_payment:
            if hasattr(self.gmt_payment, 'to_alipay_dict'):
                params['gmt_payment'] = self.gmt_payment.to_alipay_dict()
            else:
                params['gmt_payment'] = self.gmt_payment
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryFulfillmentDetail()
        if 'fulfillment_amount' in d:
            o.fulfillment_amount = d['fulfillment_amount']
        if 'gmt_payment' in d:
            o.gmt_payment = d['gmt_payment']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


