#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnvVar import EnvVar


class AlipayCloudCloudbaseFunctionEnvvarsGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionEnvvarsGetResponse, self).__init__()
        self._env_vars = None

    @property
    def env_vars(self):
        return self._env_vars

    @env_vars.setter
    def env_vars(self, value):
        if isinstance(value, list):
            self._env_vars = list()
            for i in value:
                if isinstance(i, EnvVar):
                    self._env_vars.append(i)
                else:
                    self._env_vars.append(EnvVar.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionEnvvarsGetResponse, self).parse_response_content(response_content)
        if 'env_vars' in response:
            self.env_vars = response['env_vars']
