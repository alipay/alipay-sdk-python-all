#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantPromoDetailInfoVO import MerchantPromoDetailInfoVO
from alipay.aop.api.domain.PlatformPromoDetailInfoVO import PlatformPromoDetailInfoVO


class InstallmentPlanPromoDetailInfoVO(object):

    def __init__(self):
        self._merchant_promo_amount = None
        self._merchant_promo_detail = None
        self._plan_pay_amount = None
        self._plan_pay_no = None
        self._platform_promo_amount = None
        self._platform_promo_detail = None
        self._promo_amount = None

    @property
    def merchant_promo_amount(self):
        return self._merchant_promo_amount

    @merchant_promo_amount.setter
    def merchant_promo_amount(self, value):
        self._merchant_promo_amount = value
    @property
    def merchant_promo_detail(self):
        return self._merchant_promo_detail

    @merchant_promo_detail.setter
    def merchant_promo_detail(self, value):
        if isinstance(value, MerchantPromoDetailInfoVO):
            self._merchant_promo_detail = value
        else:
            self._merchant_promo_detail = MerchantPromoDetailInfoVO.from_alipay_dict(value)
    @property
    def plan_pay_amount(self):
        return self._plan_pay_amount

    @plan_pay_amount.setter
    def plan_pay_amount(self, value):
        self._plan_pay_amount = value
    @property
    def plan_pay_no(self):
        return self._plan_pay_no

    @plan_pay_no.setter
    def plan_pay_no(self, value):
        self._plan_pay_no = value
    @property
    def platform_promo_amount(self):
        return self._platform_promo_amount

    @platform_promo_amount.setter
    def platform_promo_amount(self, value):
        self._platform_promo_amount = value
    @property
    def platform_promo_detail(self):
        return self._platform_promo_detail

    @platform_promo_detail.setter
    def platform_promo_detail(self, value):
        if isinstance(value, PlatformPromoDetailInfoVO):
            self._platform_promo_detail = value
        else:
            self._platform_promo_detail = PlatformPromoDetailInfoVO.from_alipay_dict(value)
    @property
    def promo_amount(self):
        return self._promo_amount

    @promo_amount.setter
    def promo_amount(self, value):
        self._promo_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_promo_amount:
            if hasattr(self.merchant_promo_amount, 'to_alipay_dict'):
                params['merchant_promo_amount'] = self.merchant_promo_amount.to_alipay_dict()
            else:
                params['merchant_promo_amount'] = self.merchant_promo_amount
        if self.merchant_promo_detail:
            if hasattr(self.merchant_promo_detail, 'to_alipay_dict'):
                params['merchant_promo_detail'] = self.merchant_promo_detail.to_alipay_dict()
            else:
                params['merchant_promo_detail'] = self.merchant_promo_detail
        if self.plan_pay_amount:
            if hasattr(self.plan_pay_amount, 'to_alipay_dict'):
                params['plan_pay_amount'] = self.plan_pay_amount.to_alipay_dict()
            else:
                params['plan_pay_amount'] = self.plan_pay_amount
        if self.plan_pay_no:
            if hasattr(self.plan_pay_no, 'to_alipay_dict'):
                params['plan_pay_no'] = self.plan_pay_no.to_alipay_dict()
            else:
                params['plan_pay_no'] = self.plan_pay_no
        if self.platform_promo_amount:
            if hasattr(self.platform_promo_amount, 'to_alipay_dict'):
                params['platform_promo_amount'] = self.platform_promo_amount.to_alipay_dict()
            else:
                params['platform_promo_amount'] = self.platform_promo_amount
        if self.platform_promo_detail:
            if hasattr(self.platform_promo_detail, 'to_alipay_dict'):
                params['platform_promo_detail'] = self.platform_promo_detail.to_alipay_dict()
            else:
                params['platform_promo_detail'] = self.platform_promo_detail
        if self.promo_amount:
            if hasattr(self.promo_amount, 'to_alipay_dict'):
                params['promo_amount'] = self.promo_amount.to_alipay_dict()
            else:
                params['promo_amount'] = self.promo_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentPlanPromoDetailInfoVO()
        if 'merchant_promo_amount' in d:
            o.merchant_promo_amount = d['merchant_promo_amount']
        if 'merchant_promo_detail' in d:
            o.merchant_promo_detail = d['merchant_promo_detail']
        if 'plan_pay_amount' in d:
            o.plan_pay_amount = d['plan_pay_amount']
        if 'plan_pay_no' in d:
            o.plan_pay_no = d['plan_pay_no']
        if 'platform_promo_amount' in d:
            o.platform_promo_amount = d['platform_promo_amount']
        if 'platform_promo_detail' in d:
            o.platform_promo_detail = d['platform_promo_detail']
        if 'promo_amount' in d:
            o.promo_amount = d['promo_amount']
        return o


