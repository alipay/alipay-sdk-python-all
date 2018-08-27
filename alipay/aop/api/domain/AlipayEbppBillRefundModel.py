#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppBillRefundModel(object):

    def __init__(self):
        self._alipay_bill_no = None
        self._extend_field = None
        self._memo = None
        self._out_order_no = None
        self._refund_amount = None
        self._refund_from = None
        self._scene = None

    @property
    def alipay_bill_no(self):
        return self._alipay_bill_no

    @alipay_bill_no.setter
    def alipay_bill_no(self, value):
        self._alipay_bill_no = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_from(self):
        return self._refund_from

    @refund_from.setter
    def refund_from(self, value):
        self._refund_from = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_bill_no:
            if hasattr(self.alipay_bill_no, 'to_alipay_dict'):
                params['alipay_bill_no'] = self.alipay_bill_no.to_alipay_dict()
            else:
                params['alipay_bill_no'] = self.alipay_bill_no
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_from:
            if hasattr(self.refund_from, 'to_alipay_dict'):
                params['refund_from'] = self.refund_from.to_alipay_dict()
            else:
                params['refund_from'] = self.refund_from
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppBillRefundModel()
        if 'alipay_bill_no' in d:
            o.alipay_bill_no = d['alipay_bill_no']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_from' in d:
            o.refund_from = d['refund_from']
        if 'scene' in d:
            o.scene = d['scene']
        return o


