#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LlmAnswerCardDTO import LlmAnswerCardDTO


class AlipayCommerceMedicalLargermodelDoctorcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelDoctorcardQueryResponse, self).__init__()
        self._llm_service_result = None

    @property
    def llm_service_result(self):
        return self._llm_service_result

    @llm_service_result.setter
    def llm_service_result(self, value):
        if isinstance(value, list):
            self._llm_service_result = list()
            for i in value:
                if isinstance(i, LlmAnswerCardDTO):
                    self._llm_service_result.append(i)
                else:
                    self._llm_service_result.append(LlmAnswerCardDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelDoctorcardQueryResponse, self).parse_response_content(response_content)
        if 'llm_service_result' in response:
            self.llm_service_result = response['llm_service_result']
