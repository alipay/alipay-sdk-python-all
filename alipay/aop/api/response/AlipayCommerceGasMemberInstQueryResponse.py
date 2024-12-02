#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceGasMemberInstQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceGasMemberInstQueryResponse, self).__init__()
        self._member_no = None

    @property
    def member_no(self):
        return self._member_no

    @member_no.setter
    def member_no(self, value):
        self._member_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceGasMemberInstQueryResponse, self).parse_response_content(response_content)
        if 'member_no' in response:
            self.member_no = response['member_no']
