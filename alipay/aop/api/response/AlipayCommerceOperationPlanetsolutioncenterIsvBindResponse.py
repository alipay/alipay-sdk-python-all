#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationPlanetsolutioncenterIsvBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPlanetsolutioncenterIsvBindResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPlanetsolutioncenterIsvBindResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
