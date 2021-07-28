#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IntelligentGuideTradeDetail(object):

    def __init__(self):
        self._card_type = None
        self._customer_source = None
        self._customer_type = None
        self._date = None
        self._fifth_recommendation = None
        self._first_category = None
        self._first_recommendation = None
        self._fourth_recommendation = None
        self._guide_record_id = None
        self._item_name = None
        self._mobile = None
        self._original_price = None
        self._payment_type = None
        self._price = None
        self._second_category = None
        self._second_recommendation = None
        self._service_staff = None
        self._third_recommendation = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def customer_source(self):
        return self._customer_source

    @customer_source.setter
    def customer_source(self, value):
        self._customer_source = value
    @property
    def customer_type(self):
        return self._customer_type

    @customer_type.setter
    def customer_type(self, value):
        self._customer_type = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def fifth_recommendation(self):
        return self._fifth_recommendation

    @fifth_recommendation.setter
    def fifth_recommendation(self, value):
        self._fifth_recommendation = value
    @property
    def first_category(self):
        return self._first_category

    @first_category.setter
    def first_category(self, value):
        self._first_category = value
    @property
    def first_recommendation(self):
        return self._first_recommendation

    @first_recommendation.setter
    def first_recommendation(self, value):
        self._first_recommendation = value
    @property
    def fourth_recommendation(self):
        return self._fourth_recommendation

    @fourth_recommendation.setter
    def fourth_recommendation(self, value):
        self._fourth_recommendation = value
    @property
    def guide_record_id(self):
        return self._guide_record_id

    @guide_record_id.setter
    def guide_record_id(self, value):
        self._guide_record_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def second_category(self):
        return self._second_category

    @second_category.setter
    def second_category(self, value):
        self._second_category = value
    @property
    def second_recommendation(self):
        return self._second_recommendation

    @second_recommendation.setter
    def second_recommendation(self, value):
        self._second_recommendation = value
    @property
    def service_staff(self):
        return self._service_staff

    @service_staff.setter
    def service_staff(self, value):
        self._service_staff = value
    @property
    def third_recommendation(self):
        return self._third_recommendation

    @third_recommendation.setter
    def third_recommendation(self, value):
        self._third_recommendation = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.customer_source:
            if hasattr(self.customer_source, 'to_alipay_dict'):
                params['customer_source'] = self.customer_source.to_alipay_dict()
            else:
                params['customer_source'] = self.customer_source
        if self.customer_type:
            if hasattr(self.customer_type, 'to_alipay_dict'):
                params['customer_type'] = self.customer_type.to_alipay_dict()
            else:
                params['customer_type'] = self.customer_type
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.fifth_recommendation:
            if hasattr(self.fifth_recommendation, 'to_alipay_dict'):
                params['fifth_recommendation'] = self.fifth_recommendation.to_alipay_dict()
            else:
                params['fifth_recommendation'] = self.fifth_recommendation
        if self.first_category:
            if hasattr(self.first_category, 'to_alipay_dict'):
                params['first_category'] = self.first_category.to_alipay_dict()
            else:
                params['first_category'] = self.first_category
        if self.first_recommendation:
            if hasattr(self.first_recommendation, 'to_alipay_dict'):
                params['first_recommendation'] = self.first_recommendation.to_alipay_dict()
            else:
                params['first_recommendation'] = self.first_recommendation
        if self.fourth_recommendation:
            if hasattr(self.fourth_recommendation, 'to_alipay_dict'):
                params['fourth_recommendation'] = self.fourth_recommendation.to_alipay_dict()
            else:
                params['fourth_recommendation'] = self.fourth_recommendation
        if self.guide_record_id:
            if hasattr(self.guide_record_id, 'to_alipay_dict'):
                params['guide_record_id'] = self.guide_record_id.to_alipay_dict()
            else:
                params['guide_record_id'] = self.guide_record_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.second_category:
            if hasattr(self.second_category, 'to_alipay_dict'):
                params['second_category'] = self.second_category.to_alipay_dict()
            else:
                params['second_category'] = self.second_category
        if self.second_recommendation:
            if hasattr(self.second_recommendation, 'to_alipay_dict'):
                params['second_recommendation'] = self.second_recommendation.to_alipay_dict()
            else:
                params['second_recommendation'] = self.second_recommendation
        if self.service_staff:
            if hasattr(self.service_staff, 'to_alipay_dict'):
                params['service_staff'] = self.service_staff.to_alipay_dict()
            else:
                params['service_staff'] = self.service_staff
        if self.third_recommendation:
            if hasattr(self.third_recommendation, 'to_alipay_dict'):
                params['third_recommendation'] = self.third_recommendation.to_alipay_dict()
            else:
                params['third_recommendation'] = self.third_recommendation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntelligentGuideTradeDetail()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'customer_source' in d:
            o.customer_source = d['customer_source']
        if 'customer_type' in d:
            o.customer_type = d['customer_type']
        if 'date' in d:
            o.date = d['date']
        if 'fifth_recommendation' in d:
            o.fifth_recommendation = d['fifth_recommendation']
        if 'first_category' in d:
            o.first_category = d['first_category']
        if 'first_recommendation' in d:
            o.first_recommendation = d['first_recommendation']
        if 'fourth_recommendation' in d:
            o.fourth_recommendation = d['fourth_recommendation']
        if 'guide_record_id' in d:
            o.guide_record_id = d['guide_record_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'price' in d:
            o.price = d['price']
        if 'second_category' in d:
            o.second_category = d['second_category']
        if 'second_recommendation' in d:
            o.second_recommendation = d['second_recommendation']
        if 'service_staff' in d:
            o.service_staff = d['service_staff']
        if 'third_recommendation' in d:
            o.third_recommendation = d['third_recommendation']
        return o


