#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LifeServiceTailPaymentServiceProgram import LifeServiceTailPaymentServiceProgram


class AlipayCommerceMerchantcardTailpaymentCreateModel(object):

    def __init__(self):
        self._main_booking_order_id = None
        self._main_order_id = None
        self._out_order_id = None
        self._pay_invalid_hours = None
        self._service_desc = None
        self._service_programs = None
        self._tail_payment_order_price_yuan = None

    @property
    def main_booking_order_id(self):
        return self._main_booking_order_id

    @main_booking_order_id.setter
    def main_booking_order_id(self, value):
        self._main_booking_order_id = value
    @property
    def main_order_id(self):
        return self._main_order_id

    @main_order_id.setter
    def main_order_id(self, value):
        self._main_order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def pay_invalid_hours(self):
        return self._pay_invalid_hours

    @pay_invalid_hours.setter
    def pay_invalid_hours(self, value):
        self._pay_invalid_hours = value
    @property
    def service_desc(self):
        return self._service_desc

    @service_desc.setter
    def service_desc(self, value):
        self._service_desc = value
    @property
    def service_programs(self):
        return self._service_programs

    @service_programs.setter
    def service_programs(self, value):
        if isinstance(value, list):
            self._service_programs = list()
            for i in value:
                if isinstance(i, LifeServiceTailPaymentServiceProgram):
                    self._service_programs.append(i)
                else:
                    self._service_programs.append(LifeServiceTailPaymentServiceProgram.from_alipay_dict(i))
    @property
    def tail_payment_order_price_yuan(self):
        return self._tail_payment_order_price_yuan

    @tail_payment_order_price_yuan.setter
    def tail_payment_order_price_yuan(self, value):
        self._tail_payment_order_price_yuan = value


    def to_alipay_dict(self):
        params = dict()
        if self.main_booking_order_id:
            if hasattr(self.main_booking_order_id, 'to_alipay_dict'):
                params['main_booking_order_id'] = self.main_booking_order_id.to_alipay_dict()
            else:
                params['main_booking_order_id'] = self.main_booking_order_id
        if self.main_order_id:
            if hasattr(self.main_order_id, 'to_alipay_dict'):
                params['main_order_id'] = self.main_order_id.to_alipay_dict()
            else:
                params['main_order_id'] = self.main_order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.pay_invalid_hours:
            if hasattr(self.pay_invalid_hours, 'to_alipay_dict'):
                params['pay_invalid_hours'] = self.pay_invalid_hours.to_alipay_dict()
            else:
                params['pay_invalid_hours'] = self.pay_invalid_hours
        if self.service_desc:
            if hasattr(self.service_desc, 'to_alipay_dict'):
                params['service_desc'] = self.service_desc.to_alipay_dict()
            else:
                params['service_desc'] = self.service_desc
        if self.service_programs:
            if isinstance(self.service_programs, list):
                for i in range(0, len(self.service_programs)):
                    element = self.service_programs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_programs[i] = element.to_alipay_dict()
            if hasattr(self.service_programs, 'to_alipay_dict'):
                params['service_programs'] = self.service_programs.to_alipay_dict()
            else:
                params['service_programs'] = self.service_programs
        if self.tail_payment_order_price_yuan:
            if hasattr(self.tail_payment_order_price_yuan, 'to_alipay_dict'):
                params['tail_payment_order_price_yuan'] = self.tail_payment_order_price_yuan.to_alipay_dict()
            else:
                params['tail_payment_order_price_yuan'] = self.tail_payment_order_price_yuan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTailpaymentCreateModel()
        if 'main_booking_order_id' in d:
            o.main_booking_order_id = d['main_booking_order_id']
        if 'main_order_id' in d:
            o.main_order_id = d['main_order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'pay_invalid_hours' in d:
            o.pay_invalid_hours = d['pay_invalid_hours']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_programs' in d:
            o.service_programs = d['service_programs']
        if 'tail_payment_order_price_yuan' in d:
            o.tail_payment_order_price_yuan = d['tail_payment_order_price_yuan']
        return o


