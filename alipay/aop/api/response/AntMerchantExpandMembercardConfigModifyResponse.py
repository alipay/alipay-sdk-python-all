#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberCardTemplateConfig import MemberCardTemplateConfig
from alipay.aop.api.domain.MemberCardPayEffectiveRule import MemberCardPayEffectiveRule
from alipay.aop.api.domain.MemberCardPrepaidPromotionPlanInfo import MemberCardPrepaidPromotionPlanInfo


class AntMerchantExpandMembercardConfigModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMembercardConfigModifyResponse, self).__init__()
        self._card_template_config = None
        self._member_product_id = None
        self._out_biz_no = None
        self._pay_effective_rule = None
        self._prepaid_promotion_plans = None

    @property
    def card_template_config(self):
        return self._card_template_config

    @card_template_config.setter
    def card_template_config(self, value):
        if isinstance(value, MemberCardTemplateConfig):
            self._card_template_config = value
        else:
            self._card_template_config = MemberCardTemplateConfig.from_alipay_dict(value)
    @property
    def member_product_id(self):
        return self._member_product_id

    @member_product_id.setter
    def member_product_id(self, value):
        self._member_product_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_effective_rule(self):
        return self._pay_effective_rule

    @pay_effective_rule.setter
    def pay_effective_rule(self, value):
        if isinstance(value, MemberCardPayEffectiveRule):
            self._pay_effective_rule = value
        else:
            self._pay_effective_rule = MemberCardPayEffectiveRule.from_alipay_dict(value)
    @property
    def prepaid_promotion_plans(self):
        return self._prepaid_promotion_plans

    @prepaid_promotion_plans.setter
    def prepaid_promotion_plans(self, value):
        if isinstance(value, list):
            self._prepaid_promotion_plans = list()
            for i in value:
                if isinstance(i, MemberCardPrepaidPromotionPlanInfo):
                    self._prepaid_promotion_plans.append(i)
                else:
                    self._prepaid_promotion_plans.append(MemberCardPrepaidPromotionPlanInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMembercardConfigModifyResponse, self).parse_response_content(response_content)
        if 'card_template_config' in response:
            self.card_template_config = response['card_template_config']
        if 'member_product_id' in response:
            self.member_product_id = response['member_product_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'pay_effective_rule' in response:
            self.pay_effective_rule = response['pay_effective_rule']
        if 'prepaid_promotion_plans' in response:
            self.prepaid_promotion_plans = response['prepaid_promotion_plans']
