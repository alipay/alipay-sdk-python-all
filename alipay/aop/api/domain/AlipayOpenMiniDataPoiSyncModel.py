#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PoiSyncData import PoiSyncData


class AlipayOpenMiniDataPoiSyncModel(object):

    def __init__(self):
        self._poi_data = None

    @property
    def poi_data(self):
        return self._poi_data

    @poi_data.setter
    def poi_data(self, value):
        if isinstance(value, PoiSyncData):
            self._poi_data = value
        else:
            self._poi_data = PoiSyncData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.poi_data:
            if hasattr(self.poi_data, 'to_alipay_dict'):
                params['poi_data'] = self.poi_data.to_alipay_dict()
            else:
                params['poi_data'] = self.poi_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniDataPoiSyncModel()
        if 'poi_data' in d:
            o.poi_data = d['poi_data']
        return o


