#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountVO import AccountVO


class AnttechBlockchainDefinSaasAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinSaasAccountQueryResponse, self).__init__()
        self._accounts = None
        self._out_member_id = None

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, value):
        if isinstance(value, list):
            self._accounts = list()
            for i in value:
                if isinstance(i, AccountVO):
                    self._accounts.append(i)
                else:
                    self._accounts.append(AccountVO.from_alipay_dict(i))
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        self._out_member_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinSaasAccountQueryResponse, self).parse_response_content(response_content)
        if 'accounts' in response:
            self.accounts = response['accounts']
        if 'out_member_id' in response:
            self.out_member_id = response['out_member_id']
