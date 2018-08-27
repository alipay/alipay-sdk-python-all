#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundDetailItemAOPModel import FundDetailItemAOPModel


class AlipayUserFunditemGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFunditemGetResponse, self).__init__()
        self._fund_detail_item_aopmodel = None

    @property
    def fund_detail_item_aopmodel(self):
        return self._fund_detail_item_aopmodel

    @fund_detail_item_aopmodel.setter
    def fund_detail_item_aopmodel(self, value):
        if isinstance(value, FundDetailItemAOPModel):
            self._fund_detail_item_aopmodel = value
        else:
            self._fund_detail_item_aopmodel = FundDetailItemAOPModel.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserFunditemGetResponse, self).parse_response_content(response_content)
        if 'fund_detail_item_aopmodel' in response:
            self.fund_detail_item_aopmodel = response['fund_detail_item_aopmodel']
