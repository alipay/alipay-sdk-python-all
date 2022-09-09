#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizFundSettleDetailInfo import BizFundSettleDetailInfo
from alipay.aop.api.domain.BizFundSettleSummary import BizFundSettleSummary


class AlipayMarketingActivitySettleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivitySettleQueryResponse, self).__init__()
        self._order_no = None
        self._settle_info = None
        self._summary = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, list):
            self._settle_info = list()
            for i in value:
                if isinstance(i, BizFundSettleDetailInfo):
                    self._settle_info.append(i)
                else:
                    self._settle_info.append(BizFundSettleDetailInfo.from_alipay_dict(i))
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if isinstance(value, BizFundSettleSummary):
            self._summary = value
        else:
            self._summary = BizFundSettleSummary.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivitySettleQueryResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'settle_info' in response:
            self.settle_info = response['settle_info']
        if 'summary' in response:
            self.summary = response['summary']
