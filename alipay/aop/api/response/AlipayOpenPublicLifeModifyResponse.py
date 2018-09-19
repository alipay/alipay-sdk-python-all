#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLifeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLifeModifyResponse, self).__init__()
        self._modify_time = None
        self._public_id = None

    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLifeModifyResponse, self).parse_response_content(response_content)
        if 'modify_time' in response:
            self.modify_time = response['modify_time']
        if 'public_id' in response:
            self.public_id = response['public_id']
