#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SolutionOpenVO import SolutionOpenVO


class AlipayFinancialnetAuthEcsignSolutionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignSolutionQueryResponse, self).__init__()
        self._solution_vo = None

    @property
    def solution_vo(self):
        return self._solution_vo

    @solution_vo.setter
    def solution_vo(self, value):
        if isinstance(value, SolutionOpenVO):
            self._solution_vo = value
        else:
            self._solution_vo = SolutionOpenVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignSolutionQueryResponse, self).parse_response_content(response_content)
        if 'solution_vo' in response:
            self.solution_vo = response['solution_vo']
