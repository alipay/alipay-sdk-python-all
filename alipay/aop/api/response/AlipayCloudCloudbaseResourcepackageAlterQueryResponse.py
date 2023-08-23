#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResourcePackageInfo import ResourcePackageInfo


class AlipayCloudCloudbaseResourcepackageAlterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageAlterQueryResponse, self).__init__()
        self._current_spec_code = None
        self._resource_pkgs = None

    @property
    def current_spec_code(self):
        return self._current_spec_code

    @current_spec_code.setter
    def current_spec_code(self, value):
        self._current_spec_code = value
    @property
    def resource_pkgs(self):
        return self._resource_pkgs

    @resource_pkgs.setter
    def resource_pkgs(self, value):
        if isinstance(value, list):
            self._resource_pkgs = list()
            for i in value:
                if isinstance(i, ResourcePackageInfo):
                    self._resource_pkgs.append(i)
                else:
                    self._resource_pkgs.append(ResourcePackageInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageAlterQueryResponse, self).parse_response_content(response_content)
        if 'current_spec_code' in response:
            self.current_spec_code = response['current_spec_code']
        if 'resource_pkgs' in response:
            self.resource_pkgs = response['resource_pkgs']
