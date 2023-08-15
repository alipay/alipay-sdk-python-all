#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunObjectstorageSecuredomainQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageSecuredomainQueryResponse, self).__init__()
        self._secure_domain_list = None

    @property
    def secure_domain_list(self):
        return self._secure_domain_list

    @secure_domain_list.setter
    def secure_domain_list(self, value):
        if isinstance(value, list):
            self._secure_domain_list = list()
            for i in value:
                self._secure_domain_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageSecuredomainQueryResponse, self).parse_response_content(response_content)
        if 'secure_domain_list' in response:
            self.secure_domain_list = response['secure_domain_list']
