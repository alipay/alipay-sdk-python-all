#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenServicemarketOrderAcceptModel(object):

    def __init__(self):
        self._commodity_order_id = None

    @property
    def commodity_order_id(self):
        return self._commodity_order_id

    @commodity_order_id.setter
    def commodity_order_id(self, value):
        self._commodity_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_order_id:
            if hasattr(self.commodity_order_id, 'to_alipay_dict'):
                params['commodity_order_id'] = self.commodity_order_id.to_alipay_dict()
            else:
                params['commodity_order_id'] = self.commodity_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketOrderAcceptModel()
        if 'commodity_order_id' in d:
            o.commodity_order_id = d['commodity_order_id']
        return o


