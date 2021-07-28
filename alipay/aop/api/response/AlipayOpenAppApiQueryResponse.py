#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AuthApiDTO import AuthApiDTO


class AlipayOpenAppApiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppApiQueryResponse, self).__init__()
        self._apis = None

    @property
    def apis(self):
        return self._apis

    @apis.setter
    def apis(self, value):
        if isinstance(value, list):
            self._apis = list()
            for i in value:
                if isinstance(i, AuthApiDTO):
                    self._apis.append(i)
                else:
                    self._apis.append(AuthApiDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppApiQueryResponse, self).parse_response_content(response_content)
        if 'apis' in response:
            self.apis = response['apis']
