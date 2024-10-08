#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantOrderPayModel(object):

    def __init__(self):
        self._order_id = None
        self._payment_biz_type = None
        self._related_payment_no = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def payment_biz_type(self):
        return self._payment_biz_type

    @payment_biz_type.setter
    def payment_biz_type(self, value):
        self._payment_biz_type = value
    @property
    def related_payment_no(self):
        return self._related_payment_no

    @related_payment_no.setter
    def related_payment_no(self, value):
        self._related_payment_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.payment_biz_type:
            if hasattr(self.payment_biz_type, 'to_alipay_dict'):
                params['payment_biz_type'] = self.payment_biz_type.to_alipay_dict()
            else:
                params['payment_biz_type'] = self.payment_biz_type
        if self.related_payment_no:
            if hasattr(self.related_payment_no, 'to_alipay_dict'):
                params['related_payment_no'] = self.related_payment_no.to_alipay_dict()
            else:
                params['related_payment_no'] = self.related_payment_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantOrderPayModel()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'payment_biz_type' in d:
            o.payment_biz_type = d['payment_biz_type']
        if 'related_payment_no' in d:
            o.related_payment_no = d['related_payment_no']
        return o


