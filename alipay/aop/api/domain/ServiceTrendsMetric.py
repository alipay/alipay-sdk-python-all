#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceTrendsMetric(object):

    def __init__(self):
        self._aggr_day = None
        self._data_dt = None
        self._service_pv = None
        self._service_uv = None

    @property
    def aggr_day(self):
        return self._aggr_day

    @aggr_day.setter
    def aggr_day(self, value):
        self._aggr_day = value
    @property
    def data_dt(self):
        return self._data_dt

    @data_dt.setter
    def data_dt(self, value):
        self._data_dt = value
    @property
    def service_pv(self):
        return self._service_pv

    @service_pv.setter
    def service_pv(self, value):
        self._service_pv = value
    @property
    def service_uv(self):
        return self._service_uv

    @service_uv.setter
    def service_uv(self, value):
        self._service_uv = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggr_day:
            if hasattr(self.aggr_day, 'to_alipay_dict'):
                params['aggr_day'] = self.aggr_day.to_alipay_dict()
            else:
                params['aggr_day'] = self.aggr_day
        if self.data_dt:
            if hasattr(self.data_dt, 'to_alipay_dict'):
                params['data_dt'] = self.data_dt.to_alipay_dict()
            else:
                params['data_dt'] = self.data_dt
        if self.service_pv:
            if hasattr(self.service_pv, 'to_alipay_dict'):
                params['service_pv'] = self.service_pv.to_alipay_dict()
            else:
                params['service_pv'] = self.service_pv
        if self.service_uv:
            if hasattr(self.service_uv, 'to_alipay_dict'):
                params['service_uv'] = self.service_uv.to_alipay_dict()
            else:
                params['service_uv'] = self.service_uv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceTrendsMetric()
        if 'aggr_day' in d:
            o.aggr_day = d['aggr_day']
        if 'data_dt' in d:
            o.data_dt = d['data_dt']
        if 'service_pv' in d:
            o.service_pv = d['service_pv']
        if 'service_uv' in d:
            o.service_uv = d['service_uv']
        return o


