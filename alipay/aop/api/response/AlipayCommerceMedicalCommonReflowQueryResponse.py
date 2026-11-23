#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommonReflowQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommonReflowQueryResponse, self).__init__()
        self._award_time = None
        self._has_cashback = None

    @property
    def award_time(self):
        return self._award_time

    @award_time.setter
    def award_time(self, value):
        self._award_time = value
    @property
    def has_cashback(self):
        return self._has_cashback

    @has_cashback.setter
    def has_cashback(self, value):
        self._has_cashback = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommonReflowQueryResponse, self).parse_response_content(response_content)
        if 'award_time' in response:
            self.award_time = response['award_time']
        if 'has_cashback' in response:
            self.has_cashback = response['has_cashback']
