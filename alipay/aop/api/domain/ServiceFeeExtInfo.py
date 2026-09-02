#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceFeeExtInfo(object):

    def __init__(self):
        self._city_name = None
        self._origin_consume_amount = None
        self._origin_peer_pay_amount = None
        self._service_id = None
        self._settle_failed_code = None
        self._settle_failed_msg = None
        self._settle_failed_solution = None
        self._shop_id = None
        self._shop_name = None

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def origin_consume_amount(self):
        return self._origin_consume_amount

    @origin_consume_amount.setter
    def origin_consume_amount(self, value):
        self._origin_consume_amount = value
    @property
    def origin_peer_pay_amount(self):
        return self._origin_peer_pay_amount

    @origin_peer_pay_amount.setter
    def origin_peer_pay_amount(self, value):
        self._origin_peer_pay_amount = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def settle_failed_code(self):
        return self._settle_failed_code

    @settle_failed_code.setter
    def settle_failed_code(self, value):
        self._settle_failed_code = value
    @property
    def settle_failed_msg(self):
        return self._settle_failed_msg

    @settle_failed_msg.setter
    def settle_failed_msg(self, value):
        self._settle_failed_msg = value
    @property
    def settle_failed_solution(self):
        return self._settle_failed_solution

    @settle_failed_solution.setter
    def settle_failed_solution(self, value):
        self._settle_failed_solution = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.origin_consume_amount:
            if hasattr(self.origin_consume_amount, 'to_alipay_dict'):
                params['origin_consume_amount'] = self.origin_consume_amount.to_alipay_dict()
            else:
                params['origin_consume_amount'] = self.origin_consume_amount
        if self.origin_peer_pay_amount:
            if hasattr(self.origin_peer_pay_amount, 'to_alipay_dict'):
                params['origin_peer_pay_amount'] = self.origin_peer_pay_amount.to_alipay_dict()
            else:
                params['origin_peer_pay_amount'] = self.origin_peer_pay_amount
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.settle_failed_code:
            if hasattr(self.settle_failed_code, 'to_alipay_dict'):
                params['settle_failed_code'] = self.settle_failed_code.to_alipay_dict()
            else:
                params['settle_failed_code'] = self.settle_failed_code
        if self.settle_failed_msg:
            if hasattr(self.settle_failed_msg, 'to_alipay_dict'):
                params['settle_failed_msg'] = self.settle_failed_msg.to_alipay_dict()
            else:
                params['settle_failed_msg'] = self.settle_failed_msg
        if self.settle_failed_solution:
            if hasattr(self.settle_failed_solution, 'to_alipay_dict'):
                params['settle_failed_solution'] = self.settle_failed_solution.to_alipay_dict()
            else:
                params['settle_failed_solution'] = self.settle_failed_solution
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceFeeExtInfo()
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'origin_consume_amount' in d:
            o.origin_consume_amount = d['origin_consume_amount']
        if 'origin_peer_pay_amount' in d:
            o.origin_peer_pay_amount = d['origin_peer_pay_amount']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'settle_failed_code' in d:
            o.settle_failed_code = d['settle_failed_code']
        if 'settle_failed_msg' in d:
            o.settle_failed_msg = d['settle_failed_msg']
        if 'settle_failed_solution' in d:
            o.settle_failed_solution = d['settle_failed_solution']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


