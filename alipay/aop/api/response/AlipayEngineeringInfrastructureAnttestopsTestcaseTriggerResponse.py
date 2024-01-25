#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEngineeringInfrastructureAnttestopsTestcaseTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEngineeringInfrastructureAnttestopsTestcaseTriggerResponse, self).__init__()
        self._case_execute_result_id = None

    @property
    def case_execute_result_id(self):
        return self._case_execute_result_id

    @case_execute_result_id.setter
    def case_execute_result_id(self, value):
        self._case_execute_result_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEngineeringInfrastructureAnttestopsTestcaseTriggerResponse, self).parse_response_content(response_content)
        if 'case_execute_result_id' in response:
            self.case_execute_result_id = response['case_execute_result_id']
