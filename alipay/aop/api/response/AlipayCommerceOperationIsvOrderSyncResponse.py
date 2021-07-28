#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationIsvOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationIsvOrderSyncResponse, self).__init__()
        self._record_id = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationIsvOrderSyncResponse, self).parse_response_content(response_content)
        if 'record_id' in response:
            self.record_id = response['record_id']
