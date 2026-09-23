#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SaasEbankInstInfo import SaasEbankInstInfo


class AlipayTradeSaasEbankConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasEbankConsultResponse, self).__init__()
        self._bank_code_list = None
        self._inst_id_list = None
        self._inst_info_list = None

    @property
    def bank_code_list(self):
        return self._bank_code_list

    @bank_code_list.setter
    def bank_code_list(self, value):
        if isinstance(value, list):
            self._bank_code_list = list()
            for i in value:
                self._bank_code_list.append(i)
    @property
    def inst_id_list(self):
        return self._inst_id_list

    @inst_id_list.setter
    def inst_id_list(self, value):
        if isinstance(value, list):
            self._inst_id_list = list()
            for i in value:
                self._inst_id_list.append(i)
    @property
    def inst_info_list(self):
        return self._inst_info_list

    @inst_info_list.setter
    def inst_info_list(self, value):
        if isinstance(value, list):
            self._inst_info_list = list()
            for i in value:
                if isinstance(i, SaasEbankInstInfo):
                    self._inst_info_list.append(i)
                else:
                    self._inst_info_list.append(SaasEbankInstInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasEbankConsultResponse, self).parse_response_content(response_content)
        if 'bank_code_list' in response:
            self.bank_code_list = response['bank_code_list']
        if 'inst_id_list' in response:
            self.inst_id_list = response['inst_id_list']
        if 'inst_info_list' in response:
            self.inst_info_list = response['inst_info_list']
