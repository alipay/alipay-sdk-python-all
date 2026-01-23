#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcMarketRegionQueryModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._region_position = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def region_position(self):
        return self._region_position

    @region_position.setter
    def region_position(self, value):
        self._region_position = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.region_position:
            if hasattr(self.region_position, 'to_alipay_dict'):
                params['region_position'] = self.region_position.to_alipay_dict()
            else:
                params['region_position'] = self.region_position
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcMarketRegionQueryModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'region_position' in d:
            o.region_position = d['region_position']
        return o


