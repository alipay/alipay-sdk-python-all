#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCourseCheckincodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCourseCheckincodeCreateResponse, self).__init__()
        self._course_rule_id = None

    @property
    def course_rule_id(self):
        return self._course_rule_id

    @course_rule_id.setter
    def course_rule_id(self, value):
        self._course_rule_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCourseCheckincodeCreateResponse, self).parse_response_content(response_content)
        if 'course_rule_id' in response:
            self.course_rule_id = response['course_rule_id']
