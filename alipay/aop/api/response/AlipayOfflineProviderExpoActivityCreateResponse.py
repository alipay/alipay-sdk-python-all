#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SolutionVO import SolutionVO


class AlipayOfflineProviderExpoActivityCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderExpoActivityCreateResponse, self).__init__()
        self._activity_code = None
        self._solution_v_o_list = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def solution_v_o_list(self):
        return self._solution_v_o_list

    @solution_v_o_list.setter
    def solution_v_o_list(self, value):
        if isinstance(value, list):
            self._solution_v_o_list = list()
            for i in value:
                if isinstance(i, SolutionVO):
                    self._solution_v_o_list.append(i)
                else:
                    self._solution_v_o_list.append(SolutionVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderExpoActivityCreateResponse, self).parse_response_content(response_content)
        if 'activity_code' in response:
            self.activity_code = response['activity_code']
        if 'solution_v_o_list' in response:
            self.solution_v_o_list = response['solution_v_o_list']
