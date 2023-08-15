#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Config import Config


class AlipayCloudCloudbaseFunctionConfigGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionConfigGetResponse, self).__init__()
        self._config = None
        self._function_name = None

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        if isinstance(value, Config):
            self._config = value
        else:
            self._config = Config.from_alipay_dict(value)
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionConfigGetResponse, self).parse_response_content(response_content)
        if 'config' in response:
            self.config = response['config']
        if 'function_name' in response:
            self.function_name = response['function_name']
