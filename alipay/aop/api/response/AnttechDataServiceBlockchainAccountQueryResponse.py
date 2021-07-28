#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BlockChainAccountApiDO import BlockChainAccountApiDO


class AnttechDataServiceBlockchainAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechDataServiceBlockchainAccountQueryResponse, self).__init__()
        self._account_list = None

    @property
    def account_list(self):
        return self._account_list

    @account_list.setter
    def account_list(self, value):
        if isinstance(value, list):
            self._account_list = list()
            for i in value:
                if isinstance(i, BlockChainAccountApiDO):
                    self._account_list.append(i)
                else:
                    self._account_list.append(BlockChainAccountApiDO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechDataServiceBlockchainAccountQueryResponse, self).parse_response_content(response_content)
        if 'account_list' in response:
            self.account_list = response['account_list']
