#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemberCardTemplateConfig import MemberCardTemplateConfig
from alipay.aop.api.domain.MemberCardOperator import MemberCardOperator
from alipay.aop.api.domain.MemberCardPayEffectiveRule import MemberCardPayEffectiveRule
from alipay.aop.api.domain.MemberCardCreatePrepaidPromotionPlanInfo import MemberCardCreatePrepaidPromotionPlanInfo


class AntMerchantExpandMembercardConfigSaveModel(object):

    def __init__(self):
        self._card_template_config = None
        self._operator = None
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
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        if isinstance(value, MemberCardOperator):
            self._operator = value
        else:
            self._operator = MemberCardOperator.from_alipay_dict(value)
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
                if isinstance(i, MemberCardCreatePrepaidPromotionPlanInfo):
                    self._prepaid_promotion_plans.append(i)
                else:
                    self._prepaid_promotion_plans.append(MemberCardCreatePrepaidPromotionPlanInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_config:
            if hasattr(self.card_template_config, 'to_alipay_dict'):
                params['card_template_config'] = self.card_template_config.to_alipay_dict()
            else:
                params['card_template_config'] = self.card_template_config
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_effective_rule:
            if hasattr(self.pay_effective_rule, 'to_alipay_dict'):
                params['pay_effective_rule'] = self.pay_effective_rule.to_alipay_dict()
            else:
                params['pay_effective_rule'] = self.pay_effective_rule
        if self.prepaid_promotion_plans:
            if isinstance(self.prepaid_promotion_plans, list):
                for i in range(0, len(self.prepaid_promotion_plans)):
                    element = self.prepaid_promotion_plans[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prepaid_promotion_plans[i] = element.to_alipay_dict()
            if hasattr(self.prepaid_promotion_plans, 'to_alipay_dict'):
                params['prepaid_promotion_plans'] = self.prepaid_promotion_plans.to_alipay_dict()
            else:
                params['prepaid_promotion_plans'] = self.prepaid_promotion_plans
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandMembercardConfigSaveModel()
        if 'card_template_config' in d:
            o.card_template_config = d['card_template_config']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_effective_rule' in d:
            o.pay_effective_rule = d['pay_effective_rule']
        if 'prepaid_promotion_plans' in d:
            o.prepaid_promotion_plans = d['prepaid_promotion_plans']
        return o


