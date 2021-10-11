#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainSignIndexCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainSignIndexCreateResponse, self).__init__()
        self._publish_success = None

    @property
    def publish_success(self):
        return self._publish_success

    @publish_success.setter
    def publish_success(self, value):
        self._publish_success = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainSignIndexCreateResponse, self).parse_response_content(response_content)
        if 'publish_success' in response:
            self.publish_success = response['publish_success']
