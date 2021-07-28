#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DefiCustMemberDTO import DefiCustMemberDTO


class AnttechBlockchainDefinCustomerMemberQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinCustomerMemberQueryResponse, self).__init__()
        self._member_info_list = None

    @property
    def member_info_list(self):
        return self._member_info_list

    @member_info_list.setter
    def member_info_list(self, value):
        if isinstance(value, list):
            self._member_info_list = list()
            for i in value:
                if isinstance(i, DefiCustMemberDTO):
                    self._member_info_list.append(i)
                else:
                    self._member_info_list.append(DefiCustMemberDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinCustomerMemberQueryResponse, self).parse_response_content(response_content)
        if 'member_info_list' in response:
            self.member_info_list = response['member_info_list']
