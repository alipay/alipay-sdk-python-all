#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditFreezeSubOrder(object):

    def __init__(self):
        self._credit_amount = None
        self._ext_info = None
        self._fulfill_cutoff_time = None
        self._goods_amount = None
        self._goods_name = None
        self._sub_out_order_no = None

    @property
    def credit_amount(self):
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, value):
        self._credit_amount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fulfill_cutoff_time(self):
        return self._fulfill_cutoff_time

    @fulfill_cutoff_time.setter
    def fulfill_cutoff_time(self, value):
        self._fulfill_cutoff_time = value
    @property
    def goods_amount(self):
        return self._goods_amount

    @goods_amount.setter
    def goods_amount(self, value):
        self._goods_amount = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def sub_out_order_no(self):
        return self._sub_out_order_no

    @sub_out_order_no.setter
    def sub_out_order_no(self, value):
        self._sub_out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_amount:
            if hasattr(self.credit_amount, 'to_alipay_dict'):
                params['credit_amount'] = self.credit_amount.to_alipay_dict()
            else:
                params['credit_amount'] = self.credit_amount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fulfill_cutoff_time:
            if hasattr(self.fulfill_cutoff_time, 'to_alipay_dict'):
                params['fulfill_cutoff_time'] = self.fulfill_cutoff_time.to_alipay_dict()
            else:
                params['fulfill_cutoff_time'] = self.fulfill_cutoff_time
        if self.goods_amount:
            if hasattr(self.goods_amount, 'to_alipay_dict'):
                params['goods_amount'] = self.goods_amount.to_alipay_dict()
            else:
                params['goods_amount'] = self.goods_amount
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.sub_out_order_no:
            if hasattr(self.sub_out_order_no, 'to_alipay_dict'):
                params['sub_out_order_no'] = self.sub_out_order_no.to_alipay_dict()
            else:
                params['sub_out_order_no'] = self.sub_out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditFreezeSubOrder()
        if 'credit_amount' in d:
            o.credit_amount = d['credit_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fulfill_cutoff_time' in d:
            o.fulfill_cutoff_time = d['fulfill_cutoff_time']
        if 'goods_amount' in d:
            o.goods_amount = d['goods_amount']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'sub_out_order_no' in d:
            o.sub_out_order_no = d['sub_out_order_no']
        return o


