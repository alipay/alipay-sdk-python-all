#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TravelMallRequest(object):

    def __init__(self):
        self._distance = None
        self._mall_id = None

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TravelMallRequest()
        if 'distance' in d:
            o.distance = d['distance']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        return o


