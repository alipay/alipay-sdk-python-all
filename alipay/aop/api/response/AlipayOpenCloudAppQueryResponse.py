#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenCloudAppQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenCloudAppQueryResponse, self).__init__()
        self._cloud_call_status = None

    @property
    def cloud_call_status(self):
        return self._cloud_call_status

    @cloud_call_status.setter
    def cloud_call_status(self, value):
        self._cloud_call_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenCloudAppQueryResponse, self).parse_response_content(response_content)
        if 'cloud_call_status' in response:
            self.cloud_call_status = response['cloud_call_status']
