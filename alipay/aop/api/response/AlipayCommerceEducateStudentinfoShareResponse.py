#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduStudentInfoShareResult import EduStudentInfoShareResult


class AlipayCommerceEducateStudentinfoShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateStudentinfoShareResponse, self).__init__()
        self._student_info_share_result = None

    @property
    def student_info_share_result(self):
        return self._student_info_share_result

    @student_info_share_result.setter
    def student_info_share_result(self, value):
        if isinstance(value, EduStudentInfoShareResult):
            self._student_info_share_result = value
        else:
            self._student_info_share_result = EduStudentInfoShareResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateStudentinfoShareResponse, self).parse_response_content(response_content)
        if 'student_info_share_result' in response:
            self.student_info_share_result = response['student_info_share_result']
