#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitSendTime import BenefitSendTime
from alipay.aop.api.domain.CouponEffectTime import CouponEffectTime
from alipay.aop.api.domain.CouponTemplateConsumeInfo import CouponTemplateConsumeInfo
from alipay.aop.api.domain.DiscountInfoConfig import DiscountInfoConfig


class AlipayUserDtbankcustChannelvoucherconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankcustChannelvoucherconfigQueryResponse, self).__init__()
        self._activity_id = None
        self._activity_name = None
        self._activity_status = None
        self._bank_card_type = None
        self._benefit_send_time = None
        self._card_bin_list = None
        self._coupon_effect_time = None
        self._coupon_template_consume_info = None
        self._discount_info_config = None
        self._min_send_count = None
        self._total_budget = None
        self._user_instruction_list = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def bank_card_type(self):
        return self._bank_card_type

    @bank_card_type.setter
    def bank_card_type(self, value):
        self._bank_card_type = value
    @property
    def benefit_send_time(self):
        return self._benefit_send_time

    @benefit_send_time.setter
    def benefit_send_time(self, value):
        if isinstance(value, BenefitSendTime):
            self._benefit_send_time = value
        else:
            self._benefit_send_time = BenefitSendTime.from_alipay_dict(value)
    @property
    def card_bin_list(self):
        return self._card_bin_list

    @card_bin_list.setter
    def card_bin_list(self, value):
        if isinstance(value, list):
            self._card_bin_list = list()
            for i in value:
                self._card_bin_list.append(i)
    @property
    def coupon_effect_time(self):
        return self._coupon_effect_time

    @coupon_effect_time.setter
    def coupon_effect_time(self, value):
        if isinstance(value, CouponEffectTime):
            self._coupon_effect_time = value
        else:
            self._coupon_effect_time = CouponEffectTime.from_alipay_dict(value)
    @property
    def coupon_template_consume_info(self):
        return self._coupon_template_consume_info

    @coupon_template_consume_info.setter
    def coupon_template_consume_info(self, value):
        if isinstance(value, CouponTemplateConsumeInfo):
            self._coupon_template_consume_info = value
        else:
            self._coupon_template_consume_info = CouponTemplateConsumeInfo.from_alipay_dict(value)
    @property
    def discount_info_config(self):
        return self._discount_info_config

    @discount_info_config.setter
    def discount_info_config(self, value):
        if isinstance(value, DiscountInfoConfig):
            self._discount_info_config = value
        else:
            self._discount_info_config = DiscountInfoConfig.from_alipay_dict(value)
    @property
    def min_send_count(self):
        return self._min_send_count

    @min_send_count.setter
    def min_send_count(self, value):
        self._min_send_count = value
    @property
    def total_budget(self):
        return self._total_budget

    @total_budget.setter
    def total_budget(self, value):
        self._total_budget = value
    @property
    def user_instruction_list(self):
        return self._user_instruction_list

    @user_instruction_list.setter
    def user_instruction_list(self, value):
        if isinstance(value, list):
            self._user_instruction_list = list()
            for i in value:
                self._user_instruction_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankcustChannelvoucherconfigQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'bank_card_type' in response:
            self.bank_card_type = response['bank_card_type']
        if 'benefit_send_time' in response:
            self.benefit_send_time = response['benefit_send_time']
        if 'card_bin_list' in response:
            self.card_bin_list = response['card_bin_list']
        if 'coupon_effect_time' in response:
            self.coupon_effect_time = response['coupon_effect_time']
        if 'coupon_template_consume_info' in response:
            self.coupon_template_consume_info = response['coupon_template_consume_info']
        if 'discount_info_config' in response:
            self.discount_info_config = response['discount_info_config']
        if 'min_send_count' in response:
            self.min_send_count = response['min_send_count']
        if 'total_budget' in response:
            self.total_budget = response['total_budget']
        if 'user_instruction_list' in response:
            self.user_instruction_list = response['user_instruction_list']
