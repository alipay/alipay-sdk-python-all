#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLifeaccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLifeaccountCreateResponse, self).__init__()
        self._public_id = None

    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLifeaccountCreateResponse, self).parse_response_content(response_content)
        if 'public_id' in response:
            self.public_id = response['public_id']
