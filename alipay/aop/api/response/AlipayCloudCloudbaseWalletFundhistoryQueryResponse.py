#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundHistory import FundHistory


class AlipayCloudCloudbaseWalletFundhistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletFundhistoryQueryResponse, self).__init__()
        self._fund_histories = None

    @property
    def fund_histories(self):
        return self._fund_histories

    @fund_histories.setter
    def fund_histories(self, value):
        if isinstance(value, list):
            self._fund_histories = list()
            for i in value:
                if isinstance(i, FundHistory):
                    self._fund_histories.append(i)
                else:
                    self._fund_histories.append(FundHistory.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletFundhistoryQueryResponse, self).parse_response_content(response_content)
        if 'fund_histories' in response:
            self.fund_histories = response['fund_histories']
