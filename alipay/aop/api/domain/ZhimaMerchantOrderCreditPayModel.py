#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantOrderCreditPayModel(object):

    def __init__(self):
        self._coupon_amount = None
        self._order_operate_type = None
        self._out_order_no = None
        self._out_trans_no = None
        self._pay_amount = None
        self._remark = None
        self._use_coupon = None
        self._zm_order_no = None

    @property
    def coupon_amount(self):
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, value):
        self._coupon_amount = value
    @property
    def order_operate_type(self):
        return self._order_operate_type

    @order_operate_type.setter
    def order_operate_type(self, value):
        self._order_operate_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_trans_no(self):
        return self._out_trans_no

    @out_trans_no.setter
    def out_trans_no(self, value):
        self._out_trans_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def use_coupon(self):
        return self._use_coupon

    @use_coupon.setter
    def use_coupon(self, value):
        self._use_coupon = value
    @property
    def zm_order_no(self):
        return self._zm_order_no

    @zm_order_no.setter
    def zm_order_no(self, value):
        self._zm_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_amount:
            if hasattr(self.coupon_amount, 'to_alipay_dict'):
                params['coupon_amount'] = self.coupon_amount.to_alipay_dict()
            else:
                params['coupon_amount'] = self.coupon_amount
        if self.order_operate_type:
            if hasattr(self.order_operate_type, 'to_alipay_dict'):
                params['order_operate_type'] = self.order_operate_type.to_alipay_dict()
            else:
                params['order_operate_type'] = self.order_operate_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_trans_no:
            if hasattr(self.out_trans_no, 'to_alipay_dict'):
                params['out_trans_no'] = self.out_trans_no.to_alipay_dict()
            else:
                params['out_trans_no'] = self.out_trans_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.use_coupon:
            if hasattr(self.use_coupon, 'to_alipay_dict'):
                params['use_coupon'] = self.use_coupon.to_alipay_dict()
            else:
                params['use_coupon'] = self.use_coupon
        if self.zm_order_no:
            if hasattr(self.zm_order_no, 'to_alipay_dict'):
                params['zm_order_no'] = self.zm_order_no.to_alipay_dict()
            else:
                params['zm_order_no'] = self.zm_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantOrderCreditPayModel()
        if 'coupon_amount' in d:
            o.coupon_amount = d['coupon_amount']
        if 'order_operate_type' in d:
            o.order_operate_type = d['order_operate_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_trans_no' in d:
            o.out_trans_no = d['out_trans_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'remark' in d:
            o.remark = d['remark']
        if 'use_coupon' in d:
            o.use_coupon = d['use_coupon']
        if 'zm_order_no' in d:
            o.zm_order_no = d['zm_order_no']
        return o


