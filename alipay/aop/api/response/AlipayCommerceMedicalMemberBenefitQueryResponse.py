#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitDiscountInfoDTO import BenefitDiscountInfoDTO


class AlipayCommerceMedicalMemberBenefitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMemberBenefitQueryResponse, self).__init__()
        self._benefit_order_id = None
        self._discount_info_list = None
        self._discount_type = None
        self._member_price = None
        self._membership = None
        self._original_price = None
        self._product_id = None

    @property
    def benefit_order_id(self):
        return self._benefit_order_id

    @benefit_order_id.setter
    def benefit_order_id(self, value):
        self._benefit_order_id = value
    @property
    def discount_info_list(self):
        return self._discount_info_list

    @discount_info_list.setter
    def discount_info_list(self, value):
        if isinstance(value, list):
            self._discount_info_list = list()
            for i in value:
                if isinstance(i, BenefitDiscountInfoDTO):
                    self._discount_info_list.append(i)
                else:
                    self._discount_info_list.append(BenefitDiscountInfoDTO.from_alipay_dict(i))
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def member_price(self):
        return self._member_price

    @member_price.setter
    def member_price(self, value):
        self._member_price = value
    @property
    def membership(self):
        return self._membership

    @membership.setter
    def membership(self, value):
        self._membership = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMemberBenefitQueryResponse, self).parse_response_content(response_content)
        if 'benefit_order_id' in response:
            self.benefit_order_id = response['benefit_order_id']
        if 'discount_info_list' in response:
            self.discount_info_list = response['discount_info_list']
        if 'discount_type' in response:
            self.discount_type = response['discount_type']
        if 'member_price' in response:
            self.member_price = response['member_price']
        if 'membership' in response:
            self.membership = response['membership']
        if 'original_price' in response:
            self.original_price = response['original_price']
        if 'product_id' in response:
            self.product_id = response['product_id']
