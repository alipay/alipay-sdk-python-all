#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLifeserviceAccountmsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceAccountmsgSendResponse, self).__init__()
        self._settle_account_id_list = None

    @property
    def settle_account_id_list(self):
        return self._settle_account_id_list

    @settle_account_id_list.setter
    def settle_account_id_list(self, value):
        if isinstance(value, list):
            self._settle_account_id_list = list()
            for i in value:
                self._settle_account_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceAccountmsgSendResponse, self).parse_response_content(response_content)
        if 'settle_account_id_list' in response:
            self.settle_account_id_list = response['settle_account_id_list']
