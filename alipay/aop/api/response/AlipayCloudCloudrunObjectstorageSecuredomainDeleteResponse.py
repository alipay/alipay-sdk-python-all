#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunObjectstorageSecuredomainDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageSecuredomainDeleteResponse, self).__init__()
        self._secure_domain = None

    @property
    def secure_domain(self):
        return self._secure_domain

    @secure_domain.setter
    def secure_domain(self, value):
        self._secure_domain = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageSecuredomainDeleteResponse, self).parse_response_content(response_content)
        if 'secure_domain' in response:
            self.secure_domain = response['secure_domain']
