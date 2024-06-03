#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BookingRule import BookingRule
from alipay.aop.api.domain.HotelPromotionStaticInfo import HotelPromotionStaticInfo
from alipay.aop.api.domain.RatePlan import RatePlan
from alipay.aop.api.domain.RefundRule import RefundRule


class AlipayCommerceHotelRateplanUploadModel(object):

    def __init__(self):
        self._booking_rules = None
        self._hotel_id = None
        self._increment = None
        self._promotion_static_info_list = None
        self._rate_plans = None
        self._refund_rules = None

    @property
    def booking_rules(self):
        return self._booking_rules

    @booking_rules.setter
    def booking_rules(self, value):
        if isinstance(value, list):
            self._booking_rules = list()
            for i in value:
                if isinstance(i, BookingRule):
                    self._booking_rules.append(i)
                else:
                    self._booking_rules.append(BookingRule.from_alipay_dict(i))
    @property
    def hotel_id(self):
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, value):
        self._hotel_id = value
    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        self._increment = value
    @property
    def promotion_static_info_list(self):
        return self._promotion_static_info_list

    @promotion_static_info_list.setter
    def promotion_static_info_list(self, value):
        if isinstance(value, list):
            self._promotion_static_info_list = list()
            for i in value:
                if isinstance(i, HotelPromotionStaticInfo):
                    self._promotion_static_info_list.append(i)
                else:
                    self._promotion_static_info_list.append(HotelPromotionStaticInfo.from_alipay_dict(i))
    @property
    def rate_plans(self):
        return self._rate_plans

    @rate_plans.setter
    def rate_plans(self, value):
        if isinstance(value, list):
            self._rate_plans = list()
            for i in value:
                if isinstance(i, RatePlan):
                    self._rate_plans.append(i)
                else:
                    self._rate_plans.append(RatePlan.from_alipay_dict(i))
    @property
    def refund_rules(self):
        return self._refund_rules

    @refund_rules.setter
    def refund_rules(self, value):
        if isinstance(value, list):
            self._refund_rules = list()
            for i in value:
                if isinstance(i, RefundRule):
                    self._refund_rules.append(i)
                else:
                    self._refund_rules.append(RefundRule.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.booking_rules:
            if isinstance(self.booking_rules, list):
                for i in range(0, len(self.booking_rules)):
                    element = self.booking_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.booking_rules[i] = element.to_alipay_dict()
            if hasattr(self.booking_rules, 'to_alipay_dict'):
                params['booking_rules'] = self.booking_rules.to_alipay_dict()
            else:
                params['booking_rules'] = self.booking_rules
        if self.hotel_id:
            if hasattr(self.hotel_id, 'to_alipay_dict'):
                params['hotel_id'] = self.hotel_id.to_alipay_dict()
            else:
                params['hotel_id'] = self.hotel_id
        if self.increment:
            if hasattr(self.increment, 'to_alipay_dict'):
                params['increment'] = self.increment.to_alipay_dict()
            else:
                params['increment'] = self.increment
        if self.promotion_static_info_list:
            if isinstance(self.promotion_static_info_list, list):
                for i in range(0, len(self.promotion_static_info_list)):
                    element = self.promotion_static_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promotion_static_info_list[i] = element.to_alipay_dict()
            if hasattr(self.promotion_static_info_list, 'to_alipay_dict'):
                params['promotion_static_info_list'] = self.promotion_static_info_list.to_alipay_dict()
            else:
                params['promotion_static_info_list'] = self.promotion_static_info_list
        if self.rate_plans:
            if isinstance(self.rate_plans, list):
                for i in range(0, len(self.rate_plans)):
                    element = self.rate_plans[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rate_plans[i] = element.to_alipay_dict()
            if hasattr(self.rate_plans, 'to_alipay_dict'):
                params['rate_plans'] = self.rate_plans.to_alipay_dict()
            else:
                params['rate_plans'] = self.rate_plans
        if self.refund_rules:
            if isinstance(self.refund_rules, list):
                for i in range(0, len(self.refund_rules)):
                    element = self.refund_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_rules[i] = element.to_alipay_dict()
            if hasattr(self.refund_rules, 'to_alipay_dict'):
                params['refund_rules'] = self.refund_rules.to_alipay_dict()
            else:
                params['refund_rules'] = self.refund_rules
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelRateplanUploadModel()
        if 'booking_rules' in d:
            o.booking_rules = d['booking_rules']
        if 'hotel_id' in d:
            o.hotel_id = d['hotel_id']
        if 'increment' in d:
            o.increment = d['increment']
        if 'promotion_static_info_list' in d:
            o.promotion_static_info_list = d['promotion_static_info_list']
        if 'rate_plans' in d:
            o.rate_plans = d['rate_plans']
        if 'refund_rules' in d:
            o.refund_rules = d['refund_rules']
        return o


