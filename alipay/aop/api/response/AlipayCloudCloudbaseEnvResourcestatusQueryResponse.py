#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResourceStatus import ResourceStatus


class AlipayCloudCloudbaseEnvResourcestatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseEnvResourcestatusQueryResponse, self).__init__()
        self._resources = None

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if isinstance(value, list):
            self._resources = list()
            for i in value:
                if isinstance(i, ResourceStatus):
                    self._resources.append(i)
                else:
                    self._resources.append(ResourceStatus.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseEnvResourcestatusQueryResponse, self).parse_response_content(response_content)
        if 'resources' in response:
            self.resources = response['resources']
