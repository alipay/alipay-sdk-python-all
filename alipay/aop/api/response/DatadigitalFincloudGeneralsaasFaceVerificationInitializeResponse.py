#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasFaceVerificationInitializeResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasFaceVerificationInitializeResponse, self).__init__()
        self._certify_id = None
        self._page_url = None
        self._web_url = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value
    @property
    def web_url(self):
        return self._web_url

    @web_url.setter
    def web_url(self, value):
        self._web_url = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasFaceVerificationInitializeResponse, self).parse_response_content(response_content)
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'page_url' in response:
            self.page_url = response['page_url']
        if 'web_url' in response:
            self.web_url = response['web_url']
