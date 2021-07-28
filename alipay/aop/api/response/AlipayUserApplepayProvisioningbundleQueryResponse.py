#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiProvisioningBundle import OpenApiProvisioningBundle
from alipay.aop.api.domain.OpenApiResponseHeader import OpenApiResponseHeader


class AlipayUserApplepayProvisioningbundleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserApplepayProvisioningbundleQueryResponse, self).__init__()
        self._pass_state = None
        self._provisioning_bundle = None
        self._response_header = None

    @property
    def pass_state(self):
        return self._pass_state

    @pass_state.setter
    def pass_state(self, value):
        self._pass_state = value
    @property
    def provisioning_bundle(self):
        return self._provisioning_bundle

    @provisioning_bundle.setter
    def provisioning_bundle(self, value):
        if isinstance(value, OpenApiProvisioningBundle):
            self._provisioning_bundle = value
        else:
            self._provisioning_bundle = OpenApiProvisioningBundle.from_alipay_dict(value)
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
        response = super(AlipayUserApplepayProvisioningbundleQueryResponse, self).parse_response_content(response_content)
        if 'pass_state' in response:
            self.pass_state = response['pass_state']
        if 'provisioning_bundle' in response:
            self.provisioning_bundle = response['provisioning_bundle']
        if 'response_header' in response:
            self.response_header = response['response_header']
