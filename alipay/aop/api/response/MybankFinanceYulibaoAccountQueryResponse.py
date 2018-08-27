#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YLBProfitDetailInfo import YLBProfitDetailInfo


class MybankFinanceYulibaoAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankFinanceYulibaoAccountQueryResponse, self).__init__()
        self._available_amount = None
        self._freeze_amount = None
        self._sys_freeze_amount = None
        self._total_amount = None
        self._ylb_profit_detail_info = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def sys_freeze_amount(self):
        return self._sys_freeze_amount

    @sys_freeze_amount.setter
    def sys_freeze_amount(self, value):
        self._sys_freeze_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def ylb_profit_detail_info(self):
        return self._ylb_profit_detail_info

    @ylb_profit_detail_info.setter
    def ylb_profit_detail_info(self, value):
        if isinstance(value, YLBProfitDetailInfo):
            self._ylb_profit_detail_info = value
        else:
            self._ylb_profit_detail_info = YLBProfitDetailInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(MybankFinanceYulibaoAccountQueryResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'freeze_amount' in response:
            self.freeze_amount = response['freeze_amount']
        if 'sys_freeze_amount' in response:
            self.sys_freeze_amount = response['sys_freeze_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'ylb_profit_detail_info' in response:
            self.ylb_profit_detail_info = response['ylb_profit_detail_info']
