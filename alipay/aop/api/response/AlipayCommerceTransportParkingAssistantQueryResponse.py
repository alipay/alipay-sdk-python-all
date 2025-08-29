#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportParkingAssistantQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportParkingAssistantQueryResponse, self).__init__()
        self._assistant_service_status = None

    @property
    def assistant_service_status(self):
        return self._assistant_service_status

    @assistant_service_status.setter
    def assistant_service_status(self, value):
        self._assistant_service_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportParkingAssistantQueryResponse, self).parse_response_content(response_content)
        if 'assistant_service_status' in response:
            self.assistant_service_status = response['assistant_service_status']
