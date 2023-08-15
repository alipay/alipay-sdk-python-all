#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Schedule import Schedule


class AlipayCloudCloudbaseFunctionTriggerGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionTriggerGetResponse, self).__init__()
        self._schedules = None
        self._trigger_name = None
        self._type = None

    @property
    def schedules(self):
        return self._schedules

    @schedules.setter
    def schedules(self, value):
        if isinstance(value, list):
            self._schedules = list()
            for i in value:
                if isinstance(i, Schedule):
                    self._schedules.append(i)
                else:
                    self._schedules.append(Schedule.from_alipay_dict(i))
    @property
    def trigger_name(self):
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, value):
        self._trigger_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionTriggerGetResponse, self).parse_response_content(response_content)
        if 'schedules' in response:
            self.schedules = response['schedules']
        if 'trigger_name' in response:
            self.trigger_name = response['trigger_name']
        if 'type' in response:
            self.type = response['type']
