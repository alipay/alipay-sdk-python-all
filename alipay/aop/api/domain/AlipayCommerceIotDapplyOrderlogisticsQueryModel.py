#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDapplyOrderlogisticsQueryModel(object):

    def __init__(self):
        self._order_biz_id = None

    @property
    def order_biz_id(self):
        return self._order_biz_id

    @order_biz_id.setter
    def order_biz_id(self, value):
        self._order_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_biz_id:
            if hasattr(self.order_biz_id, 'to_alipay_dict'):
                params['order_biz_id'] = self.order_biz_id.to_alipay_dict()
            else:
                params['order_biz_id'] = self.order_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDapplyOrderlogisticsQueryModel()
        if 'order_biz_id' in d:
            o.order_biz_id = d['order_biz_id']
        return o


