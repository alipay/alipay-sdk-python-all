#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerSafedomainQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerSafedomainQueryResponse, self).__init__()
        self._allow_add_count = None
        self._safe_domains = None

    @property
    def allow_add_count(self):
        return self._allow_add_count

    @allow_add_count.setter
    def allow_add_count(self, value):
        self._allow_add_count = value
    @property
    def safe_domains(self):
        return self._safe_domains

    @safe_domains.setter
    def safe_domains(self, value):
        if isinstance(value, list):
            self._safe_domains = list()
            for i in value:
                self._safe_domains.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerSafedomainQueryResponse, self).parse_response_content(response_content)
        if 'allow_add_count' in response:
            self.allow_add_count = response['allow_add_count']
        if 'safe_domains' in response:
            self.safe_domains = response['safe_domains']
