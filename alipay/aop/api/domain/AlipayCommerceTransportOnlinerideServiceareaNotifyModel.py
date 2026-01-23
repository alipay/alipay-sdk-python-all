#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoboDowntimeInfo import RoboDowntimeInfo


class AlipayCommerceTransportOnlinerideServiceareaNotifyModel(object):

    def __init__(self):
        self._action = None
        self._city_id = None
        self._reason = None
        self._region_id = None
        self._time_ranges = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, value):
        self._region_id = value
    @property
    def time_ranges(self):
        return self._time_ranges

    @time_ranges.setter
    def time_ranges(self, value):
        if isinstance(value, list):
            self._time_ranges = list()
            for i in value:
                if isinstance(i, RoboDowntimeInfo):
                    self._time_ranges.append(i)
                else:
                    self._time_ranges.append(RoboDowntimeInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.region_id:
            if hasattr(self.region_id, 'to_alipay_dict'):
                params['region_id'] = self.region_id.to_alipay_dict()
            else:
                params['region_id'] = self.region_id
        if self.time_ranges:
            if isinstance(self.time_ranges, list):
                for i in range(0, len(self.time_ranges)):
                    element = self.time_ranges[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_ranges[i] = element.to_alipay_dict()
            if hasattr(self.time_ranges, 'to_alipay_dict'):
                params['time_ranges'] = self.time_ranges.to_alipay_dict()
            else:
                params['time_ranges'] = self.time_ranges
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportOnlinerideServiceareaNotifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'reason' in d:
            o.reason = d['reason']
        if 'region_id' in d:
            o.region_id = d['region_id']
        if 'time_ranges' in d:
            o.time_ranges = d['time_ranges']
        return o


