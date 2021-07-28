#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataservicePropertyBusinesspropertyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataservicePropertyBusinesspropertyCreateResponse, self).__init__()
        self._business_property_id = None

    @property
    def business_property_id(self):
        return self._business_property_id

    @business_property_id.setter
    def business_property_id(self, value):
        self._business_property_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataservicePropertyBusinesspropertyCreateResponse, self).parse_response_content(response_content)
        if 'business_property_id' in response:
            self.business_property_id = response['business_property_id']
