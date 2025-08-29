#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseGatewayDomainModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseGatewayDomainModifyResponse, self).__init__()
        self._operation_info = None

    @property
    def operation_info(self):
        return self._operation_info

    @operation_info.setter
    def operation_info(self, value):
        self._operation_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseGatewayDomainModifyResponse, self).parse_response_content(response_content)
        if 'operation_info' in response:
            self.operation_info = response['operation_info']
