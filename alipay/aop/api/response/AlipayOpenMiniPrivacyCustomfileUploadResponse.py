#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniPrivacyCustomfileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPrivacyCustomfileUploadResponse, self).__init__()
        self._user_custom_file = None

    @property
    def user_custom_file(self):
        return self._user_custom_file

    @user_custom_file.setter
    def user_custom_file(self, value):
        self._user_custom_file = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPrivacyCustomfileUploadResponse, self).parse_response_content(response_content)
        if 'user_custom_file' in response:
            self.user_custom_file = response['user_custom_file']
