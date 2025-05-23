#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardAftersalesConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardAftersalesConfirmResponse, self).__init__()
        self._aftersales_id = None

    @property
    def aftersales_id(self):
        return self._aftersales_id

    @aftersales_id.setter
    def aftersales_id(self, value):
        self._aftersales_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardAftersalesConfirmResponse, self).parse_response_content(response_content)
        if 'aftersales_id' in response:
            self.aftersales_id = response['aftersales_id']
