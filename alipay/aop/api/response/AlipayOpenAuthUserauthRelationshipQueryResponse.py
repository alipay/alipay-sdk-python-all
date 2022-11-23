#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthUserauthRelationshipQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthUserauthRelationshipQueryResponse, self).__init__()
        self._query_detail = None

    @property
    def query_detail(self):
        return self._query_detail

    @query_detail.setter
    def query_detail(self, value):
        self._query_detail = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthUserauthRelationshipQueryResponse, self).parse_response_content(response_content)
        if 'query_detail' in response:
            self.query_detail = response['query_detail']
