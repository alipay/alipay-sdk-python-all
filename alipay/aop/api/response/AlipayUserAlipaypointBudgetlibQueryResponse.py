#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAlipaypointBudgetlibQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAlipaypointBudgetlibQueryResponse, self).__init__()
        self._budget_code = None
        self._budget_desc = None
        self._cumulative_amount = None
        self._enabled = None
        self._end_time = None
        self._remain_amount = None
        self._start_time = None

    @property
    def budget_code(self):
        return self._budget_code

    @budget_code.setter
    def budget_code(self, value):
        self._budget_code = value
    @property
    def budget_desc(self):
        return self._budget_desc

    @budget_desc.setter
    def budget_desc(self, value):
        self._budget_desc = value
    @property
    def cumulative_amount(self):
        return self._cumulative_amount

    @cumulative_amount.setter
    def cumulative_amount(self, value):
        self._cumulative_amount = value
    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAlipaypointBudgetlibQueryResponse, self).parse_response_content(response_content)
        if 'budget_code' in response:
            self.budget_code = response['budget_code']
        if 'budget_desc' in response:
            self.budget_desc = response['budget_desc']
        if 'cumulative_amount' in response:
            self.cumulative_amount = response['cumulative_amount']
        if 'enabled' in response:
            self.enabled = response['enabled']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'remain_amount' in response:
            self.remain_amount = response['remain_amount']
        if 'start_time' in response:
            self.start_time = response['start_time']
