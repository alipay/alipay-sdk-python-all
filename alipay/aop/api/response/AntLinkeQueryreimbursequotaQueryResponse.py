#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntLinkeQueryreimbursequotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntLinkeQueryreimbursequotaQueryResponse, self).__init__()
        self._quota_usd = None
        self._subscription_list = None
        self._year_month = None

    @property
    def quota_usd(self):
        return self._quota_usd

    @quota_usd.setter
    def quota_usd(self, value):
        self._quota_usd = value
    @property
    def subscription_list(self):
        return self._subscription_list

    @subscription_list.setter
    def subscription_list(self, value):
        if isinstance(value, list):
            self._subscription_list = list()
            for i in value:
                self._subscription_list.append(i)
    @property
    def year_month(self):
        return self._year_month

    @year_month.setter
    def year_month(self, value):
        self._year_month = value

    def parse_response_content(self, response_content):
        response = super(AntLinkeQueryreimbursequotaQueryResponse, self).parse_response_content(response_content)
        if 'quota_usd' in response:
            self.quota_usd = response['quota_usd']
        if 'subscription_list' in response:
            self.subscription_list = response['subscription_list']
        if 'year_month' in response:
            self.year_month = response['year_month']
