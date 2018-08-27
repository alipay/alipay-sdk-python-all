#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeWapMergePayModel(object):

    def __init__(self):
        self._pre_order_no = None

    @property
    def pre_order_no(self):
        return self._pre_order_no

    @pre_order_no.setter
    def pre_order_no(self, value):
        self._pre_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.pre_order_no:
            if hasattr(self.pre_order_no, 'to_alipay_dict'):
                params['pre_order_no'] = self.pre_order_no.to_alipay_dict()
            else:
                params['pre_order_no'] = self.pre_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeWapMergePayModel()
        if 'pre_order_no' in d:
            o.pre_order_no = d['pre_order_no']
        return o


