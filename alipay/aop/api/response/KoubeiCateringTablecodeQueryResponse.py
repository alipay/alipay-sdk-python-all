#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringTablecodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringTablecodeQueryResponse, self).__init__()
        self._code_flag = None
        self._shop_id = None
        self._table_num = None

    @property
    def code_flag(self):
        return self._code_flag

    @code_flag.setter
    def code_flag(self, value):
        self._code_flag = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def table_num(self):
        return self._table_num

    @table_num.setter
    def table_num(self, value):
        self._table_num = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringTablecodeQueryResponse, self).parse_response_content(response_content)
        if 'code_flag' in response:
            self.code_flag = response['code_flag']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'table_num' in response:
            self.table_num = response['table_num']
