#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlarmInfo import AlarmInfo


class AlipayEbppIndustryGovWeatheralarmSyncModel(object):

    def __init__(self):
        self._alarm_list = None
        self._source = None

    @property
    def alarm_list(self):
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, value):
        if isinstance(value, list):
            self._alarm_list = list()
            for i in value:
                if isinstance(i, AlarmInfo):
                    self._alarm_list.append(i)
                else:
                    self._alarm_list.append(AlarmInfo.from_alipay_dict(i))
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.alarm_list:
            if isinstance(self.alarm_list, list):
                for i in range(0, len(self.alarm_list)):
                    element = self.alarm_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.alarm_list[i] = element.to_alipay_dict()
            if hasattr(self.alarm_list, 'to_alipay_dict'):
                params['alarm_list'] = self.alarm_list.to_alipay_dict()
            else:
                params['alarm_list'] = self.alarm_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryGovWeatheralarmSyncModel()
        if 'alarm_list' in d:
            o.alarm_list = d['alarm_list']
        if 'source' in d:
            o.source = d['source']
        return o


