#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerVersionproportionsetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerVersionproportionsetQueryResponse, self).__init__()
        self._mini_appx_version = None

    @property
    def mini_appx_version(self):
        return self._mini_appx_version

    @mini_appx_version.setter
    def mini_appx_version(self, value):
        self._mini_appx_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerVersionproportionsetQueryResponse, self).parse_response_content(response_content)
        if 'mini_appx_version' in response:
            self.mini_appx_version = response['mini_appx_version']
