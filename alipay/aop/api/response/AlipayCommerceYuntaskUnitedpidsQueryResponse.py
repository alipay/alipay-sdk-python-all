#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskUnitedpidsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskUnitedpidsQueryResponse, self).__init__()
        self._pid_list = None

    @property
    def pid_list(self):
        return self._pid_list

    @pid_list.setter
    def pid_list(self, value):
        if isinstance(value, list):
            self._pid_list = list()
            for i in value:
                self._pid_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskUnitedpidsQueryResponse, self).parse_response_content(response_content)
        if 'pid_list' in response:
            self.pid_list = response['pid_list']
