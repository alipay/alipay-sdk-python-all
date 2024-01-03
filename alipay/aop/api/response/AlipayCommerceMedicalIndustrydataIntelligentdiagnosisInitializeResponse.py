#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MedicalGuideChatInitDTO import MedicalGuideChatInitDTO


class AlipayCommerceMedicalIndustrydataIntelligentdiagnosisInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataIntelligentdiagnosisInitializeResponse, self).__init__()
        self._chat_init_result = None
        self._result_code = None
        self._result_desc = None

    @property
    def chat_init_result(self):
        return self._chat_init_result

    @chat_init_result.setter
    def chat_init_result(self, value):
        if isinstance(value, MedicalGuideChatInitDTO):
            self._chat_init_result = value
        else:
            self._chat_init_result = MedicalGuideChatInitDTO.from_alipay_dict(value)
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
        response = super(AlipayCommerceMedicalIndustrydataIntelligentdiagnosisInitializeResponse, self).parse_response_content(response_content)
        if 'chat_init_result' in response:
            self.chat_init_result = response['chat_init_result']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
