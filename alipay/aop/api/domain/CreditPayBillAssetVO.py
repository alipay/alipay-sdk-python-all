#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayAssetBaseVO import CreditPayAssetBaseVO
from alipay.aop.api.domain.CreditPayChargePricingVO import CreditPayChargePricingVO
from alipay.aop.api.domain.CreditPayClauseVO import CreditPayClauseVO
from alipay.aop.api.domain.CreditPayDiscountVO import CreditPayDiscountVO
from alipay.aop.api.domain.CreditPayIntPricingVO import CreditPayIntPricingVO
from alipay.aop.api.domain.CreditPayRepayVO import CreditPayRepayVO
from alipay.aop.api.domain.CreditPayTermVO import CreditPayTermVO


class CreditPayBillAssetVO(object):

    def __init__(self):
        self._allow_part_prepayment = None
        self._allow_prepayment = None
        self._base_info = None
        self._bill_account_day = None
        self._bill_account_day_unit = None
        self._bill_pd_code = None
        self._charge_pricing_list = None
        self._clauses = None
        self._discount_info = None
        self._int_pricing = None
        self._repay_info = None
        self._term_info = None

    @property
    def allow_part_prepayment(self):
        return self._allow_part_prepayment

    @allow_part_prepayment.setter
    def allow_part_prepayment(self, value):
        self._allow_part_prepayment = value
    @property
    def allow_prepayment(self):
        return self._allow_prepayment

    @allow_prepayment.setter
    def allow_prepayment(self, value):
        self._allow_prepayment = value
    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, CreditPayAssetBaseVO):
            self._base_info = value
        else:
            self._base_info = CreditPayAssetBaseVO.from_alipay_dict(value)
    @property
    def bill_account_day(self):
        return self._bill_account_day

    @bill_account_day.setter
    def bill_account_day(self, value):
        self._bill_account_day = value
    @property
    def bill_account_day_unit(self):
        return self._bill_account_day_unit

    @bill_account_day_unit.setter
    def bill_account_day_unit(self, value):
        self._bill_account_day_unit = value
    @property
    def bill_pd_code(self):
        return self._bill_pd_code

    @bill_pd_code.setter
    def bill_pd_code(self, value):
        self._bill_pd_code = value
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
    def int_pricing(self):
        return self._int_pricing

    @int_pricing.setter
    def int_pricing(self, value):
        if isinstance(value, CreditPayIntPricingVO):
            self._int_pricing = value
        else:
            self._int_pricing = CreditPayIntPricingVO.from_alipay_dict(value)
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
        if self.allow_part_prepayment:
            if hasattr(self.allow_part_prepayment, 'to_alipay_dict'):
                params['allow_part_prepayment'] = self.allow_part_prepayment.to_alipay_dict()
            else:
                params['allow_part_prepayment'] = self.allow_part_prepayment
        if self.allow_prepayment:
            if hasattr(self.allow_prepayment, 'to_alipay_dict'):
                params['allow_prepayment'] = self.allow_prepayment.to_alipay_dict()
            else:
                params['allow_prepayment'] = self.allow_prepayment
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.bill_account_day:
            if hasattr(self.bill_account_day, 'to_alipay_dict'):
                params['bill_account_day'] = self.bill_account_day.to_alipay_dict()
            else:
                params['bill_account_day'] = self.bill_account_day
        if self.bill_account_day_unit:
            if hasattr(self.bill_account_day_unit, 'to_alipay_dict'):
                params['bill_account_day_unit'] = self.bill_account_day_unit.to_alipay_dict()
            else:
                params['bill_account_day_unit'] = self.bill_account_day_unit
        if self.bill_pd_code:
            if hasattr(self.bill_pd_code, 'to_alipay_dict'):
                params['bill_pd_code'] = self.bill_pd_code.to_alipay_dict()
            else:
                params['bill_pd_code'] = self.bill_pd_code
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
        if self.int_pricing:
            if hasattr(self.int_pricing, 'to_alipay_dict'):
                params['int_pricing'] = self.int_pricing.to_alipay_dict()
            else:
                params['int_pricing'] = self.int_pricing
        if self.repay_info:
            if hasattr(self.repay_info, 'to_alipay_dict'):
                params['repay_info'] = self.repay_info.to_alipay_dict()
            else:
                params['repay_info'] = self.repay_info
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
        o = CreditPayBillAssetVO()
        if 'allow_part_prepayment' in d:
            o.allow_part_prepayment = d['allow_part_prepayment']
        if 'allow_prepayment' in d:
            o.allow_prepayment = d['allow_prepayment']
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'bill_account_day' in d:
            o.bill_account_day = d['bill_account_day']
        if 'bill_account_day_unit' in d:
            o.bill_account_day_unit = d['bill_account_day_unit']
        if 'bill_pd_code' in d:
            o.bill_pd_code = d['bill_pd_code']
        if 'charge_pricing_list' in d:
            o.charge_pricing_list = d['charge_pricing_list']
        if 'clauses' in d:
            o.clauses = d['clauses']
        if 'discount_info' in d:
            o.discount_info = d['discount_info']
        if 'int_pricing' in d:
            o.int_pricing = d['int_pricing']
        if 'repay_info' in d:
            o.repay_info = d['repay_info']
        if 'term_info' in d:
            o.term_info = d['term_info']
        return o


