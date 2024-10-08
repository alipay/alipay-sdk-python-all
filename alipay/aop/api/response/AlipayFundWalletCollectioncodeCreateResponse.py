#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletCollectioncodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletCollectioncodeCreateResponse, self).__init__()
        self._collection_code_url = None

    @property
    def collection_code_url(self):
        return self._collection_code_url

    @collection_code_url.setter
    def collection_code_url(self, value):
        self._collection_code_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletCollectioncodeCreateResponse, self).parse_response_content(response_content)
        if 'collection_code_url' in response:
            self.collection_code_url = response['collection_code_url']
