#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosOrderKey import PosOrderKey


class KoubeiCateringOrderPayCancelModel(object):

    def __init__(self):
        self._out_pay_no = None
        self._pos_order_key = None

    @property
    def out_pay_no(self):
        return self._out_pay_no

    @out_pay_no.setter
    def out_pay_no(self, value):
        self._out_pay_no = value
    @property
    def pos_order_key(self):
        return self._pos_order_key

    @pos_order_key.setter
    def pos_order_key(self, value):
        if isinstance(value, PosOrderKey):
            self._pos_order_key = value
        else:
            self._pos_order_key = PosOrderKey.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.out_pay_no:
            if hasattr(self.out_pay_no, 'to_alipay_dict'):
                params['out_pay_no'] = self.out_pay_no.to_alipay_dict()
            else:
                params['out_pay_no'] = self.out_pay_no
        if self.pos_order_key:
            if hasattr(self.pos_order_key, 'to_alipay_dict'):
                params['pos_order_key'] = self.pos_order_key.to_alipay_dict()
            else:
                params['pos_order_key'] = self.pos_order_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderPayCancelModel()
        if 'out_pay_no' in d:
            o.out_pay_no = d['out_pay_no']
        if 'pos_order_key' in d:
            o.pos_order_key = d['pos_order_key']
        return o


