#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinCustomerMemberCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinCustomerMemberCreateResponse, self).__init__()
        self._member_id = None

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinCustomerMemberCreateResponse, self).parse_response_content(response_content)
        if 'member_id' in response:
            self.member_id = response['member_id']
