#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PublicBindAccount import PublicBindAccount


class AlipayMobileStdPublicAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileStdPublicAccountQueryResponse, self).__init__()
        self._public_bind_accounts = None

    @property
    def public_bind_accounts(self):
        return self._public_bind_accounts

    @public_bind_accounts.setter
    def public_bind_accounts(self, value):
        if isinstance(value, list):
            self._public_bind_accounts = list()
            for i in value:
                if isinstance(i, PublicBindAccount):
                    self._public_bind_accounts.append(i)
                else:
                    self._public_bind_accounts.append(PublicBindAccount.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMobileStdPublicAccountQueryResponse, self).parse_response_content(response_content)
        if 'public_bind_accounts' in response:
            self.public_bind_accounts = response['public_bind_accounts']
