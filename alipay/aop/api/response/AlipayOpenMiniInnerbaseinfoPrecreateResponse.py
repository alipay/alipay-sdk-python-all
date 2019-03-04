#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerbaseinfoPrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerbaseinfoPrecreateResponse, self).__init__()
        self._mini_app_id = None

    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerbaseinfoPrecreateResponse, self).parse_response_content(response_content)
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
