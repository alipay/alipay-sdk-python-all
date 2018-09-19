#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiShopMallAuditQueryModel(object):

    def __init__(self):
        self._order_flow_id = None

    @property
    def order_flow_id(self):
        return self._order_flow_id

    @order_flow_id.setter
    def order_flow_id(self, value):
        self._order_flow_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_flow_id:
            if hasattr(self.order_flow_id, 'to_alipay_dict'):
                params['order_flow_id'] = self.order_flow_id.to_alipay_dict()
            else:
                params['order_flow_id'] = self.order_flow_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiShopMallAuditQueryModel()
        if 'order_flow_id' in d:
            o.order_flow_id = d['order_flow_id']
        return o


