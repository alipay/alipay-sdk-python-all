#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainFactoringSelleradmitQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainFactoringSelleradmitQueryResponse, self).__init__()
        self._exsit = None
        self._need_sign_ar = None
        self._refuse_code = None
        self._refuse_msg = None
        self._refused = None
        self._seller_mybank_card_no_list = None
        self._white = None

    @property
    def exsit(self):
        return self._exsit

    @exsit.setter
    def exsit(self, value):
        self._exsit = value
    @property
    def need_sign_ar(self):
        return self._need_sign_ar

    @need_sign_ar.setter
    def need_sign_ar(self, value):
        self._need_sign_ar = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def refused(self):
        return self._refused

    @refused.setter
    def refused(self, value):
        self._refused = value
    @property
    def seller_mybank_card_no_list(self):
        return self._seller_mybank_card_no_list

    @seller_mybank_card_no_list.setter
    def seller_mybank_card_no_list(self, value):
        if isinstance(value, list):
            self._seller_mybank_card_no_list = list()
            for i in value:
                self._seller_mybank_card_no_list.append(i)
    @property
    def white(self):
        return self._white

    @white.setter
    def white(self, value):
        self._white = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainFactoringSelleradmitQueryResponse, self).parse_response_content(response_content)
        if 'exsit' in response:
            self.exsit = response['exsit']
        if 'need_sign_ar' in response:
            self.need_sign_ar = response['need_sign_ar']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'refused' in response:
            self.refused = response['refused']
        if 'seller_mybank_card_no_list' in response:
            self.seller_mybank_card_no_list = response['seller_mybank_card_no_list']
        if 'white' in response:
            self.white = response['white']
