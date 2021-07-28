#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateStudentIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateStudentIdentityQueryResponse, self).__init__()
        self._college_name = None
        self._college_online_tag = None

    @property
    def college_name(self):
        return self._college_name

    @college_name.setter
    def college_name(self, value):
        self._college_name = value
    @property
    def college_online_tag(self):
        return self._college_online_tag

    @college_online_tag.setter
    def college_online_tag(self, value):
        self._college_online_tag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateStudentIdentityQueryResponse, self).parse_response_content(response_content)
        if 'college_name' in response:
            self.college_name = response['college_name']
        if 'college_online_tag' in response:
            self.college_online_tag = response['college_online_tag']
