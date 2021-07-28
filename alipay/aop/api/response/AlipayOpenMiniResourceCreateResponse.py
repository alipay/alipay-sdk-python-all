#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniResourceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniResourceCreateResponse, self).__init__()
        self._resource_id = None

    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniResourceCreateResponse, self).parse_response_content(response_content)
        if 'resource_id' in response:
            self.resource_id = response['resource_id']
