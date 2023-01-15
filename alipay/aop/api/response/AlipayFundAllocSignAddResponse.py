#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAllocSignAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAllocSignAddResponse, self).__init__()
        self._flow_id = None
        self._operation_url = None

    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def operation_url(self):
        return self._operation_url

    @operation_url.setter
    def operation_url(self, value):
        self._operation_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAllocSignAddResponse, self).parse_response_content(response_content)
        if 'flow_id' in response:
            self.flow_id = response['flow_id']
        if 'operation_url' in response:
            self.operation_url = response['operation_url']
