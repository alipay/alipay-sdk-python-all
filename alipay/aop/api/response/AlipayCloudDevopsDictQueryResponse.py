#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudDevopsDictQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudDevopsDictQueryResponse, self).__init__()
        self._config = None

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudDevopsDictQueryResponse, self).parse_response_content(response_content)
        if 'config' in response:
            self.config = response['config']
