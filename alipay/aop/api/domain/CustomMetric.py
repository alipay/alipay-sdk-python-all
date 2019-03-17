#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Dimension import Dimension


class CustomMetric(object):

    def __init__(self):
        self._biz_time = None
        self._dimensions = None
        self._metric_name = None
        self._value = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        if isinstance(value, list):
            self._dimensions = list()
            for i in value:
                if isinstance(i, Dimension):
                    self._dimensions.append(i)
                else:
                    self._dimensions.append(Dimension.from_alipay_dict(i))
    @property
    def metric_name(self):
        return self._metric_name

    @metric_name.setter
    def metric_name(self, value):
        self._metric_name = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.dimensions:
            if isinstance(self.dimensions, list):
                for i in range(0, len(self.dimensions)):
                    element = self.dimensions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dimensions[i] = element.to_alipay_dict()
            if hasattr(self.dimensions, 'to_alipay_dict'):
                params['dimensions'] = self.dimensions.to_alipay_dict()
            else:
                params['dimensions'] = self.dimensions
        if self.metric_name:
            if hasattr(self.metric_name, 'to_alipay_dict'):
                params['metric_name'] = self.metric_name.to_alipay_dict()
            else:
                params['metric_name'] = self.metric_name
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomMetric()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'dimensions' in d:
            o.dimensions = d['dimensions']
        if 'metric_name' in d:
            o.metric_name = d['metric_name']
        if 'value' in d:
            o.value = d['value']
        return o


