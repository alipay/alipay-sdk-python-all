#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DcmealDishDetail import DcmealDishDetail
from alipay.aop.api.domain.DcmealPayDetail import DcmealPayDetail


class AlipayDigitalmgmtDcmealMightydataInfoSyncModel(object):

    def __init__(self):
        self._biz_time = None
        self._campus_name = None
        self._city_name = None
        self._dish_details = None
        self._meal_type = None
        self._open_id = None
        self._order_type = None
        self._pay_details = None
        self._pay_type = None
        self._restaurant_name = None
        self._shop_name = None
        self._term_document_id = None
        self._term_name = None
        self._total_amount = None
        self._trade_no = None
        self._user_id = None
        self._uuid = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def dish_details(self):
        return self._dish_details

    @dish_details.setter
    def dish_details(self, value):
        if isinstance(value, list):
            self._dish_details = list()
            for i in value:
                if isinstance(i, DcmealDishDetail):
                    self._dish_details.append(i)
                else:
                    self._dish_details.append(DcmealDishDetail.from_alipay_dict(i))
    @property
    def meal_type(self):
        return self._meal_type

    @meal_type.setter
    def meal_type(self, value):
        self._meal_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def pay_details(self):
        return self._pay_details

    @pay_details.setter
    def pay_details(self, value):
        if isinstance(value, list):
            self._pay_details = list()
            for i in value:
                if isinstance(i, DcmealPayDetail):
                    self._pay_details.append(i)
                else:
                    self._pay_details.append(DcmealPayDetail.from_alipay_dict(i))
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def restaurant_name(self):
        return self._restaurant_name

    @restaurant_name.setter
    def restaurant_name(self, value):
        self._restaurant_name = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def term_document_id(self):
        return self._term_document_id

    @term_document_id.setter
    def term_document_id(self, value):
        self._term_document_id = value
    @property
    def term_name(self):
        return self._term_name

    @term_name.setter
    def term_name(self, value):
        self._term_name = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.dish_details:
            if isinstance(self.dish_details, list):
                for i in range(0, len(self.dish_details)):
                    element = self.dish_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_details[i] = element.to_alipay_dict()
            if hasattr(self.dish_details, 'to_alipay_dict'):
                params['dish_details'] = self.dish_details.to_alipay_dict()
            else:
                params['dish_details'] = self.dish_details
        if self.meal_type:
            if hasattr(self.meal_type, 'to_alipay_dict'):
                params['meal_type'] = self.meal_type.to_alipay_dict()
            else:
                params['meal_type'] = self.meal_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.pay_details:
            if isinstance(self.pay_details, list):
                for i in range(0, len(self.pay_details)):
                    element = self.pay_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_details[i] = element.to_alipay_dict()
            if hasattr(self.pay_details, 'to_alipay_dict'):
                params['pay_details'] = self.pay_details.to_alipay_dict()
            else:
                params['pay_details'] = self.pay_details
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.restaurant_name:
            if hasattr(self.restaurant_name, 'to_alipay_dict'):
                params['restaurant_name'] = self.restaurant_name.to_alipay_dict()
            else:
                params['restaurant_name'] = self.restaurant_name
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.term_document_id:
            if hasattr(self.term_document_id, 'to_alipay_dict'):
                params['term_document_id'] = self.term_document_id.to_alipay_dict()
            else:
                params['term_document_id'] = self.term_document_id
        if self.term_name:
            if hasattr(self.term_name, 'to_alipay_dict'):
                params['term_name'] = self.term_name.to_alipay_dict()
            else:
                params['term_name'] = self.term_name
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtDcmealMightydataInfoSyncModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'dish_details' in d:
            o.dish_details = d['dish_details']
        if 'meal_type' in d:
            o.meal_type = d['meal_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'pay_details' in d:
            o.pay_details = d['pay_details']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'restaurant_name' in d:
            o.restaurant_name = d['restaurant_name']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'term_document_id' in d:
            o.term_document_id = d['term_document_id']
        if 'term_name' in d:
            o.term_name = d['term_name']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


