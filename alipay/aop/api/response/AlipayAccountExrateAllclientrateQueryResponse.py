#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExClientRateVO import ExClientRateVO


class AlipayAccountExrateAllclientrateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountExrateAllclientrateQueryResponse, self).__init__()
        self._client_rate_list = None

    @property
    def client_rate_list(self):
        return self._client_rate_list

    @client_rate_list.setter
    def client_rate_list(self, value):
        if isinstance(value, list):
            self._client_rate_list = list()
            for i in value:
                if isinstance(i, ExClientRateVO):
                    self._client_rate_list.append(i)
                else:
                    self._client_rate_list.append(ExClientRateVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayAccountExrateAllclientrateQueryResponse, self).parse_response_content(response_content)
        if 'client_rate_list' in response:
            self.client_rate_list = response['client_rate_list']
