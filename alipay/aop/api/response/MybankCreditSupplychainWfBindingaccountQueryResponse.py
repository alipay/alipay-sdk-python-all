#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainWfBindingaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfBindingaccountQueryResponse, self).__init__()
        self._alipayuserid = None

    @property
    def alipayuserid(self):
        return self._alipayuserid

    @alipayuserid.setter
    def alipayuserid(self, value):
        self._alipayuserid = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfBindingaccountQueryResponse, self).parse_response_content(response_content)
        if 'alipayuserid' in response:
            self.alipayuserid = response['alipayuserid']
