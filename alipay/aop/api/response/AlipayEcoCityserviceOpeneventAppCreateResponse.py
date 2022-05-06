#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCityserviceOpeneventAppCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceOpeneventAppCreateResponse, self).__init__()
        self._app_code = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceOpeneventAppCreateResponse, self).parse_response_content(response_content)
        if 'app_code' in response:
            self.app_code = response['app_code']
