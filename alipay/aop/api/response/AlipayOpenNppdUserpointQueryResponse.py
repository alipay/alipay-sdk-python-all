#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenNppdUserpointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenNppdUserpointQueryResponse, self).__init__()
        self._grade = None
        self._point = None

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenNppdUserpointQueryResponse, self).parse_response_content(response_content)
        if 'grade' in response:
            self.grade = response['grade']
        if 'point' in response:
            self.point = response['point']
