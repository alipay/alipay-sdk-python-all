#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSemesterInfoSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSemesterInfoSaveResponse, self).__init__()
        self._semester_id = None

    @property
    def semester_id(self):
        return self._semester_id

    @semester_id.setter
    def semester_id(self, value):
        self._semester_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSemesterInfoSaveResponse, self).parse_response_content(response_content)
        if 'semester_id' in response:
            self.semester_id = response['semester_id']
