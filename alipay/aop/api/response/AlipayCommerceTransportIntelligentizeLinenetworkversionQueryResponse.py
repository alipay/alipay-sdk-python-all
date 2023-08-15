#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportIntelligentizeLinenetworkversionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIntelligentizeLinenetworkversionQueryResponse, self).__init__()
        self._ext_info = None
        self._linenet_version = None
        self._source = None
        self._version_time = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def linenet_version(self):
        return self._linenet_version

    @linenet_version.setter
    def linenet_version(self, value):
        self._linenet_version = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def version_time(self):
        return self._version_time

    @version_time.setter
    def version_time(self, value):
        self._version_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIntelligentizeLinenetworkversionQueryResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'linenet_version' in response:
            self.linenet_version = response['linenet_version']
        if 'source' in response:
            self.source = response['source']
        if 'version_time' in response:
            self.version_time = response['version_time']
