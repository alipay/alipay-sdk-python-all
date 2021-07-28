#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceTradeDetail import DeviceTradeDetail


class AlipayCommerceIotDapplyTradedetaillistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDapplyTradedetaillistQueryResponse, self).__init__()
        self._devicetradedetaillist = None
        self._total_count = None

    @property
    def devicetradedetaillist(self):
        return self._devicetradedetaillist

    @devicetradedetaillist.setter
    def devicetradedetaillist(self, value):
        if isinstance(value, list):
            self._devicetradedetaillist = list()
            for i in value:
                if isinstance(i, DeviceTradeDetail):
                    self._devicetradedetaillist.append(i)
                else:
                    self._devicetradedetaillist.append(DeviceTradeDetail.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDapplyTradedetaillistQueryResponse, self).parse_response_content(response_content)
        if 'devicetradedetaillist' in response:
            self.devicetradedetaillist = response['devicetradedetaillist']
        if 'total_count' in response:
            self.total_count = response['total_count']
