#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskWarningInfo(object):

    def __init__(self):
        self._current_status = None
        self._risk_level = None
        self._source_name = None
        self._source_pid = None

    @property
    def current_status(self):
        return self._current_status

    @current_status.setter
    def current_status(self, value):
        self._current_status = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def source_name(self):
        return self._source_name

    @source_name.setter
    def source_name(self, value):
        self._source_name = value
    @property
    def source_pid(self):
        return self._source_pid

    @source_pid.setter
    def source_pid(self, value):
        self._source_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_status:
            if hasattr(self.current_status, 'to_alipay_dict'):
                params['current_status'] = self.current_status.to_alipay_dict()
            else:
                params['current_status'] = self.current_status
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.source_name:
            if hasattr(self.source_name, 'to_alipay_dict'):
                params['source_name'] = self.source_name.to_alipay_dict()
            else:
                params['source_name'] = self.source_name
        if self.source_pid:
            if hasattr(self.source_pid, 'to_alipay_dict'):
                params['source_pid'] = self.source_pid.to_alipay_dict()
            else:
                params['source_pid'] = self.source_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskWarningInfo()
        if 'current_status' in d:
            o.current_status = d['current_status']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'source_name' in d:
            o.source_name = d['source_name']
        if 'source_pid' in d:
            o.source_pid = d['source_pid']
        return o


