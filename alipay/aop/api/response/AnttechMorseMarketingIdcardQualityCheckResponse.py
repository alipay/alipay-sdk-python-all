#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingIdcardQualityCheckResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingIdcardQualityCheckResponse, self).__init__()
        self._biz_no = None
        self._check_result = None
        self._fallback = None
        self._passed = None
        self._reason = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value
    @property
    def fallback(self):
        return self._fallback

    @fallback.setter
    def fallback(self, value):
        self._fallback = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingIdcardQualityCheckResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'check_result' in response:
            self.check_result = response['check_result']
        if 'fallback' in response:
            self.fallback = response['fallback']
        if 'passed' in response:
            self.passed = response['passed']
        if 'reason' in response:
            self.reason = response['reason']
