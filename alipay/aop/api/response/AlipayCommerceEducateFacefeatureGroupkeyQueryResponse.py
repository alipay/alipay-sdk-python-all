#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateFacefeatureGroupkeyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateFacefeatureGroupkeyQueryResponse, self).__init__()
        self._group_key = None

    @property
    def group_key(self):
        return self._group_key

    @group_key.setter
    def group_key(self, value):
        self._group_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateFacefeatureGroupkeyQueryResponse, self).parse_response_content(response_content)
        if 'group_key' in response:
            self.group_key = response['group_key']
