#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantContractCommonConfirmResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantContractCommonConfirmResponse, self).__init__()
        self._contract_no = None
        self._ext_info = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantContractCommonConfirmResponse, self).parse_response_content(response_content)
        if 'contract_no' in response:
            self.contract_no = response['contract_no']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
