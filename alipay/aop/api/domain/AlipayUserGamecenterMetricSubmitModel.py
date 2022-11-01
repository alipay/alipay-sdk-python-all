#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGamecenterMetricSubmitModel(object):

    def __init__(self):
        self._metric_content = None
        self._metric_date = None

    @property
    def metric_content(self):
        return self._metric_content

    @metric_content.setter
    def metric_content(self, value):
        self._metric_content = value
    @property
    def metric_date(self):
        return self._metric_date

    @metric_date.setter
    def metric_date(self, value):
        self._metric_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.metric_content:
            if hasattr(self.metric_content, 'to_alipay_dict'):
                params['metric_content'] = self.metric_content.to_alipay_dict()
            else:
                params['metric_content'] = self.metric_content
        if self.metric_date:
            if hasattr(self.metric_date, 'to_alipay_dict'):
                params['metric_date'] = self.metric_date.to_alipay_dict()
            else:
                params['metric_date'] = self.metric_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserGamecenterMetricSubmitModel()
        if 'metric_content' in d:
            o.metric_content = d['metric_content']
        if 'metric_date' in d:
            o.metric_date = d['metric_date']
        return o


