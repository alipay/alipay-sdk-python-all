#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LlmServiceDTO import LlmServiceDTO


class AlipayCommerceMedicalLargermodelSessionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelSessionQueryResponse, self).__init__()
        self._llm_service_result = None
        self._result_code = None
        self._result_desc = None

    @property
    def llm_service_result(self):
        return self._llm_service_result

    @llm_service_result.setter
    def llm_service_result(self, value):
        if isinstance(value, LlmServiceDTO):
            self._llm_service_result = value
        else:
            self._llm_service_result = LlmServiceDTO.from_alipay_dict(value)
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
        response = super(AlipayCommerceMedicalLargermodelSessionQueryResponse, self).parse_response_content(response_content)
        if 'llm_service_result' in response:
            self.llm_service_result = response['llm_service_result']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
