#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateTrainCourseCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateTrainCourseCreateResponse, self).__init__()
        self._course_id = None

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateTrainCourseCreateResponse, self).parse_response_content(response_content)
        if 'course_id' in response:
            self.course_id = response['course_id']
