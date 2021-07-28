#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApiContractDetail import ApiContractDetail


class ZhimaCustomerContractDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerContractDetailQueryResponse, self).__init__()
        self._contract_detail = None

    @property
    def contract_detail(self):
        return self._contract_detail

    @contract_detail.setter
    def contract_detail(self, value):
        if isinstance(value, ApiContractDetail):
            self._contract_detail = value
        else:
            self._contract_detail = ApiContractDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerContractDetailQueryResponse, self).parse_response_content(response_content)
        if 'contract_detail' in response:
            self.contract_detail = response['contract_detail']
