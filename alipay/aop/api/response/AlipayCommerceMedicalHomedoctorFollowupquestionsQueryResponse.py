#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuestionInfoOpenapiResponse import QuestionInfoOpenapiResponse


class AlipayCommerceMedicalHomedoctorFollowupquestionsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHomedoctorFollowupquestionsQueryResponse, self).__init__()
        self._question_list = None

    @property
    def question_list(self):
        return self._question_list

    @question_list.setter
    def question_list(self, value):
        if isinstance(value, list):
            self._question_list = list()
            for i in value:
                if isinstance(i, QuestionInfoOpenapiResponse):
                    self._question_list.append(i)
                else:
                    self._question_list.append(QuestionInfoOpenapiResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHomedoctorFollowupquestionsQueryResponse, self).parse_response_content(response_content)
        if 'question_list' in response:
            self.question_list = response['question_list']
