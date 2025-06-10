#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsExpressmanCertifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsExpressmanCertifyQueryResponse, self).__init__()
        self._certify = None
        self._certify_url = None

    @property
    def certify(self):
        return self._certify

    @certify.setter
    def certify(self, value):
        self._certify = value
    @property
    def certify_url(self):
        return self._certify_url

    @certify_url.setter
    def certify_url(self, value):
        self._certify_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsExpressmanCertifyQueryResponse, self).parse_response_content(response_content)
        if 'certify' in response:
            self.certify = response['certify']
        if 'certify_url' in response:
            self.certify_url = response['certify_url']
