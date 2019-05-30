#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneCommandReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommandReceiveResponse, self).__init__()
        self._result_object_string = None

    @property
    def result_object_string(self):
        return self._result_object_string

    @result_object_string.setter
    def result_object_string(self, value):
        self._result_object_string = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommandReceiveResponse, self).parse_response_content(response_content)
        if 'result_object_string' in response:
            self.result_object_string = response['result_object_string']
