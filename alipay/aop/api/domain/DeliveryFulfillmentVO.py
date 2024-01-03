#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryFulfillmentVO(object):

    def __init__(self):
        self._delivery_frequency = None
        self._total_delivery_times = None
        self._unit = None

    @property
    def delivery_frequency(self):
        return self._delivery_frequency

    @delivery_frequency.setter
    def delivery_frequency(self, value):
        self._delivery_frequency = value
    @property
    def total_delivery_times(self):
        return self._total_delivery_times

    @total_delivery_times.setter
    def total_delivery_times(self, value):
        self._total_delivery_times = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_frequency:
            if hasattr(self.delivery_frequency, 'to_alipay_dict'):
                params['delivery_frequency'] = self.delivery_frequency.to_alipay_dict()
            else:
                params['delivery_frequency'] = self.delivery_frequency
        if self.total_delivery_times:
            if hasattr(self.total_delivery_times, 'to_alipay_dict'):
                params['total_delivery_times'] = self.total_delivery_times.to_alipay_dict()
            else:
                params['total_delivery_times'] = self.total_delivery_times
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryFulfillmentVO()
        if 'delivery_frequency' in d:
            o.delivery_frequency = d['delivery_frequency']
        if 'total_delivery_times' in d:
            o.total_delivery_times = d['total_delivery_times']
        if 'unit' in d:
            o.unit = d['unit']
        return o


