#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountInstfundWithdrawApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountInstfundWithdrawApplyResponse, self).__init__()
        self._instruction_no = None

    @property
    def instruction_no(self):
        return self._instruction_no

    @instruction_no.setter
    def instruction_no(self, value):
        self._instruction_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountInstfundWithdrawApplyResponse, self).parse_response_content(response_content)
        if 'instruction_no' in response:
            self.instruction_no = response['instruction_no']
