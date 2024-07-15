#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupAuthorizeAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupAuthorizeAddResponse, self).__init__()
        self._authorize_id = None

    @property
    def authorize_id(self):
        return self._authorize_id

    @authorize_id.setter
    def authorize_id(self, value):
        self._authorize_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupAuthorizeAddResponse, self).parse_response_content(response_content)
        if 'authorize_id' in response:
            self.authorize_id = response['authorize_id']
