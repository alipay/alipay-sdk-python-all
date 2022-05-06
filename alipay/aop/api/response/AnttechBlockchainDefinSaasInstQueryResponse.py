#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinSaasInstQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinSaasInstQueryResponse, self).__init__()
        self._channel_member_code = None
        self._channel_official_number = None

    @property
    def channel_member_code(self):
        return self._channel_member_code

    @channel_member_code.setter
    def channel_member_code(self, value):
        self._channel_member_code = value
    @property
    def channel_official_number(self):
        return self._channel_official_number

    @channel_official_number.setter
    def channel_official_number(self, value):
        self._channel_official_number = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinSaasInstQueryResponse, self).parse_response_content(response_content)
        if 'channel_member_code' in response:
            self.channel_member_code = response['channel_member_code']
        if 'channel_official_number' in response:
            self.channel_official_number = response['channel_official_number']
