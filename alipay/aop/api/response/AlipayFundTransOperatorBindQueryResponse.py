#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransOperatorBindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransOperatorBindQueryResponse, self).__init__()
        self._bind = None
        self._operator_name = None
        self._operator_role = None

    @property
    def bind(self):
        return self._bind

    @bind.setter
    def bind(self, value):
        self._bind = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def operator_role(self):
        return self._operator_role

    @operator_role.setter
    def operator_role(self, value):
        if isinstance(value, list):
            self._operator_role = list()
            for i in value:
                self._operator_role.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransOperatorBindQueryResponse, self).parse_response_content(response_content)
        if 'bind' in response:
            self.bind = response['bind']
        if 'operator_name' in response:
            self.operator_name = response['operator_name']
        if 'operator_role' in response:
            self.operator_role = response['operator_role']
