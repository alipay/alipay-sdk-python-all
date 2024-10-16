#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgentWelcomeCardDTO import AgentWelcomeCardDTO


class AlipayCommerceMedicalLargermodelAgentwelcomecardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelAgentwelcomecardQueryResponse, self).__init__()
        self._data = None
        self._result_code = None
        self._result_desc = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, AgentWelcomeCardDTO):
            self._data = value
        else:
            self._data = AgentWelcomeCardDTO.from_alipay_dict(value)
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelAgentwelcomecardQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
