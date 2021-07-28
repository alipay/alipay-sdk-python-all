#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FixProblemDTO import FixProblemDTO


class AlipayCommerceFixTaskproblemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceFixTaskproblemQueryResponse, self).__init__()
        self._problem_list = None

    @property
    def problem_list(self):
        return self._problem_list

    @problem_list.setter
    def problem_list(self, value):
        if isinstance(value, list):
            self._problem_list = list()
            for i in value:
                if isinstance(i, FixProblemDTO):
                    self._problem_list.append(i)
                else:
                    self._problem_list.append(FixProblemDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceFixTaskproblemQueryResponse, self).parse_response_content(response_content)
        if 'problem_list' in response:
            self.problem_list = response['problem_list']
