#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IPLimit import IPLimit


class AlipayCloudCloudrunObjectstorageIplimitModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageIplimitModifyResponse, self).__init__()
        self._ip_limit = None

    @property
    def ip_limit(self):
        return self._ip_limit

    @ip_limit.setter
    def ip_limit(self, value):
        if isinstance(value, IPLimit):
            self._ip_limit = value
        else:
            self._ip_limit = IPLimit.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageIplimitModifyResponse, self).parse_response_content(response_content)
        if 'ip_limit' in response:
            self.ip_limit = response['ip_limit']
