#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductSignStatusInfo import ProductSignStatusInfo


class AlipayOpenAgentSignstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentSignstatusQueryResponse, self).__init__()
        self._sign_status_list = None

    @property
    def sign_status_list(self):
        return self._sign_status_list

    @sign_status_list.setter
    def sign_status_list(self, value):
        if isinstance(value, list):
            self._sign_status_list = list()
            for i in value:
                if isinstance(i, ProductSignStatusInfo):
                    self._sign_status_list.append(i)
                else:
                    self._sign_status_list.append(ProductSignStatusInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentSignstatusQueryResponse, self).parse_response_content(response_content)
        if 'sign_status_list' in response:
            self.sign_status_list = response['sign_status_list']
