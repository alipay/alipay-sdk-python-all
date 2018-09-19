#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayAccount import AlipayAccount


class AlipayUserAccountGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountGetResponse, self).__init__()
        self._alipay_account = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        if isinstance(value, AlipayAccount):
            self._alipay_account = value
        else:
            self._alipay_account = AlipayAccount.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountGetResponse, self).parse_response_content(response_content)
        if 'alipay_account' in response:
            self.alipay_account = response['alipay_account']
