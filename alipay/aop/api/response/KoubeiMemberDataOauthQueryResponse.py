#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMemberDataOauthQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMemberDataOauthQueryResponse, self).__init__()
        self._ext_info = None
        self._operator_id = None
        self._operator_partner_id = None
        self._operator_type = None
        self._shop_ids = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_partner_id(self):
        return self._operator_partner_id

    @operator_partner_id.setter
    def operator_partner_id(self, value):
        self._operator_partner_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        self._shop_ids = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMemberDataOauthQueryResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'operator_id' in response:
            self.operator_id = response['operator_id']
        if 'operator_partner_id' in response:
            self.operator_partner_id = response['operator_partner_id']
        if 'operator_type' in response:
            self.operator_type = response['operator_type']
        if 'shop_ids' in response:
            self.shop_ids = response['shop_ids']
