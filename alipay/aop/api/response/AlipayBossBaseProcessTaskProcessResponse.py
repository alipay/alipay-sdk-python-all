#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BPOpenApiInstance import BPOpenApiInstance


class AlipayBossBaseProcessTaskProcessResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseProcessTaskProcessResponse, self).__init__()
        self._instance = None

    @property
    def instance(self):
        return self._instance

    @instance.setter
    def instance(self, value):
        if isinstance(value, BPOpenApiInstance):
            self._instance = value
        else:
            self._instance = BPOpenApiInstance.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseProcessTaskProcessResponse, self).parse_response_content(response_content)
        if 'instance' in response:
            self.instance = response['instance']
