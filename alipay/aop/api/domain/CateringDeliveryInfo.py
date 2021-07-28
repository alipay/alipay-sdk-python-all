#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CateringDeliveryInfo(object):

    def __init__(self):
        self._delivery_distance = None
        self._delivery_mobile = None
        self._distributor = None
        self._estimate_delivery_end_time = None
        self._estimate_delivery_start_time = None

    @property
    def delivery_distance(self):
        return self._delivery_distance

    @delivery_distance.setter
    def delivery_distance(self, value):
        self._delivery_distance = value
    @property
    def delivery_mobile(self):
        return self._delivery_mobile

    @delivery_mobile.setter
    def delivery_mobile(self, value):
        self._delivery_mobile = value
    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        self._distributor = value
    @property
    def estimate_delivery_end_time(self):
        return self._estimate_delivery_end_time

    @estimate_delivery_end_time.setter
    def estimate_delivery_end_time(self, value):
        self._estimate_delivery_end_time = value
    @property
    def estimate_delivery_start_time(self):
        return self._estimate_delivery_start_time

    @estimate_delivery_start_time.setter
    def estimate_delivery_start_time(self, value):
        self._estimate_delivery_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_distance:
            if hasattr(self.delivery_distance, 'to_alipay_dict'):
                params['delivery_distance'] = self.delivery_distance.to_alipay_dict()
            else:
                params['delivery_distance'] = self.delivery_distance
        if self.delivery_mobile:
            if hasattr(self.delivery_mobile, 'to_alipay_dict'):
                params['delivery_mobile'] = self.delivery_mobile.to_alipay_dict()
            else:
                params['delivery_mobile'] = self.delivery_mobile
        if self.distributor:
            if hasattr(self.distributor, 'to_alipay_dict'):
                params['distributor'] = self.distributor.to_alipay_dict()
            else:
                params['distributor'] = self.distributor
        if self.estimate_delivery_end_time:
            if hasattr(self.estimate_delivery_end_time, 'to_alipay_dict'):
                params['estimate_delivery_end_time'] = self.estimate_delivery_end_time.to_alipay_dict()
            else:
                params['estimate_delivery_end_time'] = self.estimate_delivery_end_time
        if self.estimate_delivery_start_time:
            if hasattr(self.estimate_delivery_start_time, 'to_alipay_dict'):
                params['estimate_delivery_start_time'] = self.estimate_delivery_start_time.to_alipay_dict()
            else:
                params['estimate_delivery_start_time'] = self.estimate_delivery_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CateringDeliveryInfo()
        if 'delivery_distance' in d:
            o.delivery_distance = d['delivery_distance']
        if 'delivery_mobile' in d:
            o.delivery_mobile = d['delivery_mobile']
        if 'distributor' in d:
            o.distributor = d['distributor']
        if 'estimate_delivery_end_time' in d:
            o.estimate_delivery_end_time = d['estimate_delivery_end_time']
        if 'estimate_delivery_start_time' in d:
            o.estimate_delivery_start_time = d['estimate_delivery_start_time']
        return o


