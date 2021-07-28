#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiResolutionMethod import OpenApiResolutionMethod
from alipay.aop.api.domain.OpenApiResponseHeader import OpenApiResponseHeader


class AlipayUserApplepayOtpresolutionmethodsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserApplepayOtpresolutionmethodsQueryResponse, self).__init__()
        self._resolution_methods = None
        self._response_header = None

    @property
    def resolution_methods(self):
        return self._resolution_methods

    @resolution_methods.setter
    def resolution_methods(self, value):
        if isinstance(value, OpenApiResolutionMethod):
            self._resolution_methods = value
        else:
            self._resolution_methods = OpenApiResolutionMethod.from_alipay_dict(value)
    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, OpenApiResponseHeader):
            self._response_header = value
        else:
            self._response_header = OpenApiResponseHeader.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserApplepayOtpresolutionmethodsQueryResponse, self).parse_response_content(response_content)
        if 'resolution_methods' in response:
            self.resolution_methods = response['resolution_methods']
        if 'response_header' in response:
            self.response_header = response['response_header']
