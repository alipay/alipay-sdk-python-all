#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrafficRule(object):

    def __init__(self):
        self._traffic_ratio = None
        self._version_name = None

    @property
    def traffic_ratio(self):
        return self._traffic_ratio

    @traffic_ratio.setter
    def traffic_ratio(self, value):
        self._traffic_ratio = value
    @property
    def version_name(self):
        return self._version_name

    @version_name.setter
    def version_name(self, value):
        self._version_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.traffic_ratio:
            if hasattr(self.traffic_ratio, 'to_alipay_dict'):
                params['traffic_ratio'] = self.traffic_ratio.to_alipay_dict()
            else:
                params['traffic_ratio'] = self.traffic_ratio
        if self.version_name:
            if hasattr(self.version_name, 'to_alipay_dict'):
                params['version_name'] = self.version_name.to_alipay_dict()
            else:
                params['version_name'] = self.version_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficRule()
        if 'traffic_ratio' in d:
            o.traffic_ratio = d['traffic_ratio']
        if 'version_name' in d:
            o.version_name = d['version_name']
        return o


