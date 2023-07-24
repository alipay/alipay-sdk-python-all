#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppDeliveryInfoQueryModel(object):

    def __init__(self):
        self._delivery_ids = None
        self._delivery_type = None

    @property
    def delivery_ids(self):
        return self._delivery_ids

    @delivery_ids.setter
    def delivery_ids(self, value):
        if isinstance(value, list):
            self._delivery_ids = list()
            for i in value:
                self._delivery_ids.append(i)
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_ids:
            if isinstance(self.delivery_ids, list):
                for i in range(0, len(self.delivery_ids)):
                    element = self.delivery_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_ids[i] = element.to_alipay_dict()
            if hasattr(self.delivery_ids, 'to_alipay_dict'):
                params['delivery_ids'] = self.delivery_ids.to_alipay_dict()
            else:
                params['delivery_ids'] = self.delivery_ids
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppDeliveryInfoQueryModel()
        if 'delivery_ids' in d:
            o.delivery_ids = d['delivery_ids']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        return o


