#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EtcInoviceRepeatTradeList import EtcInoviceRepeatTradeList


class AlipayCommerceTransportEtcenterpriseInvoicerepeatApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseInvoicerepeatApplyResponse, self).__init__()
        self._trade_list = None

    @property
    def trade_list(self):
        return self._trade_list

    @trade_list.setter
    def trade_list(self, value):
        if isinstance(value, list):
            self._trade_list = list()
            for i in value:
                if isinstance(i, EtcInoviceRepeatTradeList):
                    self._trade_list.append(i)
                else:
                    self._trade_list.append(EtcInoviceRepeatTradeList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseInvoicerepeatApplyResponse, self).parse_response_content(response_content)
        if 'trade_list' in response:
            self.trade_list = response['trade_list']
