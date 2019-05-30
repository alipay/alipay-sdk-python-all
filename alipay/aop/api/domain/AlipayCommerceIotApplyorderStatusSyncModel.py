#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotApplyorderStatusSyncModel(object):

    def __init__(self):
        self._apply_order_status = None
        self._asset_apply_order_id = None

    @property
    def apply_order_status(self):
        return self._apply_order_status

    @apply_order_status.setter
    def apply_order_status(self, value):
        self._apply_order_status = value
    @property
    def asset_apply_order_id(self):
        return self._asset_apply_order_id

    @asset_apply_order_id.setter
    def asset_apply_order_id(self, value):
        self._asset_apply_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_order_status:
            if hasattr(self.apply_order_status, 'to_alipay_dict'):
                params['apply_order_status'] = self.apply_order_status.to_alipay_dict()
            else:
                params['apply_order_status'] = self.apply_order_status
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
        o = AlipayCommerceIotApplyorderStatusSyncModel()
        if 'apply_order_status' in d:
            o.apply_order_status = d['apply_order_status']
        if 'asset_apply_order_id' in d:
            o.asset_apply_order_id = d['asset_apply_order_id']
        return o


