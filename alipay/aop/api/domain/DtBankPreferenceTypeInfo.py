#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtBankPreferenceDiscountRule import DtBankPreferenceDiscountRule
from alipay.aop.api.domain.DtBankPreferenceIntelligentRule import DtBankPreferenceIntelligentRule
from alipay.aop.api.domain.DtBankPreferenceMultiStagedRule import DtBankPreferenceMultiStagedRule
from alipay.aop.api.domain.DtBankPreferenceRandomRule import DtBankPreferenceRandomRule
from alipay.aop.api.domain.DtBankPreferenceSingleRule import DtBankPreferenceSingleRule


class DtBankPreferenceTypeInfo(object):

    def __init__(self):
        self._discount_rule = None
        self._intelligent_rule = None
        self._multi_staged_rule = None
        self._preference_type = None
        self._random_rule = None
        self._single_rule = None
        self._use_threshold = None

    @property
    def discount_rule(self):
        return self._discount_rule

    @discount_rule.setter
    def discount_rule(self, value):
        if isinstance(value, DtBankPreferenceDiscountRule):
            self._discount_rule = value
        else:
            self._discount_rule = DtBankPreferenceDiscountRule.from_alipay_dict(value)
    @property
    def intelligent_rule(self):
        return self._intelligent_rule

    @intelligent_rule.setter
    def intelligent_rule(self, value):
        if isinstance(value, DtBankPreferenceIntelligentRule):
            self._intelligent_rule = value
        else:
            self._intelligent_rule = DtBankPreferenceIntelligentRule.from_alipay_dict(value)
    @property
    def multi_staged_rule(self):
        return self._multi_staged_rule

    @multi_staged_rule.setter
    def multi_staged_rule(self, value):
        if isinstance(value, DtBankPreferenceMultiStagedRule):
            self._multi_staged_rule = value
        else:
            self._multi_staged_rule = DtBankPreferenceMultiStagedRule.from_alipay_dict(value)
    @property
    def preference_type(self):
        return self._preference_type

    @preference_type.setter
    def preference_type(self, value):
        self._preference_type = value
    @property
    def random_rule(self):
        return self._random_rule

    @random_rule.setter
    def random_rule(self, value):
        if isinstance(value, DtBankPreferenceRandomRule):
            self._random_rule = value
        else:
            self._random_rule = DtBankPreferenceRandomRule.from_alipay_dict(value)
    @property
    def single_rule(self):
        return self._single_rule

    @single_rule.setter
    def single_rule(self, value):
        if isinstance(value, DtBankPreferenceSingleRule):
            self._single_rule = value
        else:
            self._single_rule = DtBankPreferenceSingleRule.from_alipay_dict(value)
    @property
    def use_threshold(self):
        return self._use_threshold

    @use_threshold.setter
    def use_threshold(self, value):
        self._use_threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_rule:
            if hasattr(self.discount_rule, 'to_alipay_dict'):
                params['discount_rule'] = self.discount_rule.to_alipay_dict()
            else:
                params['discount_rule'] = self.discount_rule
        if self.intelligent_rule:
            if hasattr(self.intelligent_rule, 'to_alipay_dict'):
                params['intelligent_rule'] = self.intelligent_rule.to_alipay_dict()
            else:
                params['intelligent_rule'] = self.intelligent_rule
        if self.multi_staged_rule:
            if hasattr(self.multi_staged_rule, 'to_alipay_dict'):
                params['multi_staged_rule'] = self.multi_staged_rule.to_alipay_dict()
            else:
                params['multi_staged_rule'] = self.multi_staged_rule
        if self.preference_type:
            if hasattr(self.preference_type, 'to_alipay_dict'):
                params['preference_type'] = self.preference_type.to_alipay_dict()
            else:
                params['preference_type'] = self.preference_type
        if self.random_rule:
            if hasattr(self.random_rule, 'to_alipay_dict'):
                params['random_rule'] = self.random_rule.to_alipay_dict()
            else:
                params['random_rule'] = self.random_rule
        if self.single_rule:
            if hasattr(self.single_rule, 'to_alipay_dict'):
                params['single_rule'] = self.single_rule.to_alipay_dict()
            else:
                params['single_rule'] = self.single_rule
        if self.use_threshold:
            if hasattr(self.use_threshold, 'to_alipay_dict'):
                params['use_threshold'] = self.use_threshold.to_alipay_dict()
            else:
                params['use_threshold'] = self.use_threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankPreferenceTypeInfo()
        if 'discount_rule' in d:
            o.discount_rule = d['discount_rule']
        if 'intelligent_rule' in d:
            o.intelligent_rule = d['intelligent_rule']
        if 'multi_staged_rule' in d:
            o.multi_staged_rule = d['multi_staged_rule']
        if 'preference_type' in d:
            o.preference_type = d['preference_type']
        if 'random_rule' in d:
            o.random_rule = d['random_rule']
        if 'single_rule' in d:
            o.single_rule = d['single_rule']
        if 'use_threshold' in d:
            o.use_threshold = d['use_threshold']
        return o


