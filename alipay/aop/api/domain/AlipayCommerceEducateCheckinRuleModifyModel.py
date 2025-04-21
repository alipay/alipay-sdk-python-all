#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCheckinRuleModifyModel(object):

    def __init__(self):
        self._enable_status = None
        self._end_time = None
        self._frequency_type = None
        self._inst_id = None
        self._picture_check = None
        self._place_check = None
        self._place_id_list = None
        self._radius = None
        self._rule_id = None
        self._rule_name = None
        self._start_time = None
        self._week_day_list = None

    @property
    def enable_status(self):
        return self._enable_status

    @enable_status.setter
    def enable_status(self, value):
        self._enable_status = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def frequency_type(self):
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, value):
        self._frequency_type = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def picture_check(self):
        return self._picture_check

    @picture_check.setter
    def picture_check(self, value):
        self._picture_check = value
    @property
    def place_check(self):
        return self._place_check

    @place_check.setter
    def place_check(self, value):
        self._place_check = value
    @property
    def place_id_list(self):
        return self._place_id_list

    @place_id_list.setter
    def place_id_list(self, value):
        if isinstance(value, list):
            self._place_id_list = list()
            for i in value:
                self._place_id_list.append(i)
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def week_day_list(self):
        return self._week_day_list

    @week_day_list.setter
    def week_day_list(self, value):
        if isinstance(value, list):
            self._week_day_list = list()
            for i in value:
                self._week_day_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.enable_status:
            if hasattr(self.enable_status, 'to_alipay_dict'):
                params['enable_status'] = self.enable_status.to_alipay_dict()
            else:
                params['enable_status'] = self.enable_status
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.frequency_type:
            if hasattr(self.frequency_type, 'to_alipay_dict'):
                params['frequency_type'] = self.frequency_type.to_alipay_dict()
            else:
                params['frequency_type'] = self.frequency_type
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.picture_check:
            if hasattr(self.picture_check, 'to_alipay_dict'):
                params['picture_check'] = self.picture_check.to_alipay_dict()
            else:
                params['picture_check'] = self.picture_check
        if self.place_check:
            if hasattr(self.place_check, 'to_alipay_dict'):
                params['place_check'] = self.place_check.to_alipay_dict()
            else:
                params['place_check'] = self.place_check
        if self.place_id_list:
            if isinstance(self.place_id_list, list):
                for i in range(0, len(self.place_id_list)):
                    element = self.place_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.place_id_list[i] = element.to_alipay_dict()
            if hasattr(self.place_id_list, 'to_alipay_dict'):
                params['place_id_list'] = self.place_id_list.to_alipay_dict()
            else:
                params['place_id_list'] = self.place_id_list
        if self.radius:
            if hasattr(self.radius, 'to_alipay_dict'):
                params['radius'] = self.radius.to_alipay_dict()
            else:
                params['radius'] = self.radius
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.week_day_list:
            if isinstance(self.week_day_list, list):
                for i in range(0, len(self.week_day_list)):
                    element = self.week_day_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_day_list[i] = element.to_alipay_dict()
            if hasattr(self.week_day_list, 'to_alipay_dict'):
                params['week_day_list'] = self.week_day_list.to_alipay_dict()
            else:
                params['week_day_list'] = self.week_day_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCheckinRuleModifyModel()
        if 'enable_status' in d:
            o.enable_status = d['enable_status']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'frequency_type' in d:
            o.frequency_type = d['frequency_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'picture_check' in d:
            o.picture_check = d['picture_check']
        if 'place_check' in d:
            o.place_check = d['place_check']
        if 'place_id_list' in d:
            o.place_id_list = d['place_id_list']
        if 'radius' in d:
            o.radius = d['radius']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'week_day_list' in d:
            o.week_day_list = d['week_day_list']
        return o


