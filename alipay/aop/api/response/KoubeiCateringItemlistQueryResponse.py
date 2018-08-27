#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CaterItemListInfo import CaterItemListInfo


class KoubeiCateringItemlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringItemlistQueryResponse, self).__init__()
        self._item_list = None
        self._request_id = None
        self._total_amount = None

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, CaterItemListInfo):
                    self._item_list.append(i)
                else:
                    self._item_list.append(CaterItemListInfo.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringItemlistQueryResponse, self).parse_response_content(response_content)
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
