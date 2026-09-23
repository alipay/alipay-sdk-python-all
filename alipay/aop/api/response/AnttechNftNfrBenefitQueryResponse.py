#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftNfrBenefitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftNfrBenefitQueryResponse, self).__init__()
        self._benefit_status = None
        self._verify_time = None

    @property
    def benefit_status(self):
        return self._benefit_status

    @benefit_status.setter
    def benefit_status(self, value):
        self._benefit_status = value
    @property
    def verify_time(self):
        return self._verify_time

    @verify_time.setter
    def verify_time(self, value):
        self._verify_time = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftNfrBenefitQueryResponse, self).parse_response_content(response_content)
        if 'benefit_status' in response:
            self.benefit_status = response['benefit_status']
        if 'verify_time' in response:
            self.verify_time = response['verify_time']
