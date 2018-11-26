#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportAdAduserqualificationCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdAduserqualificationCreateResponse, self).__init__()
        self._qualification_id = None

    @property
    def qualification_id(self):
        return self._qualification_id

    @qualification_id.setter
    def qualification_id(self, value):
        self._qualification_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdAduserqualificationCreateResponse, self).parse_response_content(response_content)
        if 'qualification_id' in response:
            self.qualification_id = response['qualification_id']
