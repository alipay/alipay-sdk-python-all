#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayInfoBean(object):

    def __init__(self):
        self._end_time = None
        self._mer_name = None
        self._out_order_id = None
        self._out_trans_id = None
        self._pay_amt = None
        self._thirdpay_mer_id = None
        self._thirdpay_org = None
        self._trans_amt = None
        self._trans_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def mer_name(self):
        return self._mer_name

    @mer_name.setter
    def mer_name(self, value):
        self._mer_name = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_trans_id(self):
        return self._out_trans_id

    @out_trans_id.setter
    def out_trans_id(self, value):
        self._out_trans_id = value
    @property
    def pay_amt(self):
        return self._pay_amt

    @pay_amt.setter
    def pay_amt(self, value):
        self._pay_amt = value
    @property
    def thirdpay_mer_id(self):
        return self._thirdpay_mer_id

    @thirdpay_mer_id.setter
    def thirdpay_mer_id(self, value):
        self._thirdpay_mer_id = value
    @property
    def thirdpay_org(self):
        return self._thirdpay_org

    @thirdpay_org.setter
    def thirdpay_org(self, value):
        self._thirdpay_org = value
    @property
    def trans_amt(self):
        return self._trans_amt

    @trans_amt.setter
    def trans_amt(self, value):
        self._trans_amt = value
    @property
    def trans_time(self):
        return self._trans_time

    @trans_time.setter
    def trans_time(self, value):
        self._trans_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.mer_name:
            if hasattr(self.mer_name, 'to_alipay_dict'):
                params['mer_name'] = self.mer_name.to_alipay_dict()
            else:
                params['mer_name'] = self.mer_name
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_trans_id:
            if hasattr(self.out_trans_id, 'to_alipay_dict'):
                params['out_trans_id'] = self.out_trans_id.to_alipay_dict()
            else:
                params['out_trans_id'] = self.out_trans_id
        if self.pay_amt:
            if hasattr(self.pay_amt, 'to_alipay_dict'):
                params['pay_amt'] = self.pay_amt.to_alipay_dict()
            else:
                params['pay_amt'] = self.pay_amt
        if self.thirdpay_mer_id:
            if hasattr(self.thirdpay_mer_id, 'to_alipay_dict'):
                params['thirdpay_mer_id'] = self.thirdpay_mer_id.to_alipay_dict()
            else:
                params['thirdpay_mer_id'] = self.thirdpay_mer_id
        if self.thirdpay_org:
            if hasattr(self.thirdpay_org, 'to_alipay_dict'):
                params['thirdpay_org'] = self.thirdpay_org.to_alipay_dict()
            else:
                params['thirdpay_org'] = self.thirdpay_org
        if self.trans_amt:
            if hasattr(self.trans_amt, 'to_alipay_dict'):
                params['trans_amt'] = self.trans_amt.to_alipay_dict()
            else:
                params['trans_amt'] = self.trans_amt
        if self.trans_time:
            if hasattr(self.trans_time, 'to_alipay_dict'):
                params['trans_time'] = self.trans_time.to_alipay_dict()
            else:
                params['trans_time'] = self.trans_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayInfoBean()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'mer_name' in d:
            o.mer_name = d['mer_name']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_trans_id' in d:
            o.out_trans_id = d['out_trans_id']
        if 'pay_amt' in d:
            o.pay_amt = d['pay_amt']
        if 'thirdpay_mer_id' in d:
            o.thirdpay_mer_id = d['thirdpay_mer_id']
        if 'thirdpay_org' in d:
            o.thirdpay_org = d['thirdpay_org']
        if 'trans_amt' in d:
            o.trans_amt = d['trans_amt']
        if 'trans_time' in d:
            o.trans_time = d['trans_time']
        return o


