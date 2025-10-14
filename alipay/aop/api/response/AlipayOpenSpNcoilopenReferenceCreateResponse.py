#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNcoilopenReferenceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNcoilopenReferenceCreateResponse, self).__init__()
        self._reference_id = None

    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNcoilopenReferenceCreateResponse, self).parse_response_content(response_content)
        if 'reference_id' in response:
            self.reference_id = response['reference_id']
