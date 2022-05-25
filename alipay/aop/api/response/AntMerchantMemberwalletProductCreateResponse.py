#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantMemberwalletProductCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantMemberwalletProductCreateResponse, self).__init__()
        self._member_wallet_id = None
        self._out_biz_no = None

    @property
    def member_wallet_id(self):
        return self._member_wallet_id

    @member_wallet_id.setter
    def member_wallet_id(self, value):
        self._member_wallet_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantMemberwalletProductCreateResponse, self).parse_response_content(response_content)
        if 'member_wallet_id' in response:
            self.member_wallet_id = response['member_wallet_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
