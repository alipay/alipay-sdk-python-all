#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsProduct import InsProduct
from alipay.aop.api.domain.Car import Car
from alipay.aop.api.domain.CarModel import CarModel
from alipay.aop.api.domain.InsProduct import InsProduct


class AlipayInsAutoAutoinsprodQuoteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoinsprodQuoteQueryResponse, self).__init__()
        self._biz_discount = None
        self._biz_renewal_flag = None
        self._biz_renewal_org = None
        self._business_premium = None
        self._business_product = None
        self._car = None
        self._car_owner_grade = None
        self._check_code = None
        self._check_code_id = None
        self._check_code_type = None
        self._com_id = None
        self._com_name = None
        self._correct_car_models = None
        self._enquiry_biz_id = None
        self._force_discount = None
        self._force_premium = None
        self._force_product = None
        self._force_renewal_flag = None
        self._force_renewal_org = None
        self._logistics_models = None
        self._max_self_channel_ratio = None
        self._max_self_underwrite_ratio = None
        self._min_self_channel_ratio = None
        self._min_self_underwrite_ratio = None
        self._no_claim_adjust_ratio = None
        self._quote_biz_id = None
        self._quote_error_code = None
        self._quote_error_msg = None
        self._real_premium = None
        self._reduce_premium = None
        self._self_channel_ratio = None
        self._self_underwrite_ratio = None
        self._total_premium = None
        self._traffic_violation_ratio = None
        self._user_level = None
        self._warn_code = None
        self._warn_message = None

    @property
    def biz_discount(self):
        return self._biz_discount

    @biz_discount.setter
    def biz_discount(self, value):
        self._biz_discount = value
    @property
    def biz_renewal_flag(self):
        return self._biz_renewal_flag

    @biz_renewal_flag.setter
    def biz_renewal_flag(self, value):
        self._biz_renewal_flag = value
    @property
    def biz_renewal_org(self):
        return self._biz_renewal_org

    @biz_renewal_org.setter
    def biz_renewal_org(self, value):
        self._biz_renewal_org = value
    @property
    def business_premium(self):
        return self._business_premium

    @business_premium.setter
    def business_premium(self, value):
        self._business_premium = value
    @property
    def business_product(self):
        return self._business_product

    @business_product.setter
    def business_product(self, value):
        if isinstance(value, InsProduct):
            self._business_product = value
        else:
            self._business_product = InsProduct.from_alipay_dict(value)
    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        if isinstance(value, Car):
            self._car = value
        else:
            self._car = Car.from_alipay_dict(value)
    @property
    def car_owner_grade(self):
        return self._car_owner_grade

    @car_owner_grade.setter
    def car_owner_grade(self, value):
        self._car_owner_grade = value
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def check_code_id(self):
        return self._check_code_id

    @check_code_id.setter
    def check_code_id(self, value):
        self._check_code_id = value
    @property
    def check_code_type(self):
        return self._check_code_type

    @check_code_type.setter
    def check_code_type(self, value):
        self._check_code_type = value
    @property
    def com_id(self):
        return self._com_id

    @com_id.setter
    def com_id(self, value):
        self._com_id = value
    @property
    def com_name(self):
        return self._com_name

    @com_name.setter
    def com_name(self, value):
        self._com_name = value
    @property
    def correct_car_models(self):
        return self._correct_car_models

    @correct_car_models.setter
    def correct_car_models(self, value):
        if isinstance(value, list):
            self._correct_car_models = list()
            for i in value:
                if isinstance(i, CarModel):
                    self._correct_car_models.append(i)
                else:
                    self._correct_car_models.append(CarModel.from_alipay_dict(i))
    @property
    def enquiry_biz_id(self):
        return self._enquiry_biz_id

    @enquiry_biz_id.setter
    def enquiry_biz_id(self, value):
        self._enquiry_biz_id = value
    @property
    def force_discount(self):
        return self._force_discount

    @force_discount.setter
    def force_discount(self, value):
        self._force_discount = value
    @property
    def force_premium(self):
        return self._force_premium

    @force_premium.setter
    def force_premium(self, value):
        self._force_premium = value
    @property
    def force_product(self):
        return self._force_product

    @force_product.setter
    def force_product(self, value):
        if isinstance(value, InsProduct):
            self._force_product = value
        else:
            self._force_product = InsProduct.from_alipay_dict(value)
    @property
    def force_renewal_flag(self):
        return self._force_renewal_flag

    @force_renewal_flag.setter
    def force_renewal_flag(self, value):
        self._force_renewal_flag = value
    @property
    def force_renewal_org(self):
        return self._force_renewal_org

    @force_renewal_org.setter
    def force_renewal_org(self, value):
        self._force_renewal_org = value
    @property
    def logistics_models(self):
        return self._logistics_models

    @logistics_models.setter
    def logistics_models(self, value):
        if isinstance(value, list):
            self._logistics_models = list()
            for i in value:
                self._logistics_models.append(i)
    @property
    def max_self_channel_ratio(self):
        return self._max_self_channel_ratio

    @max_self_channel_ratio.setter
    def max_self_channel_ratio(self, value):
        self._max_self_channel_ratio = value
    @property
    def max_self_underwrite_ratio(self):
        return self._max_self_underwrite_ratio

    @max_self_underwrite_ratio.setter
    def max_self_underwrite_ratio(self, value):
        self._max_self_underwrite_ratio = value
    @property
    def min_self_channel_ratio(self):
        return self._min_self_channel_ratio

    @min_self_channel_ratio.setter
    def min_self_channel_ratio(self, value):
        self._min_self_channel_ratio = value
    @property
    def min_self_underwrite_ratio(self):
        return self._min_self_underwrite_ratio

    @min_self_underwrite_ratio.setter
    def min_self_underwrite_ratio(self, value):
        self._min_self_underwrite_ratio = value
    @property
    def no_claim_adjust_ratio(self):
        return self._no_claim_adjust_ratio

    @no_claim_adjust_ratio.setter
    def no_claim_adjust_ratio(self, value):
        self._no_claim_adjust_ratio = value
    @property
    def quote_biz_id(self):
        return self._quote_biz_id

    @quote_biz_id.setter
    def quote_biz_id(self, value):
        self._quote_biz_id = value
    @property
    def quote_error_code(self):
        return self._quote_error_code

    @quote_error_code.setter
    def quote_error_code(self, value):
        self._quote_error_code = value
    @property
    def quote_error_msg(self):
        return self._quote_error_msg

    @quote_error_msg.setter
    def quote_error_msg(self, value):
        self._quote_error_msg = value
    @property
    def real_premium(self):
        return self._real_premium

    @real_premium.setter
    def real_premium(self, value):
        self._real_premium = value
    @property
    def reduce_premium(self):
        return self._reduce_premium

    @reduce_premium.setter
    def reduce_premium(self, value):
        self._reduce_premium = value
    @property
    def self_channel_ratio(self):
        return self._self_channel_ratio

    @self_channel_ratio.setter
    def self_channel_ratio(self, value):
        self._self_channel_ratio = value
    @property
    def self_underwrite_ratio(self):
        return self._self_underwrite_ratio

    @self_underwrite_ratio.setter
    def self_underwrite_ratio(self, value):
        self._self_underwrite_ratio = value
    @property
    def total_premium(self):
        return self._total_premium

    @total_premium.setter
    def total_premium(self, value):
        self._total_premium = value
    @property
    def traffic_violation_ratio(self):
        return self._traffic_violation_ratio

    @traffic_violation_ratio.setter
    def traffic_violation_ratio(self, value):
        self._traffic_violation_ratio = value
    @property
    def user_level(self):
        return self._user_level

    @user_level.setter
    def user_level(self, value):
        self._user_level = value
    @property
    def warn_code(self):
        return self._warn_code

    @warn_code.setter
    def warn_code(self, value):
        self._warn_code = value
    @property
    def warn_message(self):
        return self._warn_message

    @warn_message.setter
    def warn_message(self, value):
        self._warn_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoinsprodQuoteQueryResponse, self).parse_response_content(response_content)
        if 'biz_discount' in response:
            self.biz_discount = response['biz_discount']
        if 'biz_renewal_flag' in response:
            self.biz_renewal_flag = response['biz_renewal_flag']
        if 'biz_renewal_org' in response:
            self.biz_renewal_org = response['biz_renewal_org']
        if 'business_premium' in response:
            self.business_premium = response['business_premium']
        if 'business_product' in response:
            self.business_product = response['business_product']
        if 'car' in response:
            self.car = response['car']
        if 'car_owner_grade' in response:
            self.car_owner_grade = response['car_owner_grade']
        if 'check_code' in response:
            self.check_code = response['check_code']
        if 'check_code_id' in response:
            self.check_code_id = response['check_code_id']
        if 'check_code_type' in response:
            self.check_code_type = response['check_code_type']
        if 'com_id' in response:
            self.com_id = response['com_id']
        if 'com_name' in response:
            self.com_name = response['com_name']
        if 'correct_car_models' in response:
            self.correct_car_models = response['correct_car_models']
        if 'enquiry_biz_id' in response:
            self.enquiry_biz_id = response['enquiry_biz_id']
        if 'force_discount' in response:
            self.force_discount = response['force_discount']
        if 'force_premium' in response:
            self.force_premium = response['force_premium']
        if 'force_product' in response:
            self.force_product = response['force_product']
        if 'force_renewal_flag' in response:
            self.force_renewal_flag = response['force_renewal_flag']
        if 'force_renewal_org' in response:
            self.force_renewal_org = response['force_renewal_org']
        if 'logistics_models' in response:
            self.logistics_models = response['logistics_models']
        if 'max_self_channel_ratio' in response:
            self.max_self_channel_ratio = response['max_self_channel_ratio']
        if 'max_self_underwrite_ratio' in response:
            self.max_self_underwrite_ratio = response['max_self_underwrite_ratio']
        if 'min_self_channel_ratio' in response:
            self.min_self_channel_ratio = response['min_self_channel_ratio']
        if 'min_self_underwrite_ratio' in response:
            self.min_self_underwrite_ratio = response['min_self_underwrite_ratio']
        if 'no_claim_adjust_ratio' in response:
            self.no_claim_adjust_ratio = response['no_claim_adjust_ratio']
        if 'quote_biz_id' in response:
            self.quote_biz_id = response['quote_biz_id']
        if 'quote_error_code' in response:
            self.quote_error_code = response['quote_error_code']
        if 'quote_error_msg' in response:
            self.quote_error_msg = response['quote_error_msg']
        if 'real_premium' in response:
            self.real_premium = response['real_premium']
        if 'reduce_premium' in response:
            self.reduce_premium = response['reduce_premium']
        if 'self_channel_ratio' in response:
            self.self_channel_ratio = response['self_channel_ratio']
        if 'self_underwrite_ratio' in response:
            self.self_underwrite_ratio = response['self_underwrite_ratio']
        if 'total_premium' in response:
            self.total_premium = response['total_premium']
        if 'traffic_violation_ratio' in response:
            self.traffic_violation_ratio = response['traffic_violation_ratio']
        if 'user_level' in response:
            self.user_level = response['user_level']
        if 'warn_code' in response:
            self.warn_code = response['warn_code']
        if 'warn_message' in response:
            self.warn_message = response['warn_message']
