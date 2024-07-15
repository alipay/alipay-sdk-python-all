#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundQuotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundQuotaQueryResponse, self).__init__()
        self._to_corporate_daily_available_amount = None
        self._to_corporate_monthly_available_amount = None
        self._to_private_daily_available_amount = None
        self._to_private_monthly_available_amount = None

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
        if 'to_corporate_daily_available_amount' in response:
            self.to_corporate_daily_available_amount = response['to_corporate_daily_available_amount']
        if 'to_corporate_monthly_available_amount' in response:
            self.to_corporate_monthly_available_amount = response['to_corporate_monthly_available_amount']
        if 'to_private_daily_available_amount' in response:
            self.to_private_daily_available_amount = response['to_private_daily_available_amount']
        if 'to_private_monthly_available_amount' in response:
            self.to_private_monthly_available_amount = response['to_private_monthly_available_amount']
