#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MedicalGuideChatContentDTO import MedicalGuideChatContentDTO


class AlipayCommerceMedicalIndustrydataIntelligentdiagnosisSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataIntelligentdiagnosisSendResponse, self).__init__()
        self._chat_content = None
        self._result_code = None
        self._result_desc = None

    @property
    def chat_content(self):
        return self._chat_content

    @chat_content.setter
    def chat_content(self, value):
        if isinstance(value, MedicalGuideChatContentDTO):
            self._chat_content = value
        else:
            self._chat_content = MedicalGuideChatContentDTO.from_alipay_dict(value)
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
        response = super(AlipayCommerceMedicalIndustrydataIntelligentdiagnosisSendResponse, self).parse_response_content(response_content)
        if 'chat_content' in response:
            self.chat_content = response['chat_content']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
