#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmIsvInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmIsvInitializeResponse, self).__init__()
        self._ccm_pub_key = None

    @property
    def ccm_pub_key(self):
        return self._ccm_pub_key

    @ccm_pub_key.setter
    def ccm_pub_key(self, value):
        self._ccm_pub_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmIsvInitializeResponse, self).parse_response_content(response_content)
        if 'ccm_pub_key' in response:
            self.ccm_pub_key = response['ccm_pub_key']
