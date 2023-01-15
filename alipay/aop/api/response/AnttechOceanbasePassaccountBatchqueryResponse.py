#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PassAccountDTO import PassAccountDTO


class AnttechOceanbasePassaccountBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassaccountBatchqueryResponse, self).__init__()
        self._pass_accounts = None

    @property
    def pass_accounts(self):
        return self._pass_accounts

    @pass_accounts.setter
    def pass_accounts(self, value):
        if isinstance(value, list):
            self._pass_accounts = list()
            for i in value:
                if isinstance(i, PassAccountDTO):
                    self._pass_accounts.append(i)
                else:
                    self._pass_accounts.append(PassAccountDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassaccountBatchqueryResponse, self).parse_response_content(response_content)
        if 'pass_accounts' in response:
            self.pass_accounts = response['pass_accounts']
