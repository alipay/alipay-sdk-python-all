#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceKidsAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceKidsAccountCreateResponse, self).__init__()
        self._child_id = None

    @property
    def child_id(self):
        return self._child_id

    @child_id.setter
    def child_id(self, value):
        self._child_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceKidsAccountCreateResponse, self).parse_response_content(response_content)
        if 'child_id' in response:
            self.child_id = response['child_id']
