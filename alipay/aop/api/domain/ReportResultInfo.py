#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportResultInfo(object):

    def __init__(self):
        self._abnormal_type = None
        self._project_name = None
        self._ref_interval = None
        self._result = None
        self._unit = None

    @property
    def abnormal_type(self):
        return self._abnormal_type

    @abnormal_type.setter
    def abnormal_type(self, value):
        self._abnormal_type = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def ref_interval(self):
        return self._ref_interval

    @ref_interval.setter
    def ref_interval(self, value):
        self._ref_interval = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.abnormal_type:
            if hasattr(self.abnormal_type, 'to_alipay_dict'):
                params['abnormal_type'] = self.abnormal_type.to_alipay_dict()
            else:
                params['abnormal_type'] = self.abnormal_type
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.ref_interval:
            if hasattr(self.ref_interval, 'to_alipay_dict'):
                params['ref_interval'] = self.ref_interval.to_alipay_dict()
            else:
                params['ref_interval'] = self.ref_interval
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportResultInfo()
        if 'abnormal_type' in d:
            o.abnormal_type = d['abnormal_type']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'ref_interval' in d:
            o.ref_interval = d['ref_interval']
        if 'result' in d:
            o.result = d['result']
        if 'unit' in d:
            o.unit = d['unit']
        return o


