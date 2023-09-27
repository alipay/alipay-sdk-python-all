#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountNoInfo import AccountNoInfo


class AlipayUserDtbankcustAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankcustAccountQueryResponse, self).__init__()
        self._account_no_info_list = None

    @property
    def account_no_info_list(self):
        return self._account_no_info_list

    @account_no_info_list.setter
    def account_no_info_list(self, value):
        if isinstance(value, list):
            self._account_no_info_list = list()
            for i in value:
                if isinstance(i, AccountNoInfo):
                    self._account_no_info_list.append(i)
                else:
                    self._account_no_info_list.append(AccountNoInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankcustAccountQueryResponse, self).parse_response_content(response_content)
        if 'account_no_info_list' in response:
            self.account_no_info_list = response['account_no_info_list']
