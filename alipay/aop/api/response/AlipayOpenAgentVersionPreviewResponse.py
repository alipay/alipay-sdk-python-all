#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentVersionPreviewResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentVersionPreviewResponse, self).__init__()
        self._preview_url = None

    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentVersionPreviewResponse, self).parse_response_content(response_content)
        if 'preview_url' in response:
            self.preview_url = response['preview_url']
