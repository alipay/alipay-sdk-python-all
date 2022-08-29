#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBusinessRelationAlipayaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationAlipayaccountQueryResponse, self).__init__()
        self._alipay_account = None
        self._alipay_name = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def alipay_name(self):
        return self._alipay_name

    @alipay_name.setter
    def alipay_name(self, value):
        self._alipay_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationAlipayaccountQueryResponse, self).parse_response_content(response_content)
        if 'alipay_account' in response:
            self.alipay_account = response['alipay_account']
        if 'alipay_name' in response:
            self.alipay_name = response['alipay_name']
