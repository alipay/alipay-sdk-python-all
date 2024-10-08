#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardSettleaccountusedQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardSettleaccountusedQueryResponse, self).__init__()
        self._settle_alipay_logon_id = None

    @property
    def settle_alipay_logon_id(self):
        return self._settle_alipay_logon_id

    @settle_alipay_logon_id.setter
    def settle_alipay_logon_id(self, value):
        self._settle_alipay_logon_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardSettleaccountusedQueryResponse, self).parse_response_content(response_content)
        if 'settle_alipay_logon_id' in response:
            self.settle_alipay_logon_id = response['settle_alipay_logon_id']
