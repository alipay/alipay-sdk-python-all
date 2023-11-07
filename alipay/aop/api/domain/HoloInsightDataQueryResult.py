#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HoloInsightDataResultValue import HoloInsightDataResultValue


class HoloInsightDataQueryResult(object):

    def __init__(self):
        self._headers = None
        self._metric = None
        self._tags = None
        self._values = None

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        if isinstance(value, list):
            self._headers = list()
            for i in value:
                self._headers.append(i)
    @property
    def metric(self):
        return self._metric

    @metric.setter
    def metric(self, value):
        self._metric = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, list):
            self._values = list()
            for i in value:
                if isinstance(i, HoloInsightDataResultValue):
                    self._values.append(i)
                else:
                    self._values.append(HoloInsightDataResultValue.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.headers:
            if isinstance(self.headers, list):
                for i in range(0, len(self.headers)):
                    element = self.headers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.headers[i] = element.to_alipay_dict()
            if hasattr(self.headers, 'to_alipay_dict'):
                params['headers'] = self.headers.to_alipay_dict()
            else:
                params['headers'] = self.headers
        if self.metric:
            if hasattr(self.metric, 'to_alipay_dict'):
                params['metric'] = self.metric.to_alipay_dict()
            else:
                params['metric'] = self.metric
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.values:
            if isinstance(self.values, list):
                for i in range(0, len(self.values)):
                    element = self.values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.values[i] = element.to_alipay_dict()
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HoloInsightDataQueryResult()
        if 'headers' in d:
            o.headers = d['headers']
        if 'metric' in d:
            o.metric = d['metric']
        if 'tags' in d:
            o.tags = d['tags']
        if 'values' in d:
            o.values = d['values']
        return o


