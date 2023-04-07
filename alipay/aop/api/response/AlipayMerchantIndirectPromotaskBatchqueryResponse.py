#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndirectPromoTask import IndirectPromoTask


class AlipayMerchantIndirectPromotaskBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectPromotaskBatchqueryResponse, self).__init__()
        self._item_list = None
        self._total = None

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, IndirectPromoTask):
                    self._item_list.append(i)
                else:
                    self._item_list.append(IndirectPromoTask.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectPromotaskBatchqueryResponse, self).parse_response_content(response_content)
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'total' in response:
            self.total = response['total']
