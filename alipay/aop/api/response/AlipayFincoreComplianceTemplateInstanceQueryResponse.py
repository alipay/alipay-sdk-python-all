#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AnswerDTO import AnswerDTO
from alipay.aop.api.domain.TemplateInstDTO import TemplateInstDTO


class AlipayFincoreComplianceTemplateInstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateInstanceQueryResponse, self).__init__()
        self._answers = None
        self._status = None
        self._template_instances = None

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, value):
        if isinstance(value, AnswerDTO):
            self._answers = value
        else:
            self._answers = AnswerDTO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_instances(self):
        return self._template_instances

    @template_instances.setter
    def template_instances(self, value):
        if isinstance(value, TemplateInstDTO):
            self._template_instances = value
        else:
            self._template_instances = TemplateInstDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateInstanceQueryResponse, self).parse_response_content(response_content)
        if 'answers' in response:
            self.answers = response['answers']
        if 'status' in response:
            self.status = response['status']
        if 'template_instances' in response:
            self.template_instances = response['template_instances']
