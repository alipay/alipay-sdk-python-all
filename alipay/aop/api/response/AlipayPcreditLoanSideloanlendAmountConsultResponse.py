#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanSideloanlendAmountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanlendAmountConsultResponse, self).__init__()
        self._account_status = None
        self._credit_quota = None
        self._daily_interest_rate = None
        self._end_time = None
        self._interest_rate = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None
        self._start_time = None
        self._status = None
        self._surplus_quota = None
        self._temp_credit_quota = None
        self._temp_credit_quota_end_time = None
        self._temp_credit_quota_start_time = None
        self._temp_daily_interest_rate = None
        self._temp_interest_rate = None
        self._temp_interest_rate_end_time = None
        self._temp_interest_rate_start_time = None

    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def credit_quota(self):
        return self._credit_quota

    @credit_quota.setter
    def credit_quota(self, value):
        self._credit_quota = value
    @property
    def daily_interest_rate(self):
        return self._daily_interest_rate

    @daily_interest_rate.setter
    def daily_interest_rate(self, value):
        self._daily_interest_rate = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_sub_code(self):
        return self._return_sub_code

    @return_sub_code.setter
    def return_sub_code(self, value):
        self._return_sub_code = value
    @property
    def return_sub_message(self):
        return self._return_sub_message

    @return_sub_message.setter
    def return_sub_message(self, value):
        self._return_sub_message = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def surplus_quota(self):
        return self._surplus_quota

    @surplus_quota.setter
    def surplus_quota(self, value):
        self._surplus_quota = value
    @property
    def temp_credit_quota(self):
        return self._temp_credit_quota

    @temp_credit_quota.setter
    def temp_credit_quota(self, value):
        self._temp_credit_quota = value
    @property
    def temp_credit_quota_end_time(self):
        return self._temp_credit_quota_end_time

    @temp_credit_quota_end_time.setter
    def temp_credit_quota_end_time(self, value):
        self._temp_credit_quota_end_time = value
    @property
    def temp_credit_quota_start_time(self):
        return self._temp_credit_quota_start_time

    @temp_credit_quota_start_time.setter
    def temp_credit_quota_start_time(self, value):
        self._temp_credit_quota_start_time = value
    @property
    def temp_daily_interest_rate(self):
        return self._temp_daily_interest_rate

    @temp_daily_interest_rate.setter
    def temp_daily_interest_rate(self, value):
        self._temp_daily_interest_rate = value
    @property
    def temp_interest_rate(self):
        return self._temp_interest_rate

    @temp_interest_rate.setter
    def temp_interest_rate(self, value):
        self._temp_interest_rate = value
    @property
    def temp_interest_rate_end_time(self):
        return self._temp_interest_rate_end_time

    @temp_interest_rate_end_time.setter
    def temp_interest_rate_end_time(self, value):
        self._temp_interest_rate_end_time = value
    @property
    def temp_interest_rate_start_time(self):
        return self._temp_interest_rate_start_time

    @temp_interest_rate_start_time.setter
    def temp_interest_rate_start_time(self, value):
        self._temp_interest_rate_start_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloanlendAmountConsultResponse, self).parse_response_content(response_content)
        if 'account_status' in response:
            self.account_status = response['account_status']
        if 'credit_quota' in response:
            self.credit_quota = response['credit_quota']
        if 'daily_interest_rate' in response:
            self.daily_interest_rate = response['daily_interest_rate']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'interest_rate' in response:
            self.interest_rate = response['interest_rate']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
        if 'surplus_quota' in response:
            self.surplus_quota = response['surplus_quota']
        if 'temp_credit_quota' in response:
            self.temp_credit_quota = response['temp_credit_quota']
        if 'temp_credit_quota_end_time' in response:
            self.temp_credit_quota_end_time = response['temp_credit_quota_end_time']
        if 'temp_credit_quota_start_time' in response:
            self.temp_credit_quota_start_time = response['temp_credit_quota_start_time']
        if 'temp_daily_interest_rate' in response:
            self.temp_daily_interest_rate = response['temp_daily_interest_rate']
        if 'temp_interest_rate' in response:
            self.temp_interest_rate = response['temp_interest_rate']
        if 'temp_interest_rate_end_time' in response:
            self.temp_interest_rate_end_time = response['temp_interest_rate_end_time']
        if 'temp_interest_rate_start_time' in response:
            self.temp_interest_rate_start_time = response['temp_interest_rate_start_time']
