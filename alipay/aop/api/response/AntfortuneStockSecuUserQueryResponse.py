#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SecuUserList import SecuUserList


class AntfortuneStockSecuUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockSecuUserQueryResponse, self).__init__()
        self._secu_user_list = None

    @property
    def secu_user_list(self):
        return self._secu_user_list

    @secu_user_list.setter
    def secu_user_list(self, value):
        if isinstance(value, list):
            self._secu_user_list = list()
            for i in value:
                if isinstance(i, SecuUserList):
                    self._secu_user_list.append(i)
                else:
                    self._secu_user_list.append(SecuUserList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockSecuUserQueryResponse, self).parse_response_content(response_content)
        if 'secu_user_list' in response:
            self.secu_user_list = response['secu_user_list']
