#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceOrderCreateResponse, self).__init__()
        self._flow_id = None
        self._result = None

    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceOrderCreateResponse, self).parse_response_content(response_content)
        if 'flow_id' in response:
            self.flow_id = response['flow_id']
        if 'result' in response:
            self.result = response['result']
