#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrgOperationalAggregateItem(object):

    def __init__(self):
        self._chat_uv = None
        self._data_dt = None
        self._inter_uv = None
        self._org_id = None
        self._org_name = None
        self._outpatient_penetration_rate = None
        self._outpatient_pv = None
        self._service_clk_uv = None
        self._service_expo_uv = None
        self._service_uv_ctr = None

    @property
    def chat_uv(self):
        return self._chat_uv

    @chat_uv.setter
    def chat_uv(self, value):
        self._chat_uv = value
    @property
    def data_dt(self):
        return self._data_dt

    @data_dt.setter
    def data_dt(self, value):
        self._data_dt = value
    @property
    def inter_uv(self):
        return self._inter_uv

    @inter_uv.setter
    def inter_uv(self, value):
        self._inter_uv = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def outpatient_penetration_rate(self):
        return self._outpatient_penetration_rate

    @outpatient_penetration_rate.setter
    def outpatient_penetration_rate(self, value):
        self._outpatient_penetration_rate = value
    @property
    def outpatient_pv(self):
        return self._outpatient_pv

    @outpatient_pv.setter
    def outpatient_pv(self, value):
        self._outpatient_pv = value
    @property
    def service_clk_uv(self):
        return self._service_clk_uv

    @service_clk_uv.setter
    def service_clk_uv(self, value):
        self._service_clk_uv = value
    @property
    def service_expo_uv(self):
        return self._service_expo_uv

    @service_expo_uv.setter
    def service_expo_uv(self, value):
        self._service_expo_uv = value
    @property
    def service_uv_ctr(self):
        return self._service_uv_ctr

    @service_uv_ctr.setter
    def service_uv_ctr(self, value):
        self._service_uv_ctr = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_uv:
            if hasattr(self.chat_uv, 'to_alipay_dict'):
                params['chat_uv'] = self.chat_uv.to_alipay_dict()
            else:
                params['chat_uv'] = self.chat_uv
        if self.data_dt:
            if hasattr(self.data_dt, 'to_alipay_dict'):
                params['data_dt'] = self.data_dt.to_alipay_dict()
            else:
                params['data_dt'] = self.data_dt
        if self.inter_uv:
            if hasattr(self.inter_uv, 'to_alipay_dict'):
                params['inter_uv'] = self.inter_uv.to_alipay_dict()
            else:
                params['inter_uv'] = self.inter_uv
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.outpatient_penetration_rate:
            if hasattr(self.outpatient_penetration_rate, 'to_alipay_dict'):
                params['outpatient_penetration_rate'] = self.outpatient_penetration_rate.to_alipay_dict()
            else:
                params['outpatient_penetration_rate'] = self.outpatient_penetration_rate
        if self.outpatient_pv:
            if hasattr(self.outpatient_pv, 'to_alipay_dict'):
                params['outpatient_pv'] = self.outpatient_pv.to_alipay_dict()
            else:
                params['outpatient_pv'] = self.outpatient_pv
        if self.service_clk_uv:
            if hasattr(self.service_clk_uv, 'to_alipay_dict'):
                params['service_clk_uv'] = self.service_clk_uv.to_alipay_dict()
            else:
                params['service_clk_uv'] = self.service_clk_uv
        if self.service_expo_uv:
            if hasattr(self.service_expo_uv, 'to_alipay_dict'):
                params['service_expo_uv'] = self.service_expo_uv.to_alipay_dict()
            else:
                params['service_expo_uv'] = self.service_expo_uv
        if self.service_uv_ctr:
            if hasattr(self.service_uv_ctr, 'to_alipay_dict'):
                params['service_uv_ctr'] = self.service_uv_ctr.to_alipay_dict()
            else:
                params['service_uv_ctr'] = self.service_uv_ctr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrgOperationalAggregateItem()
        if 'chat_uv' in d:
            o.chat_uv = d['chat_uv']
        if 'data_dt' in d:
            o.data_dt = d['data_dt']
        if 'inter_uv' in d:
            o.inter_uv = d['inter_uv']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'outpatient_penetration_rate' in d:
            o.outpatient_penetration_rate = d['outpatient_penetration_rate']
        if 'outpatient_pv' in d:
            o.outpatient_pv = d['outpatient_pv']
        if 'service_clk_uv' in d:
            o.service_clk_uv = d['service_clk_uv']
        if 'service_expo_uv' in d:
            o.service_expo_uv = d['service_expo_uv']
        if 'service_uv_ctr' in d:
            o.service_uv_ctr = d['service_uv_ctr']
        return o


