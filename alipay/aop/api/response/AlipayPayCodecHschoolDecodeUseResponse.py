#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayCodecHschoolDecodeUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayCodecHschoolDecodeUseResponse, self).__init__()
        self._feature_code = None
        self._health_status = None
        self._school_std_code = None
        self._student_no = None

    @property
    def feature_code(self):
        return self._feature_code

    @feature_code.setter
    def feature_code(self, value):
        self._feature_code = value
    @property
    def health_status(self):
        return self._health_status

    @health_status.setter
    def health_status(self, value):
        self._health_status = value
    @property
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value
    @property
    def student_no(self):
        return self._student_no

    @student_no.setter
    def student_no(self, value):
        self._student_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayCodecHschoolDecodeUseResponse, self).parse_response_content(response_content)
        if 'feature_code' in response:
            self.feature_code = response['feature_code']
        if 'health_status' in response:
            self.health_status = response['health_status']
        if 'school_std_code' in response:
            self.school_std_code = response['school_std_code']
        if 'student_no' in response:
            self.student_no = response['student_no']
