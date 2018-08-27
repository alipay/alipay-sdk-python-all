#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppDeveloperCheckdevelopervalidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppDeveloperCheckdevelopervalidQueryResponse, self).__init__()
        self._dev_valid = None

    @property
    def dev_valid(self):
        return self._dev_valid

    @dev_valid.setter
    def dev_valid(self, value):
        self._dev_valid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppDeveloperCheckdevelopervalidQueryResponse, self).parse_response_content(response_content)
        if 'dev_valid' in response:
            self.dev_valid = response['dev_valid']
