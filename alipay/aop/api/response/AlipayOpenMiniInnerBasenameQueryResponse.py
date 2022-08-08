#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerBasenameQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerBasenameQueryResponse, self).__init__()
        self._app_name = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerBasenameQueryResponse, self).parse_response_content(response_content)
        if 'app_name' in response:
            self.app_name = response['app_name']
