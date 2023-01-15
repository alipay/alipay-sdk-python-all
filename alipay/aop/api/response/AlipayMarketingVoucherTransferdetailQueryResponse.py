#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenVoucherTradeFundDetail import OpenVoucherTradeFundDetail


class AlipayMarketingVoucherTransferdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherTransferdetailQueryResponse, self).__init__()
        self._open_voucher_trade_fund_details = None

    @property
    def open_voucher_trade_fund_details(self):
        return self._open_voucher_trade_fund_details

    @open_voucher_trade_fund_details.setter
    def open_voucher_trade_fund_details(self, value):
        if isinstance(value, list):
            self._open_voucher_trade_fund_details = list()
            for i in value:
                if isinstance(i, OpenVoucherTradeFundDetail):
                    self._open_voucher_trade_fund_details.append(i)
                else:
                    self._open_voucher_trade_fund_details.append(OpenVoucherTradeFundDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherTransferdetailQueryResponse, self).parse_response_content(response_content)
        if 'open_voucher_trade_fund_details' in response:
            self.open_voucher_trade_fund_details = response['open_voucher_trade_fund_details']
