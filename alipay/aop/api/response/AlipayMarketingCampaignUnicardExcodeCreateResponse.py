#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignUnicardExcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUnicardExcodeCreateResponse, self).__init__()
        self._city_code = None
        self._exchange_code = None
        self._expire_date = None
        self._fail_cause = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def exchange_code(self):
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, value):
        self._exchange_code = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def fail_cause(self):
        return self._fail_cause

    @fail_cause.setter
    def fail_cause(self, value):
        self._fail_cause = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUnicardExcodeCreateResponse, self).parse_response_content(response_content)
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'exchange_code' in response:
            self.exchange_code = response['exchange_code']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'fail_cause' in response:
            self.fail_cause = response['fail_cause']
