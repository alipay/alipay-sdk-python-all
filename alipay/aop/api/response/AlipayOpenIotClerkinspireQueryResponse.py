#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotClerkinspireQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotClerkinspireQueryResponse, self).__init__()
        self._begin_time = None
        self._checkin_device_limit = None
        self._clerk_limit = None
        self._daily_max_trade_threshold = None
        self._end_time = None
        self._join_status = None
        self._single_reward_amount = None
        self._trade_threshold = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def checkin_device_limit(self):
        return self._checkin_device_limit

    @checkin_device_limit.setter
    def checkin_device_limit(self, value):
        self._checkin_device_limit = value
    @property
    def clerk_limit(self):
        return self._clerk_limit

    @clerk_limit.setter
    def clerk_limit(self, value):
        self._clerk_limit = value
    @property
    def daily_max_trade_threshold(self):
        return self._daily_max_trade_threshold

    @daily_max_trade_threshold.setter
    def daily_max_trade_threshold(self, value):
        self._daily_max_trade_threshold = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def join_status(self):
        return self._join_status

    @join_status.setter
    def join_status(self, value):
        self._join_status = value
    @property
    def single_reward_amount(self):
        return self._single_reward_amount

    @single_reward_amount.setter
    def single_reward_amount(self, value):
        self._single_reward_amount = value
    @property
    def trade_threshold(self):
        return self._trade_threshold

    @trade_threshold.setter
    def trade_threshold(self, value):
        self._trade_threshold = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotClerkinspireQueryResponse, self).parse_response_content(response_content)
        if 'begin_time' in response:
            self.begin_time = response['begin_time']
        if 'checkin_device_limit' in response:
            self.checkin_device_limit = response['checkin_device_limit']
        if 'clerk_limit' in response:
            self.clerk_limit = response['clerk_limit']
        if 'daily_max_trade_threshold' in response:
            self.daily_max_trade_threshold = response['daily_max_trade_threshold']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'join_status' in response:
            self.join_status = response['join_status']
        if 'single_reward_amount' in response:
            self.single_reward_amount = response['single_reward_amount']
        if 'trade_threshold' in response:
            self.trade_threshold = response['trade_threshold']
