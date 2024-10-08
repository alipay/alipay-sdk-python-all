#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantPromoDetailInfoVO import MerchantPromoDetailInfoVO
from alipay.aop.api.domain.PlatformPromoDetailInfoVO import PlatformPromoDetailInfoVO
from alipay.aop.api.domain.StagePromoDetailInfoVO import StagePromoDetailInfoVO


class PromoInfoVO(object):

    def __init__(self):
        self._merchant_promo_detail = None
        self._merchant_total_amount = None
        self._order_amount = None
        self._order_promo_sale_amount = None
        self._platform_promo_detail = None
        self._platform_total_amount = None
        self._stage_promo_detail_list = None
        self._total_amount = None

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
    def merchant_total_amount(self):
        return self._merchant_total_amount

    @merchant_total_amount.setter
    def merchant_total_amount(self, value):
        self._merchant_total_amount = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_promo_sale_amount(self):
        return self._order_promo_sale_amount

    @order_promo_sale_amount.setter
    def order_promo_sale_amount(self, value):
        self._order_promo_sale_amount = value
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
    def platform_total_amount(self):
        return self._platform_total_amount

    @platform_total_amount.setter
    def platform_total_amount(self, value):
        self._platform_total_amount = value
    @property
    def stage_promo_detail_list(self):
        return self._stage_promo_detail_list

    @stage_promo_detail_list.setter
    def stage_promo_detail_list(self, value):
        if isinstance(value, list):
            self._stage_promo_detail_list = list()
            for i in value:
                if isinstance(i, StagePromoDetailInfoVO):
                    self._stage_promo_detail_list.append(i)
                else:
                    self._stage_promo_detail_list.append(StagePromoDetailInfoVO.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_promo_detail:
            if hasattr(self.merchant_promo_detail, 'to_alipay_dict'):
                params['merchant_promo_detail'] = self.merchant_promo_detail.to_alipay_dict()
            else:
                params['merchant_promo_detail'] = self.merchant_promo_detail
        if self.merchant_total_amount:
            if hasattr(self.merchant_total_amount, 'to_alipay_dict'):
                params['merchant_total_amount'] = self.merchant_total_amount.to_alipay_dict()
            else:
                params['merchant_total_amount'] = self.merchant_total_amount
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_promo_sale_amount:
            if hasattr(self.order_promo_sale_amount, 'to_alipay_dict'):
                params['order_promo_sale_amount'] = self.order_promo_sale_amount.to_alipay_dict()
            else:
                params['order_promo_sale_amount'] = self.order_promo_sale_amount
        if self.platform_promo_detail:
            if hasattr(self.platform_promo_detail, 'to_alipay_dict'):
                params['platform_promo_detail'] = self.platform_promo_detail.to_alipay_dict()
            else:
                params['platform_promo_detail'] = self.platform_promo_detail
        if self.platform_total_amount:
            if hasattr(self.platform_total_amount, 'to_alipay_dict'):
                params['platform_total_amount'] = self.platform_total_amount.to_alipay_dict()
            else:
                params['platform_total_amount'] = self.platform_total_amount
        if self.stage_promo_detail_list:
            if isinstance(self.stage_promo_detail_list, list):
                for i in range(0, len(self.stage_promo_detail_list)):
                    element = self.stage_promo_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stage_promo_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.stage_promo_detail_list, 'to_alipay_dict'):
                params['stage_promo_detail_list'] = self.stage_promo_detail_list.to_alipay_dict()
            else:
                params['stage_promo_detail_list'] = self.stage_promo_detail_list
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoInfoVO()
        if 'merchant_promo_detail' in d:
            o.merchant_promo_detail = d['merchant_promo_detail']
        if 'merchant_total_amount' in d:
            o.merchant_total_amount = d['merchant_total_amount']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_promo_sale_amount' in d:
            o.order_promo_sale_amount = d['order_promo_sale_amount']
        if 'platform_promo_detail' in d:
            o.platform_promo_detail = d['platform_promo_detail']
        if 'platform_total_amount' in d:
            o.platform_total_amount = d['platform_total_amount']
        if 'stage_promo_detail_list' in d:
            o.stage_promo_detail_list = d['stage_promo_detail_list']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


