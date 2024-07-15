#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorpManagerVO(object):

    def __init__(self):
        self._appoint_dt = None
        self._manager_name = None
        self._manager_name_en = None
        self._position_tp_code = None
        self._resignation_dt = None

    @property
    def appoint_dt(self):
        return self._appoint_dt

    @appoint_dt.setter
    def appoint_dt(self, value):
        self._appoint_dt = value
    @property
    def manager_name(self):
        return self._manager_name

    @manager_name.setter
    def manager_name(self, value):
        self._manager_name = value
    @property
    def manager_name_en(self):
        return self._manager_name_en

    @manager_name_en.setter
    def manager_name_en(self, value):
        self._manager_name_en = value
    @property
    def position_tp_code(self):
        return self._position_tp_code

    @position_tp_code.setter
    def position_tp_code(self, value):
        self._position_tp_code = value
    @property
    def resignation_dt(self):
        return self._resignation_dt

    @resignation_dt.setter
    def resignation_dt(self, value):
        self._resignation_dt = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_dt:
            if hasattr(self.appoint_dt, 'to_alipay_dict'):
                params['appoint_dt'] = self.appoint_dt.to_alipay_dict()
            else:
                params['appoint_dt'] = self.appoint_dt
        if self.manager_name:
            if hasattr(self.manager_name, 'to_alipay_dict'):
                params['manager_name'] = self.manager_name.to_alipay_dict()
            else:
                params['manager_name'] = self.manager_name
        if self.manager_name_en:
            if hasattr(self.manager_name_en, 'to_alipay_dict'):
                params['manager_name_en'] = self.manager_name_en.to_alipay_dict()
            else:
                params['manager_name_en'] = self.manager_name_en
        if self.position_tp_code:
            if hasattr(self.position_tp_code, 'to_alipay_dict'):
                params['position_tp_code'] = self.position_tp_code.to_alipay_dict()
            else:
                params['position_tp_code'] = self.position_tp_code
        if self.resignation_dt:
            if hasattr(self.resignation_dt, 'to_alipay_dict'):
                params['resignation_dt'] = self.resignation_dt.to_alipay_dict()
            else:
                params['resignation_dt'] = self.resignation_dt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorpManagerVO()
        if 'appoint_dt' in d:
            o.appoint_dt = d['appoint_dt']
        if 'manager_name' in d:
            o.manager_name = d['manager_name']
        if 'manager_name_en' in d:
            o.manager_name_en = d['manager_name_en']
        if 'position_tp_code' in d:
            o.position_tp_code = d['position_tp_code']
        if 'resignation_dt' in d:
            o.resignation_dt = d['resignation_dt']
        return o


