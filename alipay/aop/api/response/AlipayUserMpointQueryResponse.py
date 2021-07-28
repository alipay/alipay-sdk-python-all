#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMpointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMpointQueryResponse, self).__init__()
        self._balance = None
        self._grade = None
        self._joint_info = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def joint_info(self):
        return self._joint_info

    @joint_info.setter
    def joint_info(self, value):
        if isinstance(value, list):
            self._joint_info = list()
            for i in value:
                self._joint_info.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayUserMpointQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'grade' in response:
            self.grade = response['grade']
        if 'joint_info' in response:
            self.joint_info = response['joint_info']
