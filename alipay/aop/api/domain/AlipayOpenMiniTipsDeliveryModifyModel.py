#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniTipsDeliveryModifyModel(object):

    def __init__(self):
        self._delivery_id = None
        self._operate_type = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniTipsDeliveryModifyModel()
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


