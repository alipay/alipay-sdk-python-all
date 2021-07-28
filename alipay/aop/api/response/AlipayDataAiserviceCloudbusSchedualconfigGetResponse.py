#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ScheduleConfigGetResult import ScheduleConfigGetResult


class AlipayDataAiserviceCloudbusSchedualconfigGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceCloudbusSchedualconfigGetResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ScheduleConfigGetResult):
            self._result = value
        else:
            self._result = ScheduleConfigGetResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceCloudbusSchedualconfigGetResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
