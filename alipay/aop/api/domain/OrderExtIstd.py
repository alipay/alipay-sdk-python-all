#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderExtIstd(object):

    def __init__(self):
        self._cash_on_delivery = None
        self._cash_on_pickup = None
        self._consumer_order_time = None
        self._delivery_direction = None
        self._delivery_type = None
        self._desc = None
        self._expected_delivery_time = None
        self._expected_finish_time = None
        self._expected_pick_time = None
        self._insure_price = None
        self._is_direct_delivery = None
        self._is_finish_code_needed = None
        self._is_insured = None
        self._is_pickup_code_needed = None
        self._poi_seq = None
        self._service_code = None

    @property
    def cash_on_delivery(self):
        return self._cash_on_delivery

    @cash_on_delivery.setter
    def cash_on_delivery(self, value):
        self._cash_on_delivery = value
    @property
    def cash_on_pickup(self):
        return self._cash_on_pickup

    @cash_on_pickup.setter
    def cash_on_pickup(self, value):
        self._cash_on_pickup = value
    @property
    def consumer_order_time(self):
        return self._consumer_order_time

    @consumer_order_time.setter
    def consumer_order_time(self, value):
        self._consumer_order_time = value
    @property
    def delivery_direction(self):
        return self._delivery_direction

    @delivery_direction.setter
    def delivery_direction(self, value):
        self._delivery_direction = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def expected_delivery_time(self):
        return self._expected_delivery_time

    @expected_delivery_time.setter
    def expected_delivery_time(self, value):
        self._expected_delivery_time = value
    @property
    def expected_finish_time(self):
        return self._expected_finish_time

    @expected_finish_time.setter
    def expected_finish_time(self, value):
        self._expected_finish_time = value
    @property
    def expected_pick_time(self):
        return self._expected_pick_time

    @expected_pick_time.setter
    def expected_pick_time(self, value):
        self._expected_pick_time = value
    @property
    def insure_price(self):
        return self._insure_price

    @insure_price.setter
    def insure_price(self, value):
        self._insure_price = value
    @property
    def is_direct_delivery(self):
        return self._is_direct_delivery

    @is_direct_delivery.setter
    def is_direct_delivery(self, value):
        self._is_direct_delivery = value
    @property
    def is_finish_code_needed(self):
        return self._is_finish_code_needed

    @is_finish_code_needed.setter
    def is_finish_code_needed(self, value):
        self._is_finish_code_needed = value
    @property
    def is_insured(self):
        return self._is_insured

    @is_insured.setter
    def is_insured(self, value):
        self._is_insured = value
    @property
    def is_pickup_code_needed(self):
        return self._is_pickup_code_needed

    @is_pickup_code_needed.setter
    def is_pickup_code_needed(self, value):
        self._is_pickup_code_needed = value
    @property
    def poi_seq(self):
        return self._poi_seq

    @poi_seq.setter
    def poi_seq(self, value):
        self._poi_seq = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.cash_on_delivery:
            if hasattr(self.cash_on_delivery, 'to_alipay_dict'):
                params['cash_on_delivery'] = self.cash_on_delivery.to_alipay_dict()
            else:
                params['cash_on_delivery'] = self.cash_on_delivery
        if self.cash_on_pickup:
            if hasattr(self.cash_on_pickup, 'to_alipay_dict'):
                params['cash_on_pickup'] = self.cash_on_pickup.to_alipay_dict()
            else:
                params['cash_on_pickup'] = self.cash_on_pickup
        if self.consumer_order_time:
            if hasattr(self.consumer_order_time, 'to_alipay_dict'):
                params['consumer_order_time'] = self.consumer_order_time.to_alipay_dict()
            else:
                params['consumer_order_time'] = self.consumer_order_time
        if self.delivery_direction:
            if hasattr(self.delivery_direction, 'to_alipay_dict'):
                params['delivery_direction'] = self.delivery_direction.to_alipay_dict()
            else:
                params['delivery_direction'] = self.delivery_direction
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.expected_delivery_time:
            if hasattr(self.expected_delivery_time, 'to_alipay_dict'):
                params['expected_delivery_time'] = self.expected_delivery_time.to_alipay_dict()
            else:
                params['expected_delivery_time'] = self.expected_delivery_time
        if self.expected_finish_time:
            if hasattr(self.expected_finish_time, 'to_alipay_dict'):
                params['expected_finish_time'] = self.expected_finish_time.to_alipay_dict()
            else:
                params['expected_finish_time'] = self.expected_finish_time
        if self.expected_pick_time:
            if hasattr(self.expected_pick_time, 'to_alipay_dict'):
                params['expected_pick_time'] = self.expected_pick_time.to_alipay_dict()
            else:
                params['expected_pick_time'] = self.expected_pick_time
        if self.insure_price:
            if hasattr(self.insure_price, 'to_alipay_dict'):
                params['insure_price'] = self.insure_price.to_alipay_dict()
            else:
                params['insure_price'] = self.insure_price
        if self.is_direct_delivery:
            if hasattr(self.is_direct_delivery, 'to_alipay_dict'):
                params['is_direct_delivery'] = self.is_direct_delivery.to_alipay_dict()
            else:
                params['is_direct_delivery'] = self.is_direct_delivery
        if self.is_finish_code_needed:
            if hasattr(self.is_finish_code_needed, 'to_alipay_dict'):
                params['is_finish_code_needed'] = self.is_finish_code_needed.to_alipay_dict()
            else:
                params['is_finish_code_needed'] = self.is_finish_code_needed
        if self.is_insured:
            if hasattr(self.is_insured, 'to_alipay_dict'):
                params['is_insured'] = self.is_insured.to_alipay_dict()
            else:
                params['is_insured'] = self.is_insured
        if self.is_pickup_code_needed:
            if hasattr(self.is_pickup_code_needed, 'to_alipay_dict'):
                params['is_pickup_code_needed'] = self.is_pickup_code_needed.to_alipay_dict()
            else:
                params['is_pickup_code_needed'] = self.is_pickup_code_needed
        if self.poi_seq:
            if hasattr(self.poi_seq, 'to_alipay_dict'):
                params['poi_seq'] = self.poi_seq.to_alipay_dict()
            else:
                params['poi_seq'] = self.poi_seq
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderExtIstd()
        if 'cash_on_delivery' in d:
            o.cash_on_delivery = d['cash_on_delivery']
        if 'cash_on_pickup' in d:
            o.cash_on_pickup = d['cash_on_pickup']
        if 'consumer_order_time' in d:
            o.consumer_order_time = d['consumer_order_time']
        if 'delivery_direction' in d:
            o.delivery_direction = d['delivery_direction']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'expected_delivery_time' in d:
            o.expected_delivery_time = d['expected_delivery_time']
        if 'expected_finish_time' in d:
            o.expected_finish_time = d['expected_finish_time']
        if 'expected_pick_time' in d:
            o.expected_pick_time = d['expected_pick_time']
        if 'insure_price' in d:
            o.insure_price = d['insure_price']
        if 'is_direct_delivery' in d:
            o.is_direct_delivery = d['is_direct_delivery']
        if 'is_finish_code_needed' in d:
            o.is_finish_code_needed = d['is_finish_code_needed']
        if 'is_insured' in d:
            o.is_insured = d['is_insured']
        if 'is_pickup_code_needed' in d:
            o.is_pickup_code_needed = d['is_pickup_code_needed']
        if 'poi_seq' in d:
            o.poi_seq = d['poi_seq']
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o


