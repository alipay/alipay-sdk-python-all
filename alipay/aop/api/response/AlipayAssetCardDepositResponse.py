#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetCardDepositResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetCardDepositResponse, self).__init__()
        self._extend_info = None
        self._recharge_no = None

    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def recharge_no(self):
        return self._recharge_no

    @recharge_no.setter
    def recharge_no(self, value):
        self._recharge_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetCardDepositResponse, self).parse_response_content(response_content)
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'recharge_no' in response:
            self.recharge_no = response['recharge_no']
