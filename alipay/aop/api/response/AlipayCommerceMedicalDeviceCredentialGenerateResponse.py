#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceIdentityCredentialOpenApiGenerateResult import DeviceIdentityCredentialOpenApiGenerateResult


class AlipayCommerceMedicalDeviceCredentialGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDeviceCredentialGenerateResponse, self).__init__()
        self._remaining_quota = None
        self._results = None

    @property
    def remaining_quota(self):
        return self._remaining_quota

    @remaining_quota.setter
    def remaining_quota(self, value):
        self._remaining_quota = value
    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        if isinstance(value, list):
            self._results = list()
            for i in value:
                if isinstance(i, DeviceIdentityCredentialOpenApiGenerateResult):
                    self._results.append(i)
                else:
                    self._results.append(DeviceIdentityCredentialOpenApiGenerateResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDeviceCredentialGenerateResponse, self).parse_response_content(response_content)
        if 'remaining_quota' in response:
            self.remaining_quota = response['remaining_quota']
        if 'results' in response:
            self.results = response['results']
