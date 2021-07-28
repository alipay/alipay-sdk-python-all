#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HomeApiResponse import HomeApiResponse


class AlipayIserviceItaskOrderRecordSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceItaskOrderRecordSyncResponse, self).__init__()
        self._home_api_response = None

    @property
    def home_api_response(self):
        return self._home_api_response

    @home_api_response.setter
    def home_api_response(self, value):
        if isinstance(value, HomeApiResponse):
            self._home_api_response = value
        else:
            self._home_api_response = HomeApiResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceItaskOrderRecordSyncResponse, self).parse_response_content(response_content)
        if 'home_api_response' in response:
            self.home_api_response = response['home_api_response']
