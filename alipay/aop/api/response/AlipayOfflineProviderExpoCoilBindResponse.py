#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderExpoCoilBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderExpoCoilBindResponse, self).__init__()
        self._tag_id = None

    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderExpoCoilBindResponse, self).parse_response_content(response_content)
        if 'tag_id' in response:
            self.tag_id = response['tag_id']
