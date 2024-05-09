#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlarmTimeConfig import AlarmTimeConfig
from alipay.aop.api.domain.AlarmTrigger import AlarmTrigger


class AlarmRule(object):

    def __init__(self):
        self._alarm_level = None
        self._id = None
        self._name = None
        self._open = None
        self._time_config = None
        self._trigger_condition = None
        self._triggers = None

    @property
    def alarm_level(self):
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, value):
        self._alarm_level = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
    @property
    def time_config(self):
        return self._time_config

    @time_config.setter
    def time_config(self, value):
        if isinstance(value, AlarmTimeConfig):
            self._time_config = value
        else:
            self._time_config = AlarmTimeConfig.from_alipay_dict(value)
    @property
    def trigger_condition(self):
        return self._trigger_condition

    @trigger_condition.setter
    def trigger_condition(self, value):
        self._trigger_condition = value
    @property
    def triggers(self):
        return self._triggers

    @triggers.setter
    def triggers(self, value):
        if isinstance(value, list):
            self._triggers = list()
            for i in value:
                if isinstance(i, AlarmTrigger):
                    self._triggers.append(i)
                else:
                    self._triggers.append(AlarmTrigger.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alarm_level:
            if hasattr(self.alarm_level, 'to_alipay_dict'):
                params['alarm_level'] = self.alarm_level.to_alipay_dict()
            else:
                params['alarm_level'] = self.alarm_level
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open:
            if hasattr(self.open, 'to_alipay_dict'):
                params['open'] = self.open.to_alipay_dict()
            else:
                params['open'] = self.open
        if self.time_config:
            if hasattr(self.time_config, 'to_alipay_dict'):
                params['time_config'] = self.time_config.to_alipay_dict()
            else:
                params['time_config'] = self.time_config
        if self.trigger_condition:
            if hasattr(self.trigger_condition, 'to_alipay_dict'):
                params['trigger_condition'] = self.trigger_condition.to_alipay_dict()
            else:
                params['trigger_condition'] = self.trigger_condition
        if self.triggers:
            if isinstance(self.triggers, list):
                for i in range(0, len(self.triggers)):
                    element = self.triggers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.triggers[i] = element.to_alipay_dict()
            if hasattr(self.triggers, 'to_alipay_dict'):
                params['triggers'] = self.triggers.to_alipay_dict()
            else:
                params['triggers'] = self.triggers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmRule()
        if 'alarm_level' in d:
            o.alarm_level = d['alarm_level']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'open' in d:
            o.open = d['open']
        if 'time_config' in d:
            o.time_config = d['time_config']
        if 'trigger_condition' in d:
            o.trigger_condition = d['trigger_condition']
        if 'triggers' in d:
            o.triggers = d['triggers']
        return o


