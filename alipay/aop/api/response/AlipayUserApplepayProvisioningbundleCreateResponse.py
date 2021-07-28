#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiResponseHeader import OpenApiResponseHeader


class AlipayUserApplepayProvisioningbundleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserApplepayProvisioningbundleCreateResponse, self).__init__()
        self._provisioning_bundle_identifier = None
        self._response_header = None

    @property
    def provisioning_bundle_identifier(self):
        return self._provisioning_bundle_identifier

    @provisioning_bundle_identifier.setter
    def provisioning_bundle_identifier(self, value):
        self._provisioning_bundle_identifier = value
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
        response = super(AlipayUserApplepayProvisioningbundleCreateResponse, self).parse_response_content(response_content)
        if 'provisioning_bundle_identifier' in response:
            self.provisioning_bundle_identifier = response['provisioning_bundle_identifier']
        if 'response_header' in response:
            self.response_header = response['response_header']
