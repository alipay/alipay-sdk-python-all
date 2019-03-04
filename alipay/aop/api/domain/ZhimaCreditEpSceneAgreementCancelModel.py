#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpSceneAgreementCancelModel(object):

    def __init__(self):
        self._biz_time = None
        self._credit_order_no = None
        self._out_order_no = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def credit_order_no(self):
        return self._credit_order_no

    @credit_order_no.setter
    def credit_order_no(self, value):
        self._credit_order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.credit_order_no:
            if hasattr(self.credit_order_no, 'to_alipay_dict'):
                params['credit_order_no'] = self.credit_order_no.to_alipay_dict()
            else:
                params['credit_order_no'] = self.credit_order_no
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
        o = ZhimaCreditEpSceneAgreementCancelModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'credit_order_no' in d:
            o.credit_order_no = d['credit_order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


