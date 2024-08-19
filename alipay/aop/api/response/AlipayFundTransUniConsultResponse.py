#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransUniConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransUniConsultResponse, self).__init__()
        self._consult_date = None
        self._guide_url = None
        self._result = None

    @property
    def consult_date(self):
        return self._consult_date

    @consult_date.setter
    def consult_date(self, value):
        self._consult_date = value
    @property
    def guide_url(self):
        return self._guide_url

    @guide_url.setter
    def guide_url(self, value):
        self._guide_url = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransUniConsultResponse, self).parse_response_content(response_content)
        if 'consult_date' in response:
            self.consult_date = response['consult_date']
        if 'guide_url' in response:
            self.guide_url = response['guide_url']
        if 'result' in response:
            self.result = response['result']
