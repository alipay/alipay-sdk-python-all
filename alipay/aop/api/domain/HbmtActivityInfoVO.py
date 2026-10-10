#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PreConsultMap import PreConsultMap


class HbmtActivityInfoVO(object):

    def __init__(self):
        self._activity_description = None
        self._activity_id = None
        self._calc_mode = None
        self._default_percentage = None
        self._end_time = None
        self._flat_ratio = None
        self._flat_ratio_cap = None
        self._level_pricing = None
        self._start_time = None

    @property
    def activity_description(self):
        return self._activity_description

    @activity_description.setter
    def activity_description(self, value):
        self._activity_description = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def calc_mode(self):
        return self._calc_mode

    @calc_mode.setter
    def calc_mode(self, value):
        self._calc_mode = value
    @property
    def default_percentage(self):
        return self._default_percentage

    @default_percentage.setter
    def default_percentage(self, value):
        self._default_percentage = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def flat_ratio(self):
        return self._flat_ratio

    @flat_ratio.setter
    def flat_ratio(self, value):
        self._flat_ratio = value
    @property
    def flat_ratio_cap(self):
        return self._flat_ratio_cap

    @flat_ratio_cap.setter
    def flat_ratio_cap(self, value):
        self._flat_ratio_cap = value
    @property
    def level_pricing(self):
        return self._level_pricing

    @level_pricing.setter
    def level_pricing(self, value):
        if isinstance(value, PreConsultMap):
            self._level_pricing = value
        else:
            self._level_pricing = PreConsultMap.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_description:
            if hasattr(self.activity_description, 'to_alipay_dict'):
                params['activity_description'] = self.activity_description.to_alipay_dict()
            else:
                params['activity_description'] = self.activity_description
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.calc_mode:
            if hasattr(self.calc_mode, 'to_alipay_dict'):
                params['calc_mode'] = self.calc_mode.to_alipay_dict()
            else:
                params['calc_mode'] = self.calc_mode
        if self.default_percentage:
            if hasattr(self.default_percentage, 'to_alipay_dict'):
                params['default_percentage'] = self.default_percentage.to_alipay_dict()
            else:
                params['default_percentage'] = self.default_percentage
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.flat_ratio:
            if hasattr(self.flat_ratio, 'to_alipay_dict'):
                params['flat_ratio'] = self.flat_ratio.to_alipay_dict()
            else:
                params['flat_ratio'] = self.flat_ratio
        if self.flat_ratio_cap:
            if hasattr(self.flat_ratio_cap, 'to_alipay_dict'):
                params['flat_ratio_cap'] = self.flat_ratio_cap.to_alipay_dict()
            else:
                params['flat_ratio_cap'] = self.flat_ratio_cap
        if self.level_pricing:
            if hasattr(self.level_pricing, 'to_alipay_dict'):
                params['level_pricing'] = self.level_pricing.to_alipay_dict()
            else:
                params['level_pricing'] = self.level_pricing
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
        o = HbmtActivityInfoVO()
        if 'activity_description' in d:
            o.activity_description = d['activity_description']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'calc_mode' in d:
            o.calc_mode = d['calc_mode']
        if 'default_percentage' in d:
            o.default_percentage = d['default_percentage']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'flat_ratio' in d:
            o.flat_ratio = d['flat_ratio']
        if 'flat_ratio_cap' in d:
            o.flat_ratio_cap = d['flat_ratio_cap']
        if 'level_pricing' in d:
            o.level_pricing = d['level_pricing']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


