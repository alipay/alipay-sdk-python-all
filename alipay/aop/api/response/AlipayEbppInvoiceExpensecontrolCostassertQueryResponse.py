#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExpenseAssetInfo import ExpenseAssetInfo


class AlipayEbppInvoiceExpensecontrolCostassertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceExpensecontrolCostassertQueryResponse, self).__init__()
        self._asset_list = None

    @property
    def asset_list(self):
        return self._asset_list

    @asset_list.setter
    def asset_list(self, value):
        if isinstance(value, list):
            self._asset_list = list()
            for i in value:
                if isinstance(i, ExpenseAssetInfo):
                    self._asset_list.append(i)
                else:
                    self._asset_list.append(ExpenseAssetInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceExpensecontrolCostassertQueryResponse, self).parse_response_content(response_content)
        if 'asset_list' in response:
            self.asset_list = response['asset_list']
