#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResourcePackageInfo import ResourcePackageInfo


class AlipayCloudCloudbaseResourcepackageOpenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageOpenQueryResponse, self).__init__()
        self._resource_packages = None

    @property
    def resource_packages(self):
        return self._resource_packages

    @resource_packages.setter
    def resource_packages(self, value):
        if isinstance(value, list):
            self._resource_packages = list()
            for i in value:
                if isinstance(i, ResourcePackageInfo):
                    self._resource_packages.append(i)
                else:
                    self._resource_packages.append(ResourcePackageInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageOpenQueryResponse, self).parse_response_content(response_content)
        if 'resource_packages' in response:
            self.resource_packages = response['resource_packages']
