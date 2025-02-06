#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCommunityDeliveryrecentorderDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCommunityDeliveryrecentorderDetectResponse, self).__init__()
        self._delivery_platform = None
        self._delivery_type = None
        self._detect_result = None

    @property
    def delivery_platform(self):
        return self._delivery_platform

    @delivery_platform.setter
    def delivery_platform(self, value):
        self._delivery_platform = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def detect_result(self):
        return self._detect_result

    @detect_result.setter
    def detect_result(self, value):
        self._detect_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCommunityDeliveryrecentorderDetectResponse, self).parse_response_content(response_content)
        if 'delivery_platform' in response:
            self.delivery_platform = response['delivery_platform']
        if 'delivery_type' in response:
            self.delivery_type = response['delivery_type']
        if 'detect_result' in response:
            self.detect_result = response['detect_result']
