#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomMetric import CustomMetric


class AlipayCommerceDataCustommetricSyncModel(object):

    def __init__(self):
        self._metric_data = None
        self._namespace = None

    @property
    def metric_data(self):
        return self._metric_data

    @metric_data.setter
    def metric_data(self, value):
        if isinstance(value, list):
            self._metric_data = list()
            for i in value:
                if isinstance(i, CustomMetric):
                    self._metric_data.append(i)
                else:
                    self._metric_data.append(CustomMetric.from_alipay_dict(i))
    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, value):
        self._namespace = value


    def to_alipay_dict(self):
        params = dict()
        if self.metric_data:
            if isinstance(self.metric_data, list):
                for i in range(0, len(self.metric_data)):
                    element = self.metric_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.metric_data[i] = element.to_alipay_dict()
            if hasattr(self.metric_data, 'to_alipay_dict'):
                params['metric_data'] = self.metric_data.to_alipay_dict()
            else:
                params['metric_data'] = self.metric_data
        if self.namespace:
            if hasattr(self.namespace, 'to_alipay_dict'):
                params['namespace'] = self.namespace.to_alipay_dict()
            else:
                params['namespace'] = self.namespace
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataCustommetricSyncModel()
        if 'metric_data' in d:
            o.metric_data = d['metric_data']
        if 'namespace' in d:
            o.namespace = d['namespace']
        return o


