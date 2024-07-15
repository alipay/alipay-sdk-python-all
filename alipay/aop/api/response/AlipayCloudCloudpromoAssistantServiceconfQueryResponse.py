#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceConfig import ServiceConfig


class AlipayCloudCloudpromoAssistantServiceconfQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAssistantServiceconfQueryResponse, self).__init__()
        self._service_configs = None

    @property
    def service_configs(self):
        return self._service_configs

    @service_configs.setter
    def service_configs(self, value):
        if isinstance(value, list):
            self._service_configs = list()
            for i in value:
                if isinstance(i, ServiceConfig):
                    self._service_configs.append(i)
                else:
                    self._service_configs.append(ServiceConfig.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAssistantServiceconfQueryResponse, self).parse_response_content(response_content)
        if 'service_configs' in response:
            self.service_configs = response['service_configs']
