#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlarmHistory import AlarmHistory


class AlipayCloudCloudbaseMonitorAlarmhistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseMonitorAlarmhistoryQueryResponse, self).__init__()
        self._alarm_histories = None

    @property
    def alarm_histories(self):
        return self._alarm_histories

    @alarm_histories.setter
    def alarm_histories(self, value):
        if isinstance(value, list):
            self._alarm_histories = list()
            for i in value:
                if isinstance(i, AlarmHistory):
                    self._alarm_histories.append(i)
                else:
                    self._alarm_histories.append(AlarmHistory.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseMonitorAlarmhistoryQueryResponse, self).parse_response_content(response_content)
        if 'alarm_histories' in response:
            self.alarm_histories = response['alarm_histories']
