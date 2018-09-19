#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SecuritydataMobileCity import SecuritydataMobileCity


class AlipaySecurityDataInfoMobilecityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataInfoMobilecityQueryResponse, self).__init__()
        self._mobile_city = None

    @property
    def mobile_city(self):
        return self._mobile_city

    @mobile_city.setter
    def mobile_city(self, value):
        if isinstance(value, SecuritydataMobileCity):
            self._mobile_city = value
        else:
            self._mobile_city = SecuritydataMobileCity.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataInfoMobilecityQueryResponse, self).parse_response_content(response_content)
        if 'mobile_city' in response:
            self.mobile_city = response['mobile_city']
