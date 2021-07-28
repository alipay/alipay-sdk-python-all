#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BlockChainContractApiDO import BlockChainContractApiDO


class AnttechDataServiceBlockchainContractQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechDataServiceBlockchainContractQueryResponse, self).__init__()
        self._contract_list = None

    @property
    def contract_list(self):
        return self._contract_list

    @contract_list.setter
    def contract_list(self, value):
        if isinstance(value, list):
            self._contract_list = list()
            for i in value:
                if isinstance(i, BlockChainContractApiDO):
                    self._contract_list.append(i)
                else:
                    self._contract_list.append(BlockChainContractApiDO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechDataServiceBlockchainContractQueryResponse, self).parse_response_content(response_content)
        if 'contract_list' in response:
            self.contract_list = response['contract_list']
