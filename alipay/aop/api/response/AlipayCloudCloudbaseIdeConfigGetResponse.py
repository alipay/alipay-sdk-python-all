#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GatewayConfig import GatewayConfig


class AlipayCloudCloudbaseIdeConfigGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseIdeConfigGetResponse, self).__init__()
        self._access_key = None
        self._gateway_configs = None
        self._secret_key = None

    @property
    def access_key(self):
        return self._access_key

    @access_key.setter
    def access_key(self, value):
        self._access_key = value
    @property
    def gateway_configs(self):
        return self._gateway_configs

    @gateway_configs.setter
    def gateway_configs(self, value):
        if isinstance(value, list):
            self._gateway_configs = list()
            for i in value:
                if isinstance(i, GatewayConfig):
                    self._gateway_configs.append(i)
                else:
                    self._gateway_configs.append(GatewayConfig.from_alipay_dict(i))
    @property
    def secret_key(self):
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseIdeConfigGetResponse, self).parse_response_content(response_content)
        if 'access_key' in response:
            self.access_key = response['access_key']
        if 'gateway_configs' in response:
            self.gateway_configs = response['gateway_configs']
        if 'secret_key' in response:
            self.secret_key = response['secret_key']
