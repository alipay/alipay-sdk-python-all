#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMiniapptradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMiniapptradeQueryResponse, self).__init__()
        self._resp_alarm_trend = None
        self._trade_alarm_response_rate = None
        self._trade_avg_cost = None
        self._trade_success_rate = None
        self._trade_today_interface_success = None
        self._trade_today_total_success = None
        self._trade_total_fault = None
        self._trade_total_resp_count = None

    @property
    def resp_alarm_trend(self):
        return self._resp_alarm_trend

    @resp_alarm_trend.setter
    def resp_alarm_trend(self, value):
        self._resp_alarm_trend = value
    @property
    def trade_alarm_response_rate(self):
        return self._trade_alarm_response_rate

    @trade_alarm_response_rate.setter
    def trade_alarm_response_rate(self, value):
        self._trade_alarm_response_rate = value
    @property
    def trade_avg_cost(self):
        return self._trade_avg_cost

    @trade_avg_cost.setter
    def trade_avg_cost(self, value):
        self._trade_avg_cost = value
    @property
    def trade_success_rate(self):
        return self._trade_success_rate

    @trade_success_rate.setter
    def trade_success_rate(self, value):
        self._trade_success_rate = value
    @property
    def trade_today_interface_success(self):
        return self._trade_today_interface_success

    @trade_today_interface_success.setter
    def trade_today_interface_success(self, value):
        self._trade_today_interface_success = value
    @property
    def trade_today_total_success(self):
        return self._trade_today_total_success

    @trade_today_total_success.setter
    def trade_today_total_success(self, value):
        self._trade_today_total_success = value
    @property
    def trade_total_fault(self):
        return self._trade_total_fault

    @trade_total_fault.setter
    def trade_total_fault(self, value):
        self._trade_total_fault = value
    @property
    def trade_total_resp_count(self):
        return self._trade_total_resp_count

    @trade_total_resp_count.setter
    def trade_total_resp_count(self, value):
        self._trade_total_resp_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMiniapptradeQueryResponse, self).parse_response_content(response_content)
        if 'resp_alarm_trend' in response:
            self.resp_alarm_trend = response['resp_alarm_trend']
        if 'trade_alarm_response_rate' in response:
            self.trade_alarm_response_rate = response['trade_alarm_response_rate']
        if 'trade_avg_cost' in response:
            self.trade_avg_cost = response['trade_avg_cost']
        if 'trade_success_rate' in response:
            self.trade_success_rate = response['trade_success_rate']
        if 'trade_today_interface_success' in response:
            self.trade_today_interface_success = response['trade_today_interface_success']
        if 'trade_today_total_success' in response:
            self.trade_today_total_success = response['trade_today_total_success']
        if 'trade_total_fault' in response:
            self.trade_total_fault = response['trade_total_fault']
        if 'trade_total_resp_count' in response:
            self.trade_total_resp_count = response['trade_total_resp_count']
