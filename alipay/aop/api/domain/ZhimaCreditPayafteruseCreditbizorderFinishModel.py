#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPayafteruseCreditbizorderFinishModel(object):

    def __init__(self):
        self._credit_biz_order_id = None
        self._is_fulfilled = None
        self._out_request_no = None
        self._remark = None

    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def is_fulfilled(self):
        return self._is_fulfilled

    @is_fulfilled.setter
    def is_fulfilled(self, value):
        self._is_fulfilled = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_biz_order_id:
            if hasattr(self.credit_biz_order_id, 'to_alipay_dict'):
                params['credit_biz_order_id'] = self.credit_biz_order_id.to_alipay_dict()
            else:
                params['credit_biz_order_id'] = self.credit_biz_order_id
        if self.is_fulfilled:
            if hasattr(self.is_fulfilled, 'to_alipay_dict'):
                params['is_fulfilled'] = self.is_fulfilled.to_alipay_dict()
            else:
                params['is_fulfilled'] = self.is_fulfilled
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPayafteruseCreditbizorderFinishModel()
        if 'credit_biz_order_id' in d:
            o.credit_biz_order_id = d['credit_biz_order_id']
        if 'is_fulfilled' in d:
            o.is_fulfilled = d['is_fulfilled']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'remark' in d:
            o.remark = d['remark']
        return o


