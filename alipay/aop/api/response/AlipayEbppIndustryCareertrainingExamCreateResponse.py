#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCareertrainingExamCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingExamCreateResponse, self).__init__()
        self._exam_id = None

    @property
    def exam_id(self):
        return self._exam_id

    @exam_id.setter
    def exam_id(self, value):
        self._exam_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingExamCreateResponse, self).parse_response_content(response_content)
        if 'exam_id' in response:
            self.exam_id = response['exam_id']
