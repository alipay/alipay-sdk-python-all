#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlarmTimeConfig import AlarmTimeConfig
from alipay.aop.api.domain.AlarmTrigger import AlarmTrigger


class AlipayCloudCloudbaseMonitorAlarmruleGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseMonitorAlarmruleGetResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseMonitorAlarmruleGetResponse, self).parse_response_content(response_content)
        if 'alarm_level' in response:
            self.alarm_level = response['alarm_level']
        if 'id' in response:
            self.id = response['id']
        if 'name' in response:
            self.name = response['name']
        if 'open' in response:
            self.open = response['open']
        if 'time_config' in response:
            self.time_config = response['time_config']
        if 'trigger_condition' in response:
            self.trigger_condition = response['trigger_condition']
        if 'triggers' in response:
            self.triggers = response['triggers']
