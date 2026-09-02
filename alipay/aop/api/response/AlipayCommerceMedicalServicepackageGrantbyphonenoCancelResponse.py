#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalServicepackageGrantbyphonenoCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServicepackageGrantbyphonenoCancelResponse, self).__init__()
        self._fail_order_no_list = None

    @property
    def fail_order_no_list(self):
        return self._fail_order_no_list

    @fail_order_no_list.setter
    def fail_order_no_list(self, value):
        if isinstance(value, list):
            self._fail_order_no_list = list()
            for i in value:
                self._fail_order_no_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServicepackageGrantbyphonenoCancelResponse, self).parse_response_content(response_content)
        if 'fail_order_no_list' in response:
            self.fail_order_no_list = response['fail_order_no_list']
