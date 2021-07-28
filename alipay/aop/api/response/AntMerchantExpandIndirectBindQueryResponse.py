#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectBindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectBindQueryResponse, self).__init__()
        self._partner_id = None
        self._smid = None

    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        if isinstance(value, list):
            self._smid = list()
            for i in value:
                self._smid.append(i)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectBindQueryResponse, self).parse_response_content(response_content)
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'smid' in response:
            self.smid = response['smid']
