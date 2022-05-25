#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniTipsDeliveryQueryModel(object):

    def __init__(self):
        self._delivery_id = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniTipsDeliveryQueryModel()
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        return o


