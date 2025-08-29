#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCareertrainingCourseSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingCourseSyncResponse, self).__init__()
        self._course_id = None
        self._course_status = None

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_status(self):
        return self._course_status

    @course_status.setter
    def course_status(self, value):
        self._course_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingCourseSyncResponse, self).parse_response_content(response_content)
        if 'course_id' in response:
            self.course_id = response['course_id']
        if 'course_status' in response:
            self.course_status = response['course_status']
