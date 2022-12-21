#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IdeployForecastData(object):

    def __init__(self):
        self._business_type = None
        self._channel = None
        self._end_time = None
        self._period_interval = None
        self._predict_result_value = None
        self._scheme_guid = None
        self._scheme_name = None
        self._skill_group = None
        self._start_time = None

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def period_interval(self):
        return self._period_interval

    @period_interval.setter
    def period_interval(self, value):
        self._period_interval = value
    @property
    def predict_result_value(self):
        return self._predict_result_value

    @predict_result_value.setter
    def predict_result_value(self, value):
        self._predict_result_value = value
    @property
    def scheme_guid(self):
        return self._scheme_guid

    @scheme_guid.setter
    def scheme_guid(self, value):
        self._scheme_guid = value
    @property
    def scheme_name(self):
        return self._scheme_name

    @scheme_name.setter
    def scheme_name(self, value):
        self._scheme_name = value
    @property
    def skill_group(self):
        return self._skill_group

    @skill_group.setter
    def skill_group(self, value):
        self._skill_group = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.period_interval:
            if hasattr(self.period_interval, 'to_alipay_dict'):
                params['period_interval'] = self.period_interval.to_alipay_dict()
            else:
                params['period_interval'] = self.period_interval
        if self.predict_result_value:
            if hasattr(self.predict_result_value, 'to_alipay_dict'):
                params['predict_result_value'] = self.predict_result_value.to_alipay_dict()
            else:
                params['predict_result_value'] = self.predict_result_value
        if self.scheme_guid:
            if hasattr(self.scheme_guid, 'to_alipay_dict'):
                params['scheme_guid'] = self.scheme_guid.to_alipay_dict()
            else:
                params['scheme_guid'] = self.scheme_guid
        if self.scheme_name:
            if hasattr(self.scheme_name, 'to_alipay_dict'):
                params['scheme_name'] = self.scheme_name.to_alipay_dict()
            else:
                params['scheme_name'] = self.scheme_name
        if self.skill_group:
            if hasattr(self.skill_group, 'to_alipay_dict'):
                params['skill_group'] = self.skill_group.to_alipay_dict()
            else:
                params['skill_group'] = self.skill_group
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IdeployForecastData()
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'period_interval' in d:
            o.period_interval = d['period_interval']
        if 'predict_result_value' in d:
            o.predict_result_value = d['predict_result_value']
        if 'scheme_guid' in d:
            o.scheme_guid = d['scheme_guid']
        if 'scheme_name' in d:
            o.scheme_name = d['scheme_name']
        if 'skill_group' in d:
            o.skill_group = d['skill_group']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


