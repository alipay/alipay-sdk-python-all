#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundWalletBizOrderResponse import FundWalletBizOrderResponse


class AlipayFundWalletPageoperationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletPageoperationQueryResponse, self).__init__()
        self._fund_wallet_biz_order_response_list = None

    @property
    def fund_wallet_biz_order_response_list(self):
        return self._fund_wallet_biz_order_response_list

    @fund_wallet_biz_order_response_list.setter
    def fund_wallet_biz_order_response_list(self, value):
        if isinstance(value, list):
            self._fund_wallet_biz_order_response_list = list()
            for i in value:
                if isinstance(i, FundWalletBizOrderResponse):
                    self._fund_wallet_biz_order_response_list.append(i)
                else:
                    self._fund_wallet_biz_order_response_list.append(FundWalletBizOrderResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletPageoperationQueryResponse, self).parse_response_content(response_content)
        if 'fund_wallet_biz_order_response_list' in response:
            self.fund_wallet_biz_order_response_list = response['fund_wallet_biz_order_response_list']
