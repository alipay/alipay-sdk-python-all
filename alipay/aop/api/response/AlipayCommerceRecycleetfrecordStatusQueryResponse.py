#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleetfrecordStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleetfrecordStatusQueryResponse, self).__init__()
        self._apply_status = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleetfrecordStatusQueryResponse, self).parse_response_content(response_content)
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
