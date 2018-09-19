#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardInfo import CardInfo
from alipay.aop.api.domain.CodeCouponInfo import CodeCouponInfo
from alipay.aop.api.domain.ConsumeInfo import ConsumeInfo
from alipay.aop.api.domain.ReduceInfo import ReduceInfo


class KoubeiMarketingDataMallDiscountQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataMallDiscountQueryResponse, self).__init__()
        self._card_list = None
        self._code_coupon_list = None
        self._consume_list = None
        self._reduce_list = None

    @property
    def card_list(self):
        return self._card_list

    @card_list.setter
    def card_list(self, value):
        if isinstance(value, list):
            self._card_list = list()
            for i in value:
                if isinstance(i, CardInfo):
                    self._card_list.append(i)
                else:
                    self._card_list.append(CardInfo.from_alipay_dict(i))
    @property
    def code_coupon_list(self):
        return self._code_coupon_list

    @code_coupon_list.setter
    def code_coupon_list(self, value):
        if isinstance(value, list):
            self._code_coupon_list = list()
            for i in value:
                if isinstance(i, CodeCouponInfo):
                    self._code_coupon_list.append(i)
                else:
                    self._code_coupon_list.append(CodeCouponInfo.from_alipay_dict(i))
    @property
    def consume_list(self):
        return self._consume_list

    @consume_list.setter
    def consume_list(self, value):
        if isinstance(value, list):
            self._consume_list = list()
            for i in value:
                if isinstance(i, ConsumeInfo):
                    self._consume_list.append(i)
                else:
                    self._consume_list.append(ConsumeInfo.from_alipay_dict(i))
    @property
    def reduce_list(self):
        return self._reduce_list

    @reduce_list.setter
    def reduce_list(self, value):
        if isinstance(value, list):
            self._reduce_list = list()
            for i in value:
                if isinstance(i, ReduceInfo):
                    self._reduce_list.append(i)
                else:
                    self._reduce_list.append(ReduceInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataMallDiscountQueryResponse, self).parse_response_content(response_content)
        if 'card_list' in response:
            self.card_list = response['card_list']
        if 'code_coupon_list' in response:
            self.code_coupon_list = response['code_coupon_list']
        if 'consume_list' in response:
            self.consume_list = response['consume_list']
        if 'reduce_list' in response:
            self.reduce_list = response['reduce_list']
