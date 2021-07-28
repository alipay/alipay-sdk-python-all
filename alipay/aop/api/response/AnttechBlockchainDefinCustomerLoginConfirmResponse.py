#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DefiCustUserDTO import DefiCustUserDTO


class AnttechBlockchainDefinCustomerLoginConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinCustomerLoginConfirmResponse, self).__init__()
        self._user_info = None

    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, DefiCustUserDTO):
            self._user_info = value
        else:
            self._user_info = DefiCustUserDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinCustomerLoginConfirmResponse, self).parse_response_content(response_content)
        if 'user_info' in response:
            self.user_info = response['user_info']
