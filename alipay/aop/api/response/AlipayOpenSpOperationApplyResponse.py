#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendAccountDTO import RecommendAccountDTO
from alipay.aop.api.domain.RecommendAccountDTO import RecommendAccountDTO


class AlipayOpenSpOperationApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpOperationApplyResponse, self).__init__()
        self._batch_no = None
        self._bind_account = None
        self._recommend_accounts = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def bind_account(self):
        return self._bind_account

    @bind_account.setter
    def bind_account(self, value):
        if isinstance(value, RecommendAccountDTO):
            self._bind_account = value
        else:
            self._bind_account = RecommendAccountDTO.from_alipay_dict(value)
    @property
    def recommend_accounts(self):
        return self._recommend_accounts

    @recommend_accounts.setter
    def recommend_accounts(self, value):
        if isinstance(value, list):
            self._recommend_accounts = list()
            for i in value:
                if isinstance(i, RecommendAccountDTO):
                    self._recommend_accounts.append(i)
                else:
                    self._recommend_accounts.append(RecommendAccountDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpOperationApplyResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'bind_account' in response:
            self.bind_account = response['bind_account']
        if 'recommend_accounts' in response:
            self.recommend_accounts = response['recommend_accounts']
