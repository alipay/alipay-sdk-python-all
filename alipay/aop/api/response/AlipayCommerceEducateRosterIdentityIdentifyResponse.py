#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateRosterIdentityIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRosterIdentityIdentifyResponse, self).__init__()
        self._isv_msg = None

    @property
    def isv_msg(self):
        return self._isv_msg

    @isv_msg.setter
    def isv_msg(self, value):
        self._isv_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRosterIdentityIdentifyResponse, self).parse_response_content(response_content)
        if 'isv_msg' in response:
            self.isv_msg = response['isv_msg']
