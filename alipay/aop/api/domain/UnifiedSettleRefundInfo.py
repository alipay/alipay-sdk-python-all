#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnifiedSettleRefundInfo(object):

    def __init__(self):
        self._refund_type = None

    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnifiedSettleRefundInfo()
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        return o


