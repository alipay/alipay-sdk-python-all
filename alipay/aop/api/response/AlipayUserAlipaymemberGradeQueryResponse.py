#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAlipaymemberGradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAlipaymemberGradeQueryResponse, self).__init__()
        self._grade = None

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAlipaymemberGradeQueryResponse, self).parse_response_content(response_content)
        if 'grade' in response:
            self.grade = response['grade']
