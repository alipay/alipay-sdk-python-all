#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsMktFactorDTO import InsMktFactorDTO
from alipay.aop.api.domain.InsMktCouponCmpgnBaseDTO import InsMktCouponCmpgnBaseDTO
from alipay.aop.api.domain.InsMktCouponBaseDTO import InsMktCouponBaseDTO
from alipay.aop.api.domain.InsMktObjectDTO import InsMktObjectDTO


class AlipayInsMarketingDiscountPreuseModel(object):

    def __init__(self):
        self._account_id = None
        self._account_type = None
        self._business_type = None
        self._factors = None
        self._market_types = None
        self._mkt_coupon_campaigns = None
        self._mkt_coupons = None
        self._mkt_objects = None
        self._request_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def factors(self):
        return self._factors

    @factors.setter
    def factors(self, value):
        if isinstance(value, list):
            self._factors = list()
            for i in value:
                if isinstance(i, InsMktFactorDTO):
                    self._factors.append(i)
                else:
                    self._factors.append(InsMktFactorDTO.from_alipay_dict(i))
    @property
    def market_types(self):
        return self._market_types

    @market_types.setter
    def market_types(self, value):
        if isinstance(value, list):
            self._market_types = list()
            for i in value:
                self._market_types.append(i)
    @property
    def mkt_coupon_campaigns(self):
        return self._mkt_coupon_campaigns

    @mkt_coupon_campaigns.setter
    def mkt_coupon_campaigns(self, value):
        if isinstance(value, list):
            self._mkt_coupon_campaigns = list()
            for i in value:
                if isinstance(i, InsMktCouponCmpgnBaseDTO):
                    self._mkt_coupon_campaigns.append(i)
                else:
                    self._mkt_coupon_campaigns.append(InsMktCouponCmpgnBaseDTO.from_alipay_dict(i))
    @property
    def mkt_coupons(self):
        return self._mkt_coupons

    @mkt_coupons.setter
    def mkt_coupons(self, value):
        if isinstance(value, list):
            self._mkt_coupons = list()
            for i in value:
                if isinstance(i, InsMktCouponBaseDTO):
                    self._mkt_coupons.append(i)
                else:
                    self._mkt_coupons.append(InsMktCouponBaseDTO.from_alipay_dict(i))
    @property
    def mkt_objects(self):
        return self._mkt_objects

    @mkt_objects.setter
    def mkt_objects(self, value):
        if isinstance(value, list):
            self._mkt_objects = list()
            for i in value:
                if isinstance(i, InsMktObjectDTO):
                    self._mkt_objects.append(i)
                else:
                    self._mkt_objects.append(InsMktObjectDTO.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.factors:
            if isinstance(self.factors, list):
                for i in range(0, len(self.factors)):
                    element = self.factors[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.factors[i] = element.to_alipay_dict()
            if hasattr(self.factors, 'to_alipay_dict'):
                params['factors'] = self.factors.to_alipay_dict()
            else:
                params['factors'] = self.factors
        if self.market_types:
            if isinstance(self.market_types, list):
                for i in range(0, len(self.market_types)):
                    element = self.market_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.market_types[i] = element.to_alipay_dict()
            if hasattr(self.market_types, 'to_alipay_dict'):
                params['market_types'] = self.market_types.to_alipay_dict()
            else:
                params['market_types'] = self.market_types
        if self.mkt_coupon_campaigns:
            if isinstance(self.mkt_coupon_campaigns, list):
                for i in range(0, len(self.mkt_coupon_campaigns)):
                    element = self.mkt_coupon_campaigns[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mkt_coupon_campaigns[i] = element.to_alipay_dict()
            if hasattr(self.mkt_coupon_campaigns, 'to_alipay_dict'):
                params['mkt_coupon_campaigns'] = self.mkt_coupon_campaigns.to_alipay_dict()
            else:
                params['mkt_coupon_campaigns'] = self.mkt_coupon_campaigns
        if self.mkt_coupons:
            if isinstance(self.mkt_coupons, list):
                for i in range(0, len(self.mkt_coupons)):
                    element = self.mkt_coupons[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mkt_coupons[i] = element.to_alipay_dict()
            if hasattr(self.mkt_coupons, 'to_alipay_dict'):
                params['mkt_coupons'] = self.mkt_coupons.to_alipay_dict()
            else:
                params['mkt_coupons'] = self.mkt_coupons
        if self.mkt_objects:
            if isinstance(self.mkt_objects, list):
                for i in range(0, len(self.mkt_objects)):
                    element = self.mkt_objects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mkt_objects[i] = element.to_alipay_dict()
            if hasattr(self.mkt_objects, 'to_alipay_dict'):
                params['mkt_objects'] = self.mkt_objects.to_alipay_dict()
            else:
                params['mkt_objects'] = self.mkt_objects
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingDiscountPreuseModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'factors' in d:
            o.factors = d['factors']
        if 'market_types' in d:
            o.market_types = d['market_types']
        if 'mkt_coupon_campaigns' in d:
            o.mkt_coupon_campaigns = d['mkt_coupon_campaigns']
        if 'mkt_coupons' in d:
            o.mkt_coupons = d['mkt_coupons']
        if 'mkt_objects' in d:
            o.mkt_objects = d['mkt_objects']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


