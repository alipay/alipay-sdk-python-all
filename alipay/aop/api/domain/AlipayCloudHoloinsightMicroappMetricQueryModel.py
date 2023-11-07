#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HoloInsightDataQueryFilter import HoloInsightDataQueryFilter


class AlipayCloudHoloinsightMicroappMetricQueryModel(object):

    def __init__(self):
        self._aggregator = None
        self._downsample = None
        self._end = None
        self._fillpolicy = None
        self._filters = None
        self._groupby = None
        self._metric = None
        self._start = None

    @property
    def aggregator(self):
        return self._aggregator

    @aggregator.setter
    def aggregator(self, value):
        self._aggregator = value
    @property
    def downsample(self):
        return self._downsample

    @downsample.setter
    def downsample(self, value):
        self._downsample = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def fillpolicy(self):
        return self._fillpolicy

    @fillpolicy.setter
    def fillpolicy(self, value):
        self._fillpolicy = value
    @property
    def filters(self):
        return self._filters

    @filters.setter
    def filters(self, value):
        if isinstance(value, list):
            self._filters = list()
            for i in value:
                if isinstance(i, HoloInsightDataQueryFilter):
                    self._filters.append(i)
                else:
                    self._filters.append(HoloInsightDataQueryFilter.from_alipay_dict(i))
    @property
    def groupby(self):
        return self._groupby

    @groupby.setter
    def groupby(self, value):
        if isinstance(value, list):
            self._groupby = list()
            for i in value:
                self._groupby.append(i)
    @property
    def metric(self):
        return self._metric

    @metric.setter
    def metric(self, value):
        self._metric = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggregator:
            if hasattr(self.aggregator, 'to_alipay_dict'):
                params['aggregator'] = self.aggregator.to_alipay_dict()
            else:
                params['aggregator'] = self.aggregator
        if self.downsample:
            if hasattr(self.downsample, 'to_alipay_dict'):
                params['downsample'] = self.downsample.to_alipay_dict()
            else:
                params['downsample'] = self.downsample
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.fillpolicy:
            if hasattr(self.fillpolicy, 'to_alipay_dict'):
                params['fillpolicy'] = self.fillpolicy.to_alipay_dict()
            else:
                params['fillpolicy'] = self.fillpolicy
        if self.filters:
            if isinstance(self.filters, list):
                for i in range(0, len(self.filters)):
                    element = self.filters[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.filters[i] = element.to_alipay_dict()
            if hasattr(self.filters, 'to_alipay_dict'):
                params['filters'] = self.filters.to_alipay_dict()
            else:
                params['filters'] = self.filters
        if self.groupby:
            if isinstance(self.groupby, list):
                for i in range(0, len(self.groupby)):
                    element = self.groupby[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.groupby[i] = element.to_alipay_dict()
            if hasattr(self.groupby, 'to_alipay_dict'):
                params['groupby'] = self.groupby.to_alipay_dict()
            else:
                params['groupby'] = self.groupby
        if self.metric:
            if hasattr(self.metric, 'to_alipay_dict'):
                params['metric'] = self.metric.to_alipay_dict()
            else:
                params['metric'] = self.metric
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
        o = AlipayCloudHoloinsightMicroappMetricQueryModel()
        if 'aggregator' in d:
            o.aggregator = d['aggregator']
        if 'downsample' in d:
            o.downsample = d['downsample']
        if 'end' in d:
            o.end = d['end']
        if 'fillpolicy' in d:
            o.fillpolicy = d['fillpolicy']
        if 'filters' in d:
            o.filters = d['filters']
        if 'groupby' in d:
            o.groupby = d['groupby']
        if 'metric' in d:
            o.metric = d['metric']
        if 'start' in d:
            o.start = d['start']
        return o


