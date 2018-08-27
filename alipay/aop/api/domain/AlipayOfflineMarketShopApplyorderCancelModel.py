#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineMarketShopApplyorderCancelModel(object):

    def __init__(self):
        self._memo = None
        self._op_id = None
        self._order_id = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def op_id(self):
        return self._op_id

    @op_id.setter
    def op_id(self, value):
        self._op_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.op_id:
            if hasattr(self.op_id, 'to_alipay_dict'):
                params['op_id'] = self.op_id.to_alipay_dict()
            else:
                params['op_id'] = self.op_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketShopApplyorderCancelModel()
        if 'memo' in d:
            o.memo = d['memo']
        if 'op_id' in d:
            o.op_id = d['op_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


