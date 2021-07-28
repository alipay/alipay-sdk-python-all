#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateFacefeatureInfoSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateFacefeatureInfoSendResponse, self).__init__()
        self._error_uids = None

    @property
    def error_uids(self):
        return self._error_uids

    @error_uids.setter
    def error_uids(self, value):
        self._error_uids = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateFacefeatureInfoSendResponse, self).parse_response_content(response_content)
        if 'error_uids' in response:
            self.error_uids = response['error_uids']
