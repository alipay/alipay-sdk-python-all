#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseMonitorAlarmhistoryGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseMonitorAlarmhistoryGetResponse, self).__init__()
        self._alarm_level = None
        self._alarm_time = None
        self._duration = None
        self._id = None
        self._recover_time = None
        self._rule_id = None
        self._rule_name = None
        self._trigger_content = None

    @property
    def alarm_level(self):
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, value):
        self._alarm_level = value
    @property
    def alarm_time(self):
        return self._alarm_time

    @alarm_time.setter
    def alarm_time(self, value):
        self._alarm_time = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def recover_time(self):
        return self._recover_time

    @recover_time.setter
    def recover_time(self, value):
        self._recover_time = value
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
    def trigger_content(self):
        return self._trigger_content

    @trigger_content.setter
    def trigger_content(self, value):
        self._trigger_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseMonitorAlarmhistoryGetResponse, self).parse_response_content(response_content)
        if 'alarm_level' in response:
            self.alarm_level = response['alarm_level']
        if 'alarm_time' in response:
            self.alarm_time = response['alarm_time']
        if 'duration' in response:
            self.duration = response['duration']
        if 'id' in response:
            self.id = response['id']
        if 'recover_time' in response:
            self.recover_time = response['recover_time']
        if 'rule_id' in response:
            self.rule_id = response['rule_id']
        if 'rule_name' in response:
            self.rule_name = response['rule_name']
        if 'trigger_content' in response:
            self.trigger_content = response['trigger_content']
