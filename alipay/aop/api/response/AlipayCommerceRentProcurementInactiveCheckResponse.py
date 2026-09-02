#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentProcurementInactiveCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentProcurementInactiveCheckResponse, self).__init__()
        self._activation_label = None

    @property
    def activation_label(self):
        return self._activation_label

    @activation_label.setter
    def activation_label(self, value):
        self._activation_label = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentProcurementInactiveCheckResponse, self).parse_response_content(response_content)
        if 'activation_label' in response:
            self.activation_label = response['activation_label']
