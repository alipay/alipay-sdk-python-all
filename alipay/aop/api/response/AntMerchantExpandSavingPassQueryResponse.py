#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SCardQueryVO import SCardQueryVO


class AntMerchantExpandSavingPassQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandSavingPassQueryResponse, self).__init__()
        self._card_list = None
        self._enable = None

    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, value):
        if isinstance(value, list):
            self._card_list = list()
            for i in value:
                if isinstance(i, SCardQueryVO):
                    self._card_list.append(i)
                else:
                    self._card_list.append(SCardQueryVO.from_alipay_dict(i))
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandSavingPassQueryResponse, self).parse_response_content(response_content)
        if 'card_list' in response:
            self.card_list = response['card_list']
        if 'enable' in response:
            self.enable = response['enable']
