#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeDepositVerifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeDepositVerifyQueryResponse, self).__init__()
        self._apply_date = None
        self._apply_interval = None
        self._apply_times = None
        self._match_exp_date = None
        self._match_times = None
        self._max_apply_times_daily = None
        self._max_match_times = None
        self._reason = None
        self._status = None
        self._verify_id = None

    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_interval(self):
        return self._apply_interval

    @apply_interval.setter
    def apply_interval(self, value):
        self._apply_interval = value
    @property
    def apply_times(self):
        return self._apply_times

    @apply_times.setter
    def apply_times(self, value):
        self._apply_times = value
    @property
    def match_exp_date(self):
        return self._match_exp_date

    @match_exp_date.setter
    def match_exp_date(self, value):
        self._match_exp_date = value
    @property
    def match_times(self):
        return self._match_times

    @match_times.setter
    def match_times(self, value):
        self._match_times = value
    @property
    def max_apply_times_daily(self):
        return self._max_apply_times_daily

    @max_apply_times_daily.setter
    def max_apply_times_daily(self, value):
        self._max_apply_times_daily = value
    @property
    def max_match_times(self):
        return self._max_match_times

    @max_match_times.setter
    def max_match_times(self, value):
        self._max_match_times = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeDepositVerifyQueryResponse, self).parse_response_content(response_content)
        if 'apply_date' in response:
            self.apply_date = response['apply_date']
        if 'apply_interval' in response:
            self.apply_interval = response['apply_interval']
        if 'apply_times' in response:
            self.apply_times = response['apply_times']
        if 'match_exp_date' in response:
            self.match_exp_date = response['match_exp_date']
        if 'match_times' in response:
            self.match_times = response['match_times']
        if 'max_apply_times_daily' in response:
            self.max_apply_times_daily = response['max_apply_times_daily']
        if 'max_match_times' in response:
            self.max_match_times = response['max_match_times']
        if 'reason' in response:
            self.reason = response['reason']
        if 'status' in response:
            self.status = response['status']
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
