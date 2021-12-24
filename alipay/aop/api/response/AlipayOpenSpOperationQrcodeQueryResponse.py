#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendAccountDTO import RecommendAccountDTO
from alipay.aop.api.domain.RecommendAccountDTO import RecommendAccountDTO
from alipay.aop.api.domain.RecommendAccountDTO import RecommendAccountDTO


class AlipayOpenSpOperationQrcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpOperationQrcodeQueryResponse, self).__init__()
        self._batch_no = None
        self._bind_account = None
        self._qr_code_url = None
        self._recommend_account_list = None
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
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def recommend_account_list(self):
        return self._recommend_account_list

    @recommend_account_list.setter
    def recommend_account_list(self, value):
        if isinstance(value, list):
            self._recommend_account_list = list()
            for i in value:
                if isinstance(i, RecommendAccountDTO):
                    self._recommend_account_list.append(i)
                else:
                    self._recommend_account_list.append(RecommendAccountDTO.from_alipay_dict(i))
    @property
    def recommend_accounts(self):
        return self._recommend_accounts

    @recommend_accounts.setter
    def recommend_accounts(self, value):
        if isinstance(value, RecommendAccountDTO):
            self._recommend_accounts = value
        else:
            self._recommend_accounts = RecommendAccountDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpOperationQrcodeQueryResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'bind_account' in response:
            self.bind_account = response['bind_account']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
        if 'recommend_account_list' in response:
            self.recommend_account_list = response['recommend_account_list']
        if 'recommend_accounts' in response:
            self.recommend_accounts = response['recommend_accounts']
