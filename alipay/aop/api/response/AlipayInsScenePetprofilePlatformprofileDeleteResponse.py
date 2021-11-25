#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsScenePetprofilePlatformprofileDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePetprofilePlatformprofileDeleteResponse, self).__init__()
        self._delete_result = None

    @property
    def delete_result(self):
        return self._delete_result

    @delete_result.setter
    def delete_result(self, value):
        self._delete_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePetprofilePlatformprofileDeleteResponse, self).parse_response_content(response_content)
        if 'delete_result' in response:
            self.delete_result = response['delete_result']
