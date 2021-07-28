#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelPoiQueryModel(object):

    def __init__(self):
        self._global_shop_id = None
        self._poi_id = None
        self._poi_task_sub_type = None

    @property
    def global_shop_id(self):
        return self._global_shop_id

    @global_shop_id.setter
    def global_shop_id(self, value):
        self._global_shop_id = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def poi_task_sub_type(self):
        return self._poi_task_sub_type

    @poi_task_sub_type.setter
    def poi_task_sub_type(self, value):
        self._poi_task_sub_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.global_shop_id:
            if hasattr(self.global_shop_id, 'to_alipay_dict'):
                params['global_shop_id'] = self.global_shop_id.to_alipay_dict()
            else:
                params['global_shop_id'] = self.global_shop_id
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.poi_task_sub_type:
            if hasattr(self.poi_task_sub_type, 'to_alipay_dict'):
                params['poi_task_sub_type'] = self.poi_task_sub_type.to_alipay_dict()
            else:
                params['poi_task_sub_type'] = self.poi_task_sub_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelPoiQueryModel()
        if 'global_shop_id' in d:
            o.global_shop_id = d['global_shop_id']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'poi_task_sub_type' in d:
            o.poi_task_sub_type = d['poi_task_sub_type']
        return o


