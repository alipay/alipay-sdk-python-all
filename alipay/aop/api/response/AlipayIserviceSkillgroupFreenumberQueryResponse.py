#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ListAgentAccountStatesFacadeResponse import ListAgentAccountStatesFacadeResponse


class AlipayIserviceSkillgroupFreenumberQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceSkillgroupFreenumberQueryResponse, self).__init__()
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, ListAgentAccountStatesFacadeResponse):
            self._value = value
        else:
            self._value = ListAgentAccountStatesFacadeResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceSkillgroupFreenumberQueryResponse, self).parse_response_content(response_content)
        if 'value' in response:
            self.value = response['value']
