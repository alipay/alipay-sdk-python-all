#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundQuotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundQuotaQueryResponse, self).__init__()
        self._active_new_quota_daily_remain_limit_type = None
        self._active_new_quota_daily_remain_limited = None
        self._active_new_quota_monthly_remain_limit_type = None
        self._active_new_quota_monthly_remain_limited = None
        self._active_quota_is_new = None
        self._new_quota_daily = None
        self._new_quota_daily_remain = None
        self._new_quota_monthly = None
        self._new_quota_monthly_remain = None
        self._new_quota_single_max = None
        self._new_quota_single_min = None
        self._to_corporate_daily_available_amount = None
        self._to_corporate_monthly_available_amount = None
        self._to_private_daily_available_amount = None
        self._to_private_monthly_available_amount = None

    @property
    def active_new_quota_daily_remain_limit_type(self):
        return self._active_new_quota_daily_remain_limit_type

    @active_new_quota_daily_remain_limit_type.setter
    def active_new_quota_daily_remain_limit_type(self, value):
        self._active_new_quota_daily_remain_limit_type = value
    @property
    def active_new_quota_daily_remain_limited(self):
        return self._active_new_quota_daily_remain_limited

    @active_new_quota_daily_remain_limited.setter
    def active_new_quota_daily_remain_limited(self, value):
        self._active_new_quota_daily_remain_limited = value
    @property
    def active_new_quota_monthly_remain_limit_type(self):
        return self._active_new_quota_monthly_remain_limit_type

    @active_new_quota_monthly_remain_limit_type.setter
    def active_new_quota_monthly_remain_limit_type(self, value):
        self._active_new_quota_monthly_remain_limit_type = value
    @property
    def active_new_quota_monthly_remain_limited(self):
        return self._active_new_quota_monthly_remain_limited

    @active_new_quota_monthly_remain_limited.setter
    def active_new_quota_monthly_remain_limited(self, value):
        self._active_new_quota_monthly_remain_limited = value
    @property
    def active_quota_is_new(self):
        return self._active_quota_is_new

    @active_quota_is_new.setter
    def active_quota_is_new(self, value):
        self._active_quota_is_new = value
    @property
    def new_quota_daily(self):
        return self._new_quota_daily

    @new_quota_daily.setter
    def new_quota_daily(self, value):
        self._new_quota_daily = value
    @property
    def new_quota_daily_remain(self):
        return self._new_quota_daily_remain

    @new_quota_daily_remain.setter
    def new_quota_daily_remain(self, value):
        self._new_quota_daily_remain = value
    @property
    def new_quota_monthly(self):
        return self._new_quota_monthly

    @new_quota_monthly.setter
    def new_quota_monthly(self, value):
        self._new_quota_monthly = value
    @property
    def new_quota_monthly_remain(self):
        return self._new_quota_monthly_remain

    @new_quota_monthly_remain.setter
    def new_quota_monthly_remain(self, value):
        self._new_quota_monthly_remain = value
    @property
    def new_quota_single_max(self):
        return self._new_quota_single_max

    @new_quota_single_max.setter
    def new_quota_single_max(self, value):
        self._new_quota_single_max = value
    @property
    def new_quota_single_min(self):
        return self._new_quota_single_min

    @new_quota_single_min.setter
    def new_quota_single_min(self, value):
        self._new_quota_single_min = value
    @property
    def to_corporate_daily_available_amount(self):
        return self._to_corporate_daily_available_amount

    @to_corporate_daily_available_amount.setter
    def to_corporate_daily_available_amount(self, value):
        self._to_corporate_daily_available_amount = value
    @property
    def to_corporate_monthly_available_amount(self):
        return self._to_corporate_monthly_available_amount

    @to_corporate_monthly_available_amount.setter
    def to_corporate_monthly_available_amount(self, value):
        self._to_corporate_monthly_available_amount = value
    @property
    def to_private_daily_available_amount(self):
        return self._to_private_daily_available_amount

    @to_private_daily_available_amount.setter
    def to_private_daily_available_amount(self, value):
        self._to_private_daily_available_amount = value
    @property
    def to_private_monthly_available_amount(self):
        return self._to_private_monthly_available_amount

    @to_private_monthly_available_amount.setter
    def to_private_monthly_available_amount(self, value):
        self._to_private_monthly_available_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundQuotaQueryResponse, self).parse_response_content(response_content)
        if 'active_new_quota_daily_remain_limit_type' in response:
            self.active_new_quota_daily_remain_limit_type = response['active_new_quota_daily_remain_limit_type']
        if 'active_new_quota_daily_remain_limited' in response:
            self.active_new_quota_daily_remain_limited = response['active_new_quota_daily_remain_limited']
        if 'active_new_quota_monthly_remain_limit_type' in response:
            self.active_new_quota_monthly_remain_limit_type = response['active_new_quota_monthly_remain_limit_type']
        if 'active_new_quota_monthly_remain_limited' in response:
            self.active_new_quota_monthly_remain_limited = response['active_new_quota_monthly_remain_limited']
        if 'active_quota_is_new' in response:
            self.active_quota_is_new = response['active_quota_is_new']
        if 'new_quota_daily' in response:
            self.new_quota_daily = response['new_quota_daily']
        if 'new_quota_daily_remain' in response:
            self.new_quota_daily_remain = response['new_quota_daily_remain']
        if 'new_quota_monthly' in response:
            self.new_quota_monthly = response['new_quota_monthly']
        if 'new_quota_monthly_remain' in response:
            self.new_quota_monthly_remain = response['new_quota_monthly_remain']
        if 'new_quota_single_max' in response:
            self.new_quota_single_max = response['new_quota_single_max']
        if 'new_quota_single_min' in response:
            self.new_quota_single_min = response['new_quota_single_min']
        if 'to_corporate_daily_available_amount' in response:
            self.to_corporate_daily_available_amount = response['to_corporate_daily_available_amount']
        if 'to_corporate_monthly_available_amount' in response:
            self.to_corporate_monthly_available_amount = response['to_corporate_monthly_available_amount']
        if 'to_private_daily_available_amount' in response:
            self.to_private_daily_available_amount = response['to_private_daily_available_amount']
        if 'to_private_monthly_available_amount' in response:
            self.to_private_monthly_available_amount = response['to_private_monthly_available_amount']
