#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ScheduleOdResult import ScheduleOdResult


class AlipayDataAiserviceCloudbusScheduletaskodQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceCloudbusScheduletaskodQueryResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ScheduleOdResult):
            self._result = value
        else:
            self._result = ScheduleOdResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceCloudbusScheduletaskodQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
