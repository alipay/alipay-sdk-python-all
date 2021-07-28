#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BlockChainTransactionApiDO import BlockChainTransactionApiDO


class AnttechDataServiceBlockchainTransactionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechDataServiceBlockchainTransactionQueryResponse, self).__init__()
        self._transaction_list = None

    @property
    def transaction_list(self):
        return self._transaction_list

    @transaction_list.setter
    def transaction_list(self, value):
        if isinstance(value, list):
            self._transaction_list = list()
            for i in value:
                if isinstance(i, BlockChainTransactionApiDO):
                    self._transaction_list.append(i)
                else:
                    self._transaction_list.append(BlockChainTransactionApiDO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechDataServiceBlockchainTransactionQueryResponse, self).parse_response_content(response_content)
        if 'transaction_list' in response:
            self.transaction_list = response['transaction_list']
