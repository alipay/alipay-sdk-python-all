#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalOrgbidataBlockinfoQueryModel(object):

    def __init__(self):
        self._aggr_day = None
        self._block_type = None
        self._data_dt = None
        self._scc = None

    @property
    def aggr_day(self):
        return self._aggr_day

    @aggr_day.setter
    def aggr_day(self, value):
        self._aggr_day = value
    @property
    def block_type(self):
        return self._block_type

    @block_type.setter
    def block_type(self, value):
        self._block_type = value
    @property
    def data_dt(self):
        return self._data_dt

    @data_dt.setter
    def data_dt(self, value):
        self._data_dt = value
    @property
    def scc(self):
        return self._scc

    @scc.setter
    def scc(self, value):
        self._scc = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggr_day:
            if hasattr(self.aggr_day, 'to_alipay_dict'):
                params['aggr_day'] = self.aggr_day.to_alipay_dict()
            else:
                params['aggr_day'] = self.aggr_day
        if self.block_type:
            if hasattr(self.block_type, 'to_alipay_dict'):
                params['block_type'] = self.block_type.to_alipay_dict()
            else:
                params['block_type'] = self.block_type
        if self.data_dt:
            if hasattr(self.data_dt, 'to_alipay_dict'):
                params['data_dt'] = self.data_dt.to_alipay_dict()
            else:
                params['data_dt'] = self.data_dt
        if self.scc:
            if hasattr(self.scc, 'to_alipay_dict'):
                params['scc'] = self.scc.to_alipay_dict()
            else:
                params['scc'] = self.scc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOrgbidataBlockinfoQueryModel()
        if 'aggr_day' in d:
            o.aggr_day = d['aggr_day']
        if 'block_type' in d:
            o.block_type = d['block_type']
        if 'data_dt' in d:
            o.data_dt = d['data_dt']
        if 'scc' in d:
            o.scc = d['scc']
        return o


