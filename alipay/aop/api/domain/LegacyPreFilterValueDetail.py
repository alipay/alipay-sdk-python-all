#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LegacyPreFilterExtraValueDetail import LegacyPreFilterExtraValueDetail
from alipay.aop.api.domain.LegacyPreFilterExtraValueDetail import LegacyPreFilterExtraValueDetail
from alipay.aop.api.domain.LegacyPreFilterExtraValueDetail import LegacyPreFilterExtraValueDetail


class LegacyPreFilterValueDetail(object):

    def __init__(self):
        self._distance = None
        self._geo_point = None
        self._value = None

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        if isinstance(value, LegacyPreFilterExtraValueDetail):
            self._distance = value
        else:
            self._distance = LegacyPreFilterExtraValueDetail.from_alipay_dict(value)
    @property
    def geo_point(self):
        return self._geo_point

    @geo_point.setter
    def geo_point(self, value):
        if isinstance(value, LegacyPreFilterExtraValueDetail):
            self._geo_point = value
        else:
            self._geo_point = LegacyPreFilterExtraValueDetail.from_alipay_dict(value)
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, LegacyPreFilterExtraValueDetail):
            self._value = value
        else:
            self._value = LegacyPreFilterExtraValueDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.geo_point:
            if hasattr(self.geo_point, 'to_alipay_dict'):
                params['geo_point'] = self.geo_point.to_alipay_dict()
            else:
                params['geo_point'] = self.geo_point
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LegacyPreFilterValueDetail()
        if 'distance' in d:
            o.distance = d['distance']
        if 'geo_point' in d:
            o.geo_point = d['geo_point']
        if 'value' in d:
            o.value = d['value']
        return o


