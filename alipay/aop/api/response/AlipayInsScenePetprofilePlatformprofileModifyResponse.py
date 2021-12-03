#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsScenePetprofilePlatformprofileModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePetprofilePlatformprofileModifyResponse, self).__init__()
        self._change_result = None

    @property
    def change_result(self):
        return self._change_result

    @change_result.setter
    def change_result(self, value):
        self._change_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePetprofilePlatformprofileModifyResponse, self).parse_response_content(response_content)
        if 'change_result' in response:
            self.change_result = response['change_result']
