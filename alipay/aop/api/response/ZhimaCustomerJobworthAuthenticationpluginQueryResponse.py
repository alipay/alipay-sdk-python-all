#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthAuthenticationpluginQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthAuthenticationpluginQueryResponse, self).__init__()
        self._landing_url = None
        self._scheme_url = None

    @property
    def landing_url(self):
        return self._landing_url

    @landing_url.setter
    def landing_url(self, value):
        self._landing_url = value
    @property
    def scheme_url(self):
        return self._scheme_url

    @scheme_url.setter
    def scheme_url(self, value):
        self._scheme_url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthAuthenticationpluginQueryResponse, self).parse_response_content(response_content)
        if 'landing_url' in response:
            self.landing_url = response['landing_url']
        if 'scheme_url' in response:
            self.scheme_url = response['scheme_url']
