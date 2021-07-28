#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperatorAccountVO import OperatorAccountVO


class AlipayOpenAuthOperatorAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthOperatorAddResponse, self).__init__()
        self._accounts = None
        self._operator_id = None

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, value):
        if isinstance(value, list):
            self._accounts = list()
            for i in value:
                if isinstance(i, OperatorAccountVO):
                    self._accounts.append(i)
                else:
                    self._accounts.append(OperatorAccountVO.from_alipay_dict(i))
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthOperatorAddResponse, self).parse_response_content(response_content)
        if 'accounts' in response:
            self.accounts = response['accounts']
        if 'operator_id' in response:
            self.operator_id = response['operator_id']
