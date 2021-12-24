#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateAnswerDTO import TemplateAnswerDTO


class AlipayFincoreComplianceTemplateAnswerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateAnswerQueryResponse, self).__init__()
        self._answers = None

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, value):
        if isinstance(value, list):
            self._answers = list()
            for i in value:
                if isinstance(i, TemplateAnswerDTO):
                    self._answers.append(i)
                else:
                    self._answers.append(TemplateAnswerDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateAnswerQueryResponse, self).parse_response_content(response_content)
        if 'answers' in response:
            self.answers = response['answers']
