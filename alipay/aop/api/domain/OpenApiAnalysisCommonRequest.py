#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiAnalysisCommonRequest(object):

    def __init__(self):
        self._channel_type = None
        self._compare_type = None
        self._end_date = None
        self._multi_app_id = None
        self._start_date = None
        self._time_granularity = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def compare_type(self):
        return self._compare_type

    @compare_type.setter
    def compare_type(self, value):
        self._compare_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def multi_app_id(self):
        return self._multi_app_id

    @multi_app_id.setter
    def multi_app_id(self, value):
        self._multi_app_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def time_granularity(self):
        return self._time_granularity

    @time_granularity.setter
    def time_granularity(self, value):
        self._time_granularity = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.compare_type:
            if hasattr(self.compare_type, 'to_alipay_dict'):
                params['compare_type'] = self.compare_type.to_alipay_dict()
            else:
                params['compare_type'] = self.compare_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.multi_app_id:
            if hasattr(self.multi_app_id, 'to_alipay_dict'):
                params['multi_app_id'] = self.multi_app_id.to_alipay_dict()
            else:
                params['multi_app_id'] = self.multi_app_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.time_granularity:
            if hasattr(self.time_granularity, 'to_alipay_dict'):
                params['time_granularity'] = self.time_granularity.to_alipay_dict()
            else:
                params['time_granularity'] = self.time_granularity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiAnalysisCommonRequest()
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'compare_type' in d:
            o.compare_type = d['compare_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'multi_app_id' in d:
            o.multi_app_id = d['multi_app_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'time_granularity' in d:
            o.time_granularity = d['time_granularity']
        return o


