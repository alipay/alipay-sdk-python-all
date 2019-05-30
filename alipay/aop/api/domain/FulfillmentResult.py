#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FulfillmentResult(object):

    def __init__(self):
        self._fulfillment_order_no = None
        self._out_order_no = None

    @property
    def fulfillment_order_no(self):
        return self._fulfillment_order_no

    @fulfillment_order_no.setter
    def fulfillment_order_no(self, value):
        self._fulfillment_order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_order_no:
            if hasattr(self.fulfillment_order_no, 'to_alipay_dict'):
                params['fulfillment_order_no'] = self.fulfillment_order_no.to_alipay_dict()
            else:
                params['fulfillment_order_no'] = self.fulfillment_order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentResult()
        if 'fulfillment_order_no' in d:
            o.fulfillment_order_no = d['fulfillment_order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


