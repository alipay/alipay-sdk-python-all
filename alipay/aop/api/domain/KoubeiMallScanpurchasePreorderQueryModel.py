#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMallScanpurchasePreorderQueryModel(object):

    def __init__(self):
        self._advance_order_id = None

    @property
    def advance_order_id(self):
        return self._advance_order_id

    @advance_order_id.setter
    def advance_order_id(self, value):
        self._advance_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_order_id:
            if hasattr(self.advance_order_id, 'to_alipay_dict'):
                params['advance_order_id'] = self.advance_order_id.to_alipay_dict()
            else:
                params['advance_order_id'] = self.advance_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMallScanpurchasePreorderQueryModel()
        if 'advance_order_id' in d:
            o.advance_order_id = d['advance_order_id']
        return o


