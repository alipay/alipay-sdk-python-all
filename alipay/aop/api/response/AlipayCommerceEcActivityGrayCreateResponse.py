#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcActivityGrayCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcActivityGrayCreateResponse, self).__init__()
        self._benefit_enterprise_invite_code = None

    @property
    def benefit_enterprise_invite_code(self):
        return self._benefit_enterprise_invite_code

    @benefit_enterprise_invite_code.setter
    def benefit_enterprise_invite_code(self, value):
        self._benefit_enterprise_invite_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcActivityGrayCreateResponse, self).parse_response_content(response_content)
        if 'benefit_enterprise_invite_code' in response:
            self.benefit_enterprise_invite_code = response['benefit_enterprise_invite_code']
