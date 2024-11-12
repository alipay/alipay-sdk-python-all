#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMallWalletruleSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMallWalletruleSetResponse, self).__init__()
        self._digital_shop_id_list = None
        self._pending_shop_id_list = None
        self._wallet_template_id = None

    @property
    def digital_shop_id_list(self):
        return self._digital_shop_id_list

    @digital_shop_id_list.setter
    def digital_shop_id_list(self, value):
        if isinstance(value, list):
            self._digital_shop_id_list = list()
            for i in value:
                self._digital_shop_id_list.append(i)
    @property
    def pending_shop_id_list(self):
        return self._pending_shop_id_list

    @pending_shop_id_list.setter
    def pending_shop_id_list(self, value):
        if isinstance(value, list):
            self._pending_shop_id_list = list()
            for i in value:
                self._pending_shop_id_list.append(i)
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMallWalletruleSetResponse, self).parse_response_content(response_content)
        if 'digital_shop_id_list' in response:
            self.digital_shop_id_list = response['digital_shop_id_list']
        if 'pending_shop_id_list' in response:
            self.pending_shop_id_list = response['pending_shop_id_list']
        if 'wallet_template_id' in response:
            self.wallet_template_id = response['wallet_template_id']
