#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenDataItemSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenDataItemSyncResponse, self).__init__()
        self._external_id = None

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenDataItemSyncResponse, self).parse_response_content(response_content)
        if 'external_id' in response:
            self.external_id = response['external_id']
