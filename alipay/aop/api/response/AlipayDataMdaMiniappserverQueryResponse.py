#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMiniappserverQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMiniappserverQueryResponse, self).__init__()
        self._average_recovery_cost_mins = None
        self._success_rate = None
        self._today_alarm_number = None
        self._today_alarm_response_rate = None

    @property
    def average_recovery_cost_mins(self):
        return self._average_recovery_cost_mins

    @average_recovery_cost_mins.setter
    def average_recovery_cost_mins(self, value):
        self._average_recovery_cost_mins = value
    @property
    def success_rate(self):
        return self._success_rate

    @success_rate.setter
    def success_rate(self, value):
        self._success_rate = value
    @property
    def today_alarm_number(self):
        return self._today_alarm_number

    @today_alarm_number.setter
    def today_alarm_number(self, value):
        self._today_alarm_number = value
    @property
    def today_alarm_response_rate(self):
        return self._today_alarm_response_rate

    @today_alarm_response_rate.setter
    def today_alarm_response_rate(self, value):
        self._today_alarm_response_rate = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMiniappserverQueryResponse, self).parse_response_content(response_content)
        if 'average_recovery_cost_mins' in response:
            self.average_recovery_cost_mins = response['average_recovery_cost_mins']
        if 'success_rate' in response:
            self.success_rate = response['success_rate']
        if 'today_alarm_number' in response:
            self.today_alarm_number = response['today_alarm_number']
        if 'today_alarm_response_rate' in response:
            self.today_alarm_response_rate = response['today_alarm_response_rate']
