#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowSubaccountDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowSubaccountDeleteResponse, self).__init__()
        self._cancel_account_flag = None

    @property
    def cancel_account_flag(self):
        return self._cancel_account_flag

    @cancel_account_flag.setter
    def cancel_account_flag(self, value):
        self._cancel_account_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowSubaccountDeleteResponse, self).parse_response_content(response_content)
        if 'cancel_account_flag' in response:
            self.cancel_account_flag = response['cancel_account_flag']
