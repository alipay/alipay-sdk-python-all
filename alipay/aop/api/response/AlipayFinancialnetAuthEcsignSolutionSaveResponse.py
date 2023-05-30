#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthEcsignSolutionSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignSolutionSaveResponse, self).__init__()
        self._solution_code = None

    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignSolutionSaveResponse, self).parse_response_content(response_content)
        if 'solution_code' in response:
            self.solution_code = response['solution_code']
