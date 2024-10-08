#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockTrafficQueryModel(object):

    def __init__(self):
        self._inst_id = None
        self._traffic_code = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def traffic_code(self):
        return self._traffic_code

    @traffic_code.setter
    def traffic_code(self, value):
        self._traffic_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.traffic_code:
            if hasattr(self.traffic_code, 'to_alipay_dict'):
                params['traffic_code'] = self.traffic_code.to_alipay_dict()
            else:
                params['traffic_code'] = self.traffic_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockTrafficQueryModel()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'traffic_code' in d:
            o.traffic_code = d['traffic_code']
        return o


