#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MonitorFilter import MonitorFilter


class AlipayCloudCloudbaseMonitorMetricQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._down_sample = None
        self._end = None
        self._fill_policy = None
        self._filter_type = None
        self._metric = None
        self._monitor_filter = None
        self._product = None
        self._start = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def down_sample(self):
        return self._down_sample

    @down_sample.setter
    def down_sample(self, value):
        self._down_sample = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def fill_policy(self):
        return self._fill_policy

    @fill_policy.setter
    def fill_policy(self, value):
        self._fill_policy = value
    @property
    def filter_type(self):
        return self._filter_type

    @filter_type.setter
    def filter_type(self, value):
        self._filter_type = value
    @property
    def metric(self):
        return self._metric

    @metric.setter
    def metric(self, value):
        self._metric = value
    @property
    def monitor_filter(self):
        return self._monitor_filter

    @monitor_filter.setter
    def monitor_filter(self, value):
        if isinstance(value, MonitorFilter):
            self._monitor_filter = value
        else:
            self._monitor_filter = MonitorFilter.from_alipay_dict(value)
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.down_sample:
            if hasattr(self.down_sample, 'to_alipay_dict'):
                params['down_sample'] = self.down_sample.to_alipay_dict()
            else:
                params['down_sample'] = self.down_sample
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.fill_policy:
            if hasattr(self.fill_policy, 'to_alipay_dict'):
                params['fill_policy'] = self.fill_policy.to_alipay_dict()
            else:
                params['fill_policy'] = self.fill_policy
        if self.filter_type:
            if hasattr(self.filter_type, 'to_alipay_dict'):
                params['filter_type'] = self.filter_type.to_alipay_dict()
            else:
                params['filter_type'] = self.filter_type
        if self.metric:
            if hasattr(self.metric, 'to_alipay_dict'):
                params['metric'] = self.metric.to_alipay_dict()
            else:
                params['metric'] = self.metric
        if self.monitor_filter:
            if hasattr(self.monitor_filter, 'to_alipay_dict'):
                params['monitor_filter'] = self.monitor_filter.to_alipay_dict()
            else:
                params['monitor_filter'] = self.monitor_filter
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.start:
            if hasattr(self.start, 'to_alipay_dict'):
                params['start'] = self.start.to_alipay_dict()
            else:
                params['start'] = self.start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseMonitorMetricQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'down_sample' in d:
            o.down_sample = d['down_sample']
        if 'end' in d:
            o.end = d['end']
        if 'fill_policy' in d:
            o.fill_policy = d['fill_policy']
        if 'filter_type' in d:
            o.filter_type = d['filter_type']
        if 'metric' in d:
            o.metric = d['metric']
        if 'monitor_filter' in d:
            o.monitor_filter = d['monitor_filter']
        if 'product' in d:
            o.product = d['product']
        if 'start' in d:
            o.start = d['start']
        return o


