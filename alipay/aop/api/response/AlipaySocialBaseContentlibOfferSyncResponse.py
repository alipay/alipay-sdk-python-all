#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseContentlibOfferSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseContentlibOfferSyncResponse, self).__init__()
        self._content = None
        self._success = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseContentlibOfferSyncResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'success' in response:
            self.success = response['success']
