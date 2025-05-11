#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankModifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankModifyQueryResponse, self).__init__()
        self._modify_type = None
        self._modify_value = None
        self._status = None

    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value
    @property
    def modify_value(self):
        return self._modify_value

    @modify_value.setter
    def modify_value(self, value):
        self._modify_value = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankModifyQueryResponse, self).parse_response_content(response_content)
        if 'modify_type' in response:
            self.modify_type = response['modify_type']
        if 'modify_value' in response:
            self.modify_value = response['modify_value']
        if 'status' in response:
            self.status = response['status']
