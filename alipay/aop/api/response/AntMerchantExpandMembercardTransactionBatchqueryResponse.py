#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberCardUserTransactionDetail import MemberCardUserTransactionDetail


class AntMerchantExpandMembercardTransactionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMembercardTransactionBatchqueryResponse, self).__init__()
        self._partner_id = None
        self._transaction_detail_list = None

    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def transaction_detail_list(self):
        return self._transaction_detail_list

    @transaction_detail_list.setter
    def transaction_detail_list(self, value):
        if isinstance(value, list):
            self._transaction_detail_list = list()
            for i in value:
                if isinstance(i, MemberCardUserTransactionDetail):
                    self._transaction_detail_list.append(i)
                else:
                    self._transaction_detail_list.append(MemberCardUserTransactionDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMembercardTransactionBatchqueryResponse, self).parse_response_content(response_content)
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'transaction_detail_list' in response:
            self.transaction_detail_list = response['transaction_detail_list']
