#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCardGenerateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCardGenerateQueryResponse, self).__init__()
        self._fund_card_generate_no = None
        self._generate_finish_time = None
        self._proces_finish_time = None
        self._status = None

    @property
    def fund_card_generate_no(self):
        return self._fund_card_generate_no

    @fund_card_generate_no.setter
    def fund_card_generate_no(self, value):
        self._fund_card_generate_no = value
    @property
    def generate_finish_time(self):
        return self._generate_finish_time

    @generate_finish_time.setter
    def generate_finish_time(self, value):
        self._generate_finish_time = value
    @property
    def proces_finish_time(self):
        return self._proces_finish_time

    @proces_finish_time.setter
    def proces_finish_time(self, value):
        self._proces_finish_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCardGenerateQueryResponse, self).parse_response_content(response_content)
        if 'fund_card_generate_no' in response:
            self.fund_card_generate_no = response['fund_card_generate_no']
        if 'generate_finish_time' in response:
            self.generate_finish_time = response['generate_finish_time']
        if 'proces_finish_time' in response:
            self.proces_finish_time = response['proces_finish_time']
        if 'status' in response:
            self.status = response['status']
