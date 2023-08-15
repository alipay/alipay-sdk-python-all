#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StaticDomain import StaticDomain


class AlipayCloudCloudrunStaticsiteDomainAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunStaticsiteDomainAddResponse, self).__init__()
        self._domain = None

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        if isinstance(value, StaticDomain):
            self._domain = value
        else:
            self._domain = StaticDomain.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunStaticsiteDomainAddResponse, self).parse_response_content(response_content)
        if 'domain' in response:
            self.domain = response['domain']
