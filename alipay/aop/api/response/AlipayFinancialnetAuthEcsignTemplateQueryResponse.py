#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContractTemplateOpenVO import ContractTemplateOpenVO


class AlipayFinancialnetAuthEcsignTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignTemplateQueryResponse, self).__init__()
        self._contract_template_open_vo = None

    @property
    def contract_template_open_vo(self):
        return self._contract_template_open_vo

    @contract_template_open_vo.setter
    def contract_template_open_vo(self, value):
        if isinstance(value, ContractTemplateOpenVO):
            self._contract_template_open_vo = value
        else:
            self._contract_template_open_vo = ContractTemplateOpenVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignTemplateQueryResponse, self).parse_response_content(response_content)
        if 'contract_template_open_vo' in response:
            self.contract_template_open_vo = response['contract_template_open_vo']
