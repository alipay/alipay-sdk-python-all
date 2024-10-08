#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardSettleaccountBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardSettleaccountBatchqueryResponse, self).__init__()
        self._settle_alipay_logon_id_list = None

    @property
    def settle_alipay_logon_id_list(self):
        return self._settle_alipay_logon_id_list

    @settle_alipay_logon_id_list.setter
    def settle_alipay_logon_id_list(self, value):
        if isinstance(value, list):
            self._settle_alipay_logon_id_list = list()
            for i in value:
                self._settle_alipay_logon_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardSettleaccountBatchqueryResponse, self).parse_response_content(response_content)
        if 'settle_alipay_logon_id_list' in response:
            self.settle_alipay_logon_id_list = response['settle_alipay_logon_id_list']
