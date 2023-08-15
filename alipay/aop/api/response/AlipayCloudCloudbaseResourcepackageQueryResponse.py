#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResourcePackage import ResourcePackage


class AlipayCloudCloudbaseResourcepackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageQueryResponse, self).__init__()
        self._page_index = None
        self._page_size = None
        self._resource_packages = None
        self._total = None

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def resource_packages(self):
        return self._resource_packages

    @resource_packages.setter
    def resource_packages(self, value):
        if isinstance(value, list):
            self._resource_packages = list()
            for i in value:
                if isinstance(i, ResourcePackage):
                    self._resource_packages.append(i)
                else:
                    self._resource_packages.append(ResourcePackage.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageQueryResponse, self).parse_response_content(response_content)
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'resource_packages' in response:
            self.resource_packages = response['resource_packages']
        if 'total' in response:
            self.total = response['total']
