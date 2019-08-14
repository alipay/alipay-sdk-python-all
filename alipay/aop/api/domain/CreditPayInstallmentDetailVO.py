#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayChargePricingVO import CreditPayChargePricingVO
from alipay.aop.api.domain.CreditPayClauseVO import CreditPayClauseVO
from alipay.aop.api.domain.CreditPayDiscountVO import CreditPayDiscountVO
from alipay.aop.api.domain.CreditPayIntPricingVO import CreditPayIntPricingVO
from alipay.aop.api.domain.CreditPayRepayVO import CreditPayRepayVO
from alipay.aop.api.domain.CreditPayTermVO import CreditPayTermVO


class CreditPayInstallmentDetailVO(object):

    def __init__(self):
        self._charge_pricing_list = None
        self._clauses = None
        self._discount_info = None
        self._instal_itrv = None
        self._instal_type = None
        self._installment_id = None
        self._int_pricing = None
        self._render_strategy = None
        self._repay_info = None
        self._sale_pd_code = None
        self._scheme_sign = None
        self._term_info = None

    @property
    def charge_pricing_list(self):
        return self._charge_pricing_list

    @charge_pricing_list.setter
    def charge_pricing_list(self, value):
        if isinstance(value, list):
            self._charge_pricing_list = list()
            for i in value:
                if isinstance(i, CreditPayChargePricingVO):
                    self._charge_pricing_list.append(i)
                else:
                    self._charge_pricing_list.append(CreditPayChargePricingVO.from_alipay_dict(i))
    @property
    def clauses(self):
        return self._clauses

    @clauses.setter
    def clauses(self, value):
        if isinstance(value, list):
            self._clauses = list()
            for i in value:
                if isinstance(i, CreditPayClauseVO):
                    self._clauses.append(i)
                else:
                    self._clauses.append(CreditPayClauseVO.from_alipay_dict(i))
    @property
    def discount_info(self):
        return self._discount_info

    @discount_info.setter
    def discount_info(self, value):
        if isinstance(value, CreditPayDiscountVO):
            self._discount_info = value
        else:
            self._discount_info = CreditPayDiscountVO.from_alipay_dict(value)
    @property
    def instal_itrv(self):
        return self._instal_itrv

    @instal_itrv.setter
    def instal_itrv(self, value):
        self._instal_itrv = value
    @property
    def instal_type(self):
        return self._instal_type

    @instal_type.setter
    def instal_type(self, value):
        self._instal_type = value
    @property
    def installment_id(self):
        return self._installment_id

    @installment_id.setter
    def installment_id(self, value):
        self._installment_id = value
    @property
    def int_pricing(self):
        return self._int_pricing

    @int_pricing.setter
    def int_pricing(self, value):
        if isinstance(value, CreditPayIntPricingVO):
            self._int_pricing = value
        else:
            self._int_pricing = CreditPayIntPricingVO.from_alipay_dict(value)
    @property
    def render_strategy(self):
        return self._render_strategy

    @render_strategy.setter
    def render_strategy(self, value):
        self._render_strategy = value
    @property
    def repay_info(self):
        return self._repay_info

    @repay_info.setter
    def repay_info(self, value):
        if isinstance(value, CreditPayRepayVO):
            self._repay_info = value
        else:
            self._repay_info = CreditPayRepayVO.from_alipay_dict(value)
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value
    @property
    def scheme_sign(self):
        return self._scheme_sign

    @scheme_sign.setter
    def scheme_sign(self, value):
        self._scheme_sign = value
    @property
    def term_info(self):
        return self._term_info

    @term_info.setter
    def term_info(self, value):
        if isinstance(value, CreditPayTermVO):
            self._term_info = value
        else:
            self._term_info = CreditPayTermVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.charge_pricing_list:
            if isinstance(self.charge_pricing_list, list):
                for i in range(0, len(self.charge_pricing_list)):
                    element = self.charge_pricing_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.charge_pricing_list[i] = element.to_alipay_dict()
            if hasattr(self.charge_pricing_list, 'to_alipay_dict'):
                params['charge_pricing_list'] = self.charge_pricing_list.to_alipay_dict()
            else:
                params['charge_pricing_list'] = self.charge_pricing_list
        if self.clauses:
            if isinstance(self.clauses, list):
                for i in range(0, len(self.clauses)):
                    element = self.clauses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.clauses[i] = element.to_alipay_dict()
            if hasattr(self.clauses, 'to_alipay_dict'):
                params['clauses'] = self.clauses.to_alipay_dict()
            else:
                params['clauses'] = self.clauses
        if self.discount_info:
            if hasattr(self.discount_info, 'to_alipay_dict'):
                params['discount_info'] = self.discount_info.to_alipay_dict()
            else:
                params['discount_info'] = self.discount_info
        if self.instal_itrv:
            if hasattr(self.instal_itrv, 'to_alipay_dict'):
                params['instal_itrv'] = self.instal_itrv.to_alipay_dict()
            else:
                params['instal_itrv'] = self.instal_itrv
        if self.instal_type:
            if hasattr(self.instal_type, 'to_alipay_dict'):
                params['instal_type'] = self.instal_type.to_alipay_dict()
            else:
                params['instal_type'] = self.instal_type
        if self.installment_id:
            if hasattr(self.installment_id, 'to_alipay_dict'):
                params['installment_id'] = self.installment_id.to_alipay_dict()
            else:
                params['installment_id'] = self.installment_id
        if self.int_pricing:
            if hasattr(self.int_pricing, 'to_alipay_dict'):
                params['int_pricing'] = self.int_pricing.to_alipay_dict()
            else:
                params['int_pricing'] = self.int_pricing
        if self.render_strategy:
            if hasattr(self.render_strategy, 'to_alipay_dict'):
                params['render_strategy'] = self.render_strategy.to_alipay_dict()
            else:
                params['render_strategy'] = self.render_strategy
        if self.repay_info:
            if hasattr(self.repay_info, 'to_alipay_dict'):
                params['repay_info'] = self.repay_info.to_alipay_dict()
            else:
                params['repay_info'] = self.repay_info
        if self.sale_pd_code:
            if hasattr(self.sale_pd_code, 'to_alipay_dict'):
                params['sale_pd_code'] = self.sale_pd_code.to_alipay_dict()
            else:
                params['sale_pd_code'] = self.sale_pd_code
        if self.scheme_sign:
            if hasattr(self.scheme_sign, 'to_alipay_dict'):
                params['scheme_sign'] = self.scheme_sign.to_alipay_dict()
            else:
                params['scheme_sign'] = self.scheme_sign
        if self.term_info:
            if hasattr(self.term_info, 'to_alipay_dict'):
                params['term_info'] = self.term_info.to_alipay_dict()
            else:
                params['term_info'] = self.term_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayInstallmentDetailVO()
        if 'charge_pricing_list' in d:
            o.charge_pricing_list = d['charge_pricing_list']
        if 'clauses' in d:
            o.clauses = d['clauses']
        if 'discount_info' in d:
            o.discount_info = d['discount_info']
        if 'instal_itrv' in d:
            o.instal_itrv = d['instal_itrv']
        if 'instal_type' in d:
            o.instal_type = d['instal_type']
        if 'installment_id' in d:
            o.installment_id = d['installment_id']
        if 'int_pricing' in d:
            o.int_pricing = d['int_pricing']
        if 'render_strategy' in d:
            o.render_strategy = d['render_strategy']
        if 'repay_info' in d:
            o.repay_info = d['repay_info']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'scheme_sign' in d:
            o.scheme_sign = d['scheme_sign']
        if 'term_info' in d:
            o.term_info = d['term_info']
        return o


