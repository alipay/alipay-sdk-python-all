#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSchoolserviceModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSchoolserviceModifyResponse, self).__init__()
        self._service_id = None

    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSchoolserviceModifyResponse, self).parse_response_content(response_content)
        if 'service_id' in response:
            self.service_id = response['service_id']
