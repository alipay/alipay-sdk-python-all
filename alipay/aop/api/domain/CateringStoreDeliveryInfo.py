#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CateringStoreDeliveryInfo(object):

    def __init__(self):
        self._delivery_area = None
        self._delivery_fee = None
        self._delivery_threshold = None

    @property
    def delivery_area(self):
        return self._delivery_area

    @delivery_area.setter
    def delivery_area(self, value):
        self._delivery_area = value
    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        self._delivery_fee = value
    @property
    def delivery_threshold(self):
        return self._delivery_threshold

    @delivery_threshold.setter
    def delivery_threshold(self, value):
        self._delivery_threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_area:
            if hasattr(self.delivery_area, 'to_alipay_dict'):
                params['delivery_area'] = self.delivery_area.to_alipay_dict()
            else:
                params['delivery_area'] = self.delivery_area
        if self.delivery_fee:
            if hasattr(self.delivery_fee, 'to_alipay_dict'):
                params['delivery_fee'] = self.delivery_fee.to_alipay_dict()
            else:
                params['delivery_fee'] = self.delivery_fee
        if self.delivery_threshold:
            if hasattr(self.delivery_threshold, 'to_alipay_dict'):
                params['delivery_threshold'] = self.delivery_threshold.to_alipay_dict()
            else:
                params['delivery_threshold'] = self.delivery_threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CateringStoreDeliveryInfo()
        if 'delivery_area' in d:
            o.delivery_area = d['delivery_area']
        if 'delivery_fee' in d:
            o.delivery_fee = d['delivery_fee']
        if 'delivery_threshold' in d:
            o.delivery_threshold = d['delivery_threshold']
        return o


