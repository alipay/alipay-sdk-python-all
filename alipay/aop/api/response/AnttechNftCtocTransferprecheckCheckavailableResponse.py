#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftCtocTransferprecheckCheckavailableResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocTransferprecheckCheckavailableResponse, self).__init__()
        self._pre_check_id = None

    @property
    def pre_check_id(self):
        return self._pre_check_id

    @pre_check_id.setter
    def pre_check_id(self, value):
        self._pre_check_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocTransferprecheckCheckavailableResponse, self).parse_response_content(response_content)
        if 'pre_check_id' in response:
            self.pre_check_id = response['pre_check_id']
