#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCommonRelationSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonRelationSetResponse, self).__init__()
        self._operation_result = None
        self._operation_time = None

    @property
    def operation_result(self):
        return self._operation_result

    @operation_result.setter
    def operation_result(self, value):
        self._operation_result = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonRelationSetResponse, self).parse_response_content(response_content)
        if 'operation_result' in response:
            self.operation_result = response['operation_result']
        if 'operation_time' in response:
            self.operation_time = response['operation_time']
