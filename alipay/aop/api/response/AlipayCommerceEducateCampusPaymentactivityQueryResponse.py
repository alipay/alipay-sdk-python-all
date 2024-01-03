#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCampusPaymentactivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusPaymentactivityQueryResponse, self).__init__()
        self._inst_id_list = None
        self._sign_up = None

    @property
    def inst_id_list(self):
        return self._inst_id_list

    @inst_id_list.setter
    def inst_id_list(self, value):
        if isinstance(value, list):
            self._inst_id_list = list()
            for i in value:
                self._inst_id_list.append(i)
    @property
    def sign_up(self):
        return self._sign_up

    @sign_up.setter
    def sign_up(self, value):
        self._sign_up = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusPaymentactivityQueryResponse, self).parse_response_content(response_content)
        if 'inst_id_list' in response:
            self.inst_id_list = response['inst_id_list']
        if 'sign_up' in response:
            self.sign_up = response['sign_up']
