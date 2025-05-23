#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsRightsorderDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsRightsorderDetailQueryResponse, self).__init__()
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsRightsorderDetailQueryResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
