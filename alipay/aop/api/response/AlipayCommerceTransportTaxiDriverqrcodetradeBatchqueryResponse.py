#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DriverTradeInfo import DriverTradeInfo


class AlipayCommerceTransportTaxiDriverqrcodetradeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiDriverqrcodetradeBatchqueryResponse, self).__init__()
        self._driver_qrcode_trade_info_list = None

    @property
    def driver_qrcode_trade_info_list(self):
        return self._driver_qrcode_trade_info_list

    @driver_qrcode_trade_info_list.setter
    def driver_qrcode_trade_info_list(self, value):
        if isinstance(value, list):
            self._driver_qrcode_trade_info_list = list()
            for i in value:
                if isinstance(i, DriverTradeInfo):
                    self._driver_qrcode_trade_info_list.append(i)
                else:
                    self._driver_qrcode_trade_info_list.append(DriverTradeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiDriverqrcodetradeBatchqueryResponse, self).parse_response_content(response_content)
        if 'driver_qrcode_trade_info_list' in response:
            self.driver_qrcode_trade_info_list = response['driver_qrcode_trade_info_list']
