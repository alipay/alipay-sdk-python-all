#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerbaseinfoApplogoUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerbaseinfoApplogoUploadResponse, self).__init__()
        self._app_logo = None

    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerbaseinfoApplogoUploadResponse, self).parse_response_content(response_content)
        if 'app_logo' in response:
            self.app_logo = response['app_logo']
