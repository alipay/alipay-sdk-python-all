#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationTagClaimAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTagClaimAddResponse, self).__init__()
        self._success_count = None

    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTagClaimAddResponse, self).parse_response_content(response_content)
        if 'success_count' in response:
            self.success_count = response['success_count']
