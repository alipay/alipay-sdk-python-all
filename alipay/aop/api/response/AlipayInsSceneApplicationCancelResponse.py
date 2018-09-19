#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneApplicationCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneApplicationCancelResponse, self).__init__()
        self._application_no = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneApplicationCancelResponse, self).parse_response_content(response_content)
        if 'application_no' in response:
            self.application_no = response['application_no']
