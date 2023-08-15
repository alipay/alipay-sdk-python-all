#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantNetworkRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantNetworkRelationQueryResponse, self).__init__()
        self._relation_type = None

    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantNetworkRelationQueryResponse, self).parse_response_content(response_content)
        if 'relation_type' in response:
            self.relation_type = response['relation_type']
