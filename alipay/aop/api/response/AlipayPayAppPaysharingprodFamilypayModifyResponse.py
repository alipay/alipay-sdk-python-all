#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FamilyPayCardInfo import FamilyPayCardInfo


class AlipayPayAppPaysharingprodFamilypayModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppPaysharingprodFamilypayModifyResponse, self).__init__()
        self._card_info = None

    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, FamilyPayCardInfo):
            self._card_info = value
        else:
            self._card_info = FamilyPayCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppPaysharingprodFamilypayModifyResponse, self).parse_response_content(response_content)
        if 'card_info' in response:
            self.card_info = response['card_info']
