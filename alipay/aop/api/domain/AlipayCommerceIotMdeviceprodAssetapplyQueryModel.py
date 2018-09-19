#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMdeviceprodAssetapplyQueryModel(object):

    def __init__(self):
        self._apply_order_id = None

    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_order_id:
            if hasattr(self.apply_order_id, 'to_alipay_dict'):
                params['apply_order_id'] = self.apply_order_id.to_alipay_dict()
            else:
                params['apply_order_id'] = self.apply_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMdeviceprodAssetapplyQueryModel()
        if 'apply_order_id' in d:
            o.apply_order_id = d['apply_order_id']
        return o


