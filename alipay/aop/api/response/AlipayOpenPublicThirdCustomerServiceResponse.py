#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicThirdCustomerServiceResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicThirdCustomerServiceResponse, self).__init__()
        self._public_name = None

    @property
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicThirdCustomerServiceResponse, self).parse_response_content(response_content)
        if 'public_name' in response:
            self.public_name = response['public_name']
