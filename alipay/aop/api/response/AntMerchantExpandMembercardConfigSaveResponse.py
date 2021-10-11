#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandMembercardConfigSaveResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMembercardConfigSaveResponse, self).__init__()
        self._member_product_id = None
        self._out_biz_no = None

    @property
    def member_product_id(self):
        return self._member_product_id

    @member_product_id.setter
    def member_product_id(self, value):
        self._member_product_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMembercardConfigSaveResponse, self).parse_response_content(response_content)
        if 'member_product_id' in response:
            self.member_product_id = response['member_product_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
