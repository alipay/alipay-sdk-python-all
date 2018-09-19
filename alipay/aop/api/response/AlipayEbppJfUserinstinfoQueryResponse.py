#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EbppUserChargeInstInfo import EbppUserChargeInstInfo


class AlipayEbppJfUserinstinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfUserinstinfoQueryResponse, self).__init__()
        self._user_charge_inst_info_list = None

    @property
    def user_charge_inst_info_list(self):
        return self._user_charge_inst_info_list

    @user_charge_inst_info_list.setter
    def user_charge_inst_info_list(self, value):
        if isinstance(value, list):
            self._user_charge_inst_info_list = list()
            for i in value:
                if isinstance(i, EbppUserChargeInstInfo):
                    self._user_charge_inst_info_list.append(i)
                else:
                    self._user_charge_inst_info_list.append(EbppUserChargeInstInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfUserinstinfoQueryResponse, self).parse_response_content(response_content)
        if 'user_charge_inst_info_list' in response:
            self.user_charge_inst_info_list = response['user_charge_inst_info_list']
