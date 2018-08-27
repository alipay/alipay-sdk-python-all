#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitInfo(object):

    def __init__(self):
        self._benefit_info_id = None
        self._benefit_name = None
        self._benefit_name_cn = None
        self._benefit_type = None
        self._dispatch_dt = None
        self._end_dt = None
        self._start_dt = None
        self._status = None

    @property
    def benefit_info_id(self):
        return self._benefit_info_id

    @benefit_info_id.setter
    def benefit_info_id(self, value):
        self._benefit_info_id = value
    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def benefit_name_cn(self):
        return self._benefit_name_cn

    @benefit_name_cn.setter
    def benefit_name_cn(self, value):
        self._benefit_name_cn = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def dispatch_dt(self):
        return self._dispatch_dt

    @dispatch_dt.setter
    def dispatch_dt(self, value):
        self._dispatch_dt = value
    @property
    def end_dt(self):
        return self._end_dt

    @end_dt.setter
    def end_dt(self, value):
        self._end_dt = value
    @property
    def start_dt(self):
        return self._start_dt

    @start_dt.setter
    def start_dt(self, value):
        self._start_dt = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_info_id:
            if hasattr(self.benefit_info_id, 'to_alipay_dict'):
                params['benefit_info_id'] = self.benefit_info_id.to_alipay_dict()
            else:
                params['benefit_info_id'] = self.benefit_info_id
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.benefit_name_cn:
            if hasattr(self.benefit_name_cn, 'to_alipay_dict'):
                params['benefit_name_cn'] = self.benefit_name_cn.to_alipay_dict()
            else:
                params['benefit_name_cn'] = self.benefit_name_cn
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.dispatch_dt:
            if hasattr(self.dispatch_dt, 'to_alipay_dict'):
                params['dispatch_dt'] = self.dispatch_dt.to_alipay_dict()
            else:
                params['dispatch_dt'] = self.dispatch_dt
        if self.end_dt:
            if hasattr(self.end_dt, 'to_alipay_dict'):
                params['end_dt'] = self.end_dt.to_alipay_dict()
            else:
                params['end_dt'] = self.end_dt
        if self.start_dt:
            if hasattr(self.start_dt, 'to_alipay_dict'):
                params['start_dt'] = self.start_dt.to_alipay_dict()
            else:
                params['start_dt'] = self.start_dt
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitInfo()
        if 'benefit_info_id' in d:
            o.benefit_info_id = d['benefit_info_id']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'benefit_name_cn' in d:
            o.benefit_name_cn = d['benefit_name_cn']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'dispatch_dt' in d:
            o.dispatch_dt = d['dispatch_dt']
        if 'end_dt' in d:
            o.end_dt = d['end_dt']
        if 'start_dt' in d:
            o.start_dt = d['start_dt']
        if 'status' in d:
            o.status = d['status']
        return o


