#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BillApiSingleItem import BillApiSingleItem
from alipay.aop.api.domain.BillApiStatisticInfo import BillApiStatisticInfo


class AlipayUserMobilebillListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMobilebillListQueryResponse, self).__init__()
        self._bill_list_items = None
        self._statistic_info = None

    @property
    def bill_list_items(self):
        return self._bill_list_items

    @bill_list_items.setter
    def bill_list_items(self, value):
        if isinstance(value, BillApiSingleItem):
            self._bill_list_items = value
        else:
            self._bill_list_items = BillApiSingleItem.from_alipay_dict(value)
    @property
    def statistic_info(self):
        return self._statistic_info

    @statistic_info.setter
    def statistic_info(self, value):
        if isinstance(value, BillApiStatisticInfo):
            self._statistic_info = value
        else:
            self._statistic_info = BillApiStatisticInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserMobilebillListQueryResponse, self).parse_response_content(response_content)
        if 'bill_list_items' in response:
            self.bill_list_items = response['bill_list_items']
        if 'statistic_info' in response:
            self.statistic_info = response['statistic_info']
