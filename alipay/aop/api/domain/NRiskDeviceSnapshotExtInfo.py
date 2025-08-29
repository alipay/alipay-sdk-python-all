#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NRiskDeviceSnapshotExtInfo(object):

    def __init__(self):
        self._bind_out_poi_id = None
        self._bind_out_poi_name = None

    @property
    def bind_out_poi_id(self):
        return self._bind_out_poi_id

    @bind_out_poi_id.setter
    def bind_out_poi_id(self, value):
        self._bind_out_poi_id = value
    @property
    def bind_out_poi_name(self):
        return self._bind_out_poi_name

    @bind_out_poi_name.setter
    def bind_out_poi_name(self, value):
        self._bind_out_poi_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_out_poi_id:
            if hasattr(self.bind_out_poi_id, 'to_alipay_dict'):
                params['bind_out_poi_id'] = self.bind_out_poi_id.to_alipay_dict()
            else:
                params['bind_out_poi_id'] = self.bind_out_poi_id
        if self.bind_out_poi_name:
            if hasattr(self.bind_out_poi_name, 'to_alipay_dict'):
                params['bind_out_poi_name'] = self.bind_out_poi_name.to_alipay_dict()
            else:
                params['bind_out_poi_name'] = self.bind_out_poi_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NRiskDeviceSnapshotExtInfo()
        if 'bind_out_poi_id' in d:
            o.bind_out_poi_id = d['bind_out_poi_id']
        if 'bind_out_poi_name' in d:
            o.bind_out_poi_name = d['bind_out_poi_name']
        return o


