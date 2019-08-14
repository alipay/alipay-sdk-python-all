#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PeriodRuleParams import PeriodRuleParams


class AlipayUserAgreementTransferModel(object):

    def __init__(self):
        self._agreement_no = None
        self._period_rule_params = None
        self._target_product_code = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def period_rule_params(self):
        return self._period_rule_params

    @period_rule_params.setter
    def period_rule_params(self, value):
        if isinstance(value, PeriodRuleParams):
            self._period_rule_params = value
        else:
            self._period_rule_params = PeriodRuleParams.from_alipay_dict(value)
    @property
    def target_product_code(self):
        return self._target_product_code

    @target_product_code.setter
    def target_product_code(self, value):
        self._target_product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.period_rule_params:
            if hasattr(self.period_rule_params, 'to_alipay_dict'):
                params['period_rule_params'] = self.period_rule_params.to_alipay_dict()
            else:
                params['period_rule_params'] = self.period_rule_params
        if self.target_product_code:
            if hasattr(self.target_product_code, 'to_alipay_dict'):
                params['target_product_code'] = self.target_product_code.to_alipay_dict()
            else:
                params['target_product_code'] = self.target_product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementTransferModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'period_rule_params' in d:
            o.period_rule_params = d['period_rule_params']
        if 'target_product_code' in d:
            o.target_product_code = d['target_product_code']
        return o


