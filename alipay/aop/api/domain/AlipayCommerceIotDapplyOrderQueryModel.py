#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDapplyOrderQueryModel(object):

    def __init__(self):
        self._asset_apply_order_id = None

    @property
    def asset_apply_order_id(self):
        return self._asset_apply_order_id

    @asset_apply_order_id.setter
    def asset_apply_order_id(self, value):
        self._asset_apply_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_apply_order_id:
            if hasattr(self.asset_apply_order_id, 'to_alipay_dict'):
                params['asset_apply_order_id'] = self.asset_apply_order_id.to_alipay_dict()
            else:
                params['asset_apply_order_id'] = self.asset_apply_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDapplyOrderQueryModel()
        if 'asset_apply_order_id' in d:
            o.asset_apply_order_id = d['asset_apply_order_id']
        return o


