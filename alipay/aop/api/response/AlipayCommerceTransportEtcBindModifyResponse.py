#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcBindModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcBindModifyResponse, self).__init__()
        self._update_result = None

    @property
    def update_result(self):
        return self._update_result

    @update_result.setter
    def update_result(self, value):
        self._update_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcBindModifyResponse, self).parse_response_content(response_content)
        if 'update_result' in response:
            self.update_result = response['update_result']
