#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlarmSubscribe import AlarmSubscribe


class AlipayCloudCloudbaseMonitorAlarmsubscribeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseMonitorAlarmsubscribeQueryResponse, self).__init__()
        self._alarm_subscribes = None

    @property
    def alarm_subscribes(self):
        return self._alarm_subscribes

    @alarm_subscribes.setter
    def alarm_subscribes(self, value):
        if isinstance(value, list):
            self._alarm_subscribes = list()
            for i in value:
                if isinstance(i, AlarmSubscribe):
                    self._alarm_subscribes.append(i)
                else:
                    self._alarm_subscribes.append(AlarmSubscribe.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseMonitorAlarmsubscribeQueryResponse, self).parse_response_content(response_content)
        if 'alarm_subscribes' in response:
            self.alarm_subscribes = response['alarm_subscribes']
