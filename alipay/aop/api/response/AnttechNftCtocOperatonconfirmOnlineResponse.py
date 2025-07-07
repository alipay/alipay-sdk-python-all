#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftCtocOperatonconfirmOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocOperatonconfirmOnlineResponse, self).__init__()
        self._verify_confirm_id = None

    @property
    def verify_confirm_id(self):
        return self._verify_confirm_id

    @verify_confirm_id.setter
    def verify_confirm_id(self, value):
        self._verify_confirm_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocOperatonconfirmOnlineResponse, self).parse_response_content(response_content)
        if 'verify_confirm_id' in response:
            self.verify_confirm_id = response['verify_confirm_id']
