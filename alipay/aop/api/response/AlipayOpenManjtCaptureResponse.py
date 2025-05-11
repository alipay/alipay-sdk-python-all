#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResponseObjManjiangTest import ResponseObjManjiangTest


class AlipayOpenManjtCaptureResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenManjtCaptureResponse, self).__init__()
        self._response_obj = None
        self._test_plain_field = None

    @property
    def response_obj(self):
        return self._response_obj

    @response_obj.setter
    def response_obj(self, value):
        if isinstance(value, ResponseObjManjiangTest):
            self._response_obj = value
        else:
            self._response_obj = ResponseObjManjiangTest.from_alipay_dict(value)
    @property
    def test_plain_field(self):
        return self._test_plain_field

    @test_plain_field.setter
    def test_plain_field(self, value):
        if isinstance(value, list):
            self._test_plain_field = list()
            for i in value:
                self._test_plain_field.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenManjtCaptureResponse, self).parse_response_content(response_content)
        if 'response_obj' in response:
            self.response_obj = response['response_obj']
        if 'test_plain_field' in response:
            self.test_plain_field = response['test_plain_field']
