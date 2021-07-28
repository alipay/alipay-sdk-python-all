#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiDiscountSolutionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiDiscountSolutionCreateResponse, self).__init__()
        self._solution_id = None

    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiDiscountSolutionCreateResponse, self).parse_response_content(response_content)
        if 'solution_id' in response:
            self.solution_id = response['solution_id']
