#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobPayslipInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobPayslipInitializeResponse, self).__init__()
        self._alipay_token = None
        self._url = None

    @property
    def alipay_token(self):
        return self._alipay_token

    @alipay_token.setter
    def alipay_token(self, value):
        self._alipay_token = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobPayslipInitializeResponse, self).parse_response_content(response_content)
        if 'alipay_token' in response:
            self.alipay_token = response['alipay_token']
        if 'url' in response:
            self.url = response['url']
