#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSceneTokenApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneTokenApplyResponse, self).__init__()
        self._app_token = None

    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneTokenApplyResponse, self).parse_response_content(response_content)
        if 'app_token' in response:
            self.app_token = response['app_token']
