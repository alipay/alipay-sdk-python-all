#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdReportMetricDetail(object):

    def __init__(self):
        self._memo = None
        self._metric_code = None
        self._metric_name = None
        self._metric_num = None
        self._metric_type = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def metric_code(self):
        return self._metric_code

    @metric_code.setter
    def metric_code(self, value):
        self._metric_code = value
    @property
    def metric_name(self):
        return self._metric_name

    @metric_name.setter
    def metric_name(self, value):
        self._metric_name = value
    @property
    def metric_num(self):
        return self._metric_num

    @metric_num.setter
    def metric_num(self, value):
        self._metric_num = value
    @property
    def metric_type(self):
        return self._metric_type

    @metric_type.setter
    def metric_type(self, value):
        self._metric_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.metric_code:
            if hasattr(self.metric_code, 'to_alipay_dict'):
                params['metric_code'] = self.metric_code.to_alipay_dict()
            else:
                params['metric_code'] = self.metric_code
        if self.metric_name:
            if hasattr(self.metric_name, 'to_alipay_dict'):
                params['metric_name'] = self.metric_name.to_alipay_dict()
            else:
                params['metric_name'] = self.metric_name
        if self.metric_num:
            if hasattr(self.metric_num, 'to_alipay_dict'):
                params['metric_num'] = self.metric_num.to_alipay_dict()
            else:
                params['metric_num'] = self.metric_num
        if self.metric_type:
            if hasattr(self.metric_type, 'to_alipay_dict'):
                params['metric_type'] = self.metric_type.to_alipay_dict()
            else:
                params['metric_type'] = self.metric_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdReportMetricDetail()
        if 'memo' in d:
            o.memo = d['memo']
        if 'metric_code' in d:
            o.metric_code = d['metric_code']
        if 'metric_name' in d:
            o.metric_name = d['metric_name']
        if 'metric_num' in d:
            o.metric_num = d['metric_num']
        if 'metric_type' in d:
            o.metric_type = d['metric_type']
        return o


