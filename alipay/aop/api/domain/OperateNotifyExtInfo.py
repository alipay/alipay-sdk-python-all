#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperateNotifyExtInfo(object):

    def __init__(self):
        self._receipt_advanced = None

    @property
    def receipt_advanced(self):
        return self._receipt_advanced

    @receipt_advanced.setter
    def receipt_advanced(self, value):
        self._receipt_advanced = value


    def to_alipay_dict(self):
        params = dict()
        if self.receipt_advanced:
            if hasattr(self.receipt_advanced, 'to_alipay_dict'):
                params['receipt_advanced'] = self.receipt_advanced.to_alipay_dict()
            else:
                params['receipt_advanced'] = self.receipt_advanced
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperateNotifyExtInfo()
        if 'receipt_advanced' in d:
            o.receipt_advanced = d['receipt_advanced']
        return o


