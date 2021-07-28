#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiDiscountSolutionOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiDiscountSolutionOnlineResponse, self).__init__()
        self._solution_id = None
        self._success = None

    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiDiscountSolutionOnlineResponse, self).parse_response_content(response_content)
        if 'solution_id' in response:
            self.solution_id = response['solution_id']
        if 'success' in response:
            self.success = response['success']
