#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsTradeInfo import InsTradeInfo


class AlipayInsAutoAutoinsprodPolicyApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoinsprodPolicyApplyResponse, self).__init__()
        self._enquiry_biz_id = None
        self._quote_biz_id = None
        self._trade_infos = None
        self._zhi_link = None

    @property
    def enquiry_biz_id(self):
        return self._enquiry_biz_id

    @enquiry_biz_id.setter
    def enquiry_biz_id(self, value):
        self._enquiry_biz_id = value
    @property
    def quote_biz_id(self):
        return self._quote_biz_id

    @quote_biz_id.setter
    def quote_biz_id(self, value):
        self._quote_biz_id = value
    @property
    def trade_infos(self):
        return self._trade_infos

    @trade_infos.setter
    def trade_infos(self, value):
        if isinstance(value, list):
            self._trade_infos = list()
            for i in value:
                if isinstance(i, InsTradeInfo):
                    self._trade_infos.append(i)
                else:
                    self._trade_infos.append(InsTradeInfo.from_alipay_dict(i))
    @property
    def zhi_link(self):
        return self._zhi_link

    @zhi_link.setter
    def zhi_link(self, value):
        self._zhi_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoinsprodPolicyApplyResponse, self).parse_response_content(response_content)
        if 'enquiry_biz_id' in response:
            self.enquiry_biz_id = response['enquiry_biz_id']
        if 'quote_biz_id' in response:
            self.quote_biz_id = response['quote_biz_id']
        if 'trade_infos' in response:
            self.trade_infos = response['trade_infos']
        if 'zhi_link' in response:
            self.zhi_link = response['zhi_link']
