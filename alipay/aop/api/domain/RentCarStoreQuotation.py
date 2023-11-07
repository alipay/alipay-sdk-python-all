#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarStoreQuotation(object):

    def __init__(self):
        self._comment_num = None
        self._comment_tag = None
        self._distance = None
        self._easy_card_usable_day_count = None
        self._isv_discount_amount = None
        self._latitude = None
        self._longitude = None
        self._quote_id = None
        self._service_score = None
        self._special_services = None
        self._store_code = None
        self._store_name = None
        self._supplier_name = None
        self._support_easy_card_order_ids = None
        self._total_amount = None
        self._unit_amount = None
        self._use_easy_card_total_amount = None

    @property
    def comment_num(self):
        return self._comment_num

    @comment_num.setter
    def comment_num(self, value):
        self._comment_num = value
    @property
    def comment_tag(self):
        return self._comment_tag

    @comment_tag.setter
    def comment_tag(self, value):
        self._comment_tag = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def easy_card_usable_day_count(self):
        return self._easy_card_usable_day_count

    @easy_card_usable_day_count.setter
    def easy_card_usable_day_count(self, value):
        self._easy_card_usable_day_count = value
    @property
    def isv_discount_amount(self):
        return self._isv_discount_amount

    @isv_discount_amount.setter
    def isv_discount_amount(self, value):
        self._isv_discount_amount = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, value):
        self._quote_id = value
    @property
    def service_score(self):
        return self._service_score

    @service_score.setter
    def service_score(self, value):
        self._service_score = value
    @property
    def special_services(self):
        return self._special_services

    @special_services.setter
    def special_services(self, value):
        if isinstance(value, list):
            self._special_services = list()
            for i in value:
                self._special_services.append(i)
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value):
        self._supplier_name = value
    @property
    def support_easy_card_order_ids(self):
        return self._support_easy_card_order_ids

    @support_easy_card_order_ids.setter
    def support_easy_card_order_ids(self, value):
        if isinstance(value, list):
            self._support_easy_card_order_ids = list()
            for i in value:
                self._support_easy_card_order_ids.append(i)
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self._unit_amount = value
    @property
    def use_easy_card_total_amount(self):
        return self._use_easy_card_total_amount

    @use_easy_card_total_amount.setter
    def use_easy_card_total_amount(self, value):
        self._use_easy_card_total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.comment_num:
            if hasattr(self.comment_num, 'to_alipay_dict'):
                params['comment_num'] = self.comment_num.to_alipay_dict()
            else:
                params['comment_num'] = self.comment_num
        if self.comment_tag:
            if hasattr(self.comment_tag, 'to_alipay_dict'):
                params['comment_tag'] = self.comment_tag.to_alipay_dict()
            else:
                params['comment_tag'] = self.comment_tag
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.easy_card_usable_day_count:
            if hasattr(self.easy_card_usable_day_count, 'to_alipay_dict'):
                params['easy_card_usable_day_count'] = self.easy_card_usable_day_count.to_alipay_dict()
            else:
                params['easy_card_usable_day_count'] = self.easy_card_usable_day_count
        if self.isv_discount_amount:
            if hasattr(self.isv_discount_amount, 'to_alipay_dict'):
                params['isv_discount_amount'] = self.isv_discount_amount.to_alipay_dict()
            else:
                params['isv_discount_amount'] = self.isv_discount_amount
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.quote_id:
            if hasattr(self.quote_id, 'to_alipay_dict'):
                params['quote_id'] = self.quote_id.to_alipay_dict()
            else:
                params['quote_id'] = self.quote_id
        if self.service_score:
            if hasattr(self.service_score, 'to_alipay_dict'):
                params['service_score'] = self.service_score.to_alipay_dict()
            else:
                params['service_score'] = self.service_score
        if self.special_services:
            if isinstance(self.special_services, list):
                for i in range(0, len(self.special_services)):
                    element = self.special_services[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_services[i] = element.to_alipay_dict()
            if hasattr(self.special_services, 'to_alipay_dict'):
                params['special_services'] = self.special_services.to_alipay_dict()
            else:
                params['special_services'] = self.special_services
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.supplier_name:
            if hasattr(self.supplier_name, 'to_alipay_dict'):
                params['supplier_name'] = self.supplier_name.to_alipay_dict()
            else:
                params['supplier_name'] = self.supplier_name
        if self.support_easy_card_order_ids:
            if isinstance(self.support_easy_card_order_ids, list):
                for i in range(0, len(self.support_easy_card_order_ids)):
                    element = self.support_easy_card_order_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.support_easy_card_order_ids[i] = element.to_alipay_dict()
            if hasattr(self.support_easy_card_order_ids, 'to_alipay_dict'):
                params['support_easy_card_order_ids'] = self.support_easy_card_order_ids.to_alipay_dict()
            else:
                params['support_easy_card_order_ids'] = self.support_easy_card_order_ids
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.unit_amount:
            if hasattr(self.unit_amount, 'to_alipay_dict'):
                params['unit_amount'] = self.unit_amount.to_alipay_dict()
            else:
                params['unit_amount'] = self.unit_amount
        if self.use_easy_card_total_amount:
            if hasattr(self.use_easy_card_total_amount, 'to_alipay_dict'):
                params['use_easy_card_total_amount'] = self.use_easy_card_total_amount.to_alipay_dict()
            else:
                params['use_easy_card_total_amount'] = self.use_easy_card_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarStoreQuotation()
        if 'comment_num' in d:
            o.comment_num = d['comment_num']
        if 'comment_tag' in d:
            o.comment_tag = d['comment_tag']
        if 'distance' in d:
            o.distance = d['distance']
        if 'easy_card_usable_day_count' in d:
            o.easy_card_usable_day_count = d['easy_card_usable_day_count']
        if 'isv_discount_amount' in d:
            o.isv_discount_amount = d['isv_discount_amount']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'service_score' in d:
            o.service_score = d['service_score']
        if 'special_services' in d:
            o.special_services = d['special_services']
        if 'store_code' in d:
            o.store_code = d['store_code']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'supplier_name' in d:
            o.supplier_name = d['supplier_name']
        if 'support_easy_card_order_ids' in d:
            o.support_easy_card_order_ids = d['support_easy_card_order_ids']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        if 'use_easy_card_total_amount' in d:
            o.use_easy_card_total_amount = d['use_easy_card_total_amount']
        return o


