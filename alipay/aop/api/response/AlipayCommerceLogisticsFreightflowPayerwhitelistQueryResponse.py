#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FreightFlowAllowedAccount import FreightFlowAllowedAccount


class AlipayCommerceLogisticsFreightflowPayerwhitelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowPayerwhitelistQueryResponse, self).__init__()
        self._allowed_account_white_list = None
        self._logistics_code = None
        self._mode = None
        self._owner_account_no = None
        self._owner_account_type = None
        self._scene = None

    @property
    def allowed_account_white_list(self):
        return self._allowed_account_white_list

    @allowed_account_white_list.setter
    def allowed_account_white_list(self, value):
        if isinstance(value, list):
            self._allowed_account_white_list = list()
            for i in value:
                if isinstance(i, FreightFlowAllowedAccount):
                    self._allowed_account_white_list.append(i)
                else:
                    self._allowed_account_white_list.append(FreightFlowAllowedAccount.from_alipay_dict(i))
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def owner_account_no(self):
        return self._owner_account_no

    @owner_account_no.setter
    def owner_account_no(self, value):
        self._owner_account_no = value
    @property
    def owner_account_type(self):
        return self._owner_account_type

    @owner_account_type.setter
    def owner_account_type(self, value):
        self._owner_account_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowPayerwhitelistQueryResponse, self).parse_response_content(response_content)
        if 'allowed_account_white_list' in response:
            self.allowed_account_white_list = response['allowed_account_white_list']
        if 'logistics_code' in response:
            self.logistics_code = response['logistics_code']
        if 'mode' in response:
            self.mode = response['mode']
        if 'owner_account_no' in response:
            self.owner_account_no = response['owner_account_no']
        if 'owner_account_type' in response:
            self.owner_account_type = response['owner_account_type']
        if 'scene' in response:
            self.scene = response['scene']
