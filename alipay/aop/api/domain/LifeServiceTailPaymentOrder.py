#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LifeServiceTailPaymentServiceProgram import LifeServiceTailPaymentServiceProgram


class LifeServiceTailPaymentOrder(object):

    def __init__(self):
        self._cancel_reason = None
        self._main_booking_order_id = None
        self._main_order_id = None
        self._order_success_time = None
        self._pay_invalid_time = None
        self._service_desc = None
        self._service_programs = None
        self._tail_payment_id = None
        self._tail_payment_order_id = None
        self._tail_payment_order_price_yuan = None
        self._tail_payment_order_status = None

    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
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
    def order_success_time(self):
        return self._order_success_time

    @order_success_time.setter
    def order_success_time(self, value):
        self._order_success_time = value
    @property
    def pay_invalid_time(self):
        return self._pay_invalid_time

    @pay_invalid_time.setter
    def pay_invalid_time(self, value):
        self._pay_invalid_time = value
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
    def tail_payment_id(self):
        return self._tail_payment_id

    @tail_payment_id.setter
    def tail_payment_id(self, value):
        self._tail_payment_id = value
    @property
    def tail_payment_order_id(self):
        return self._tail_payment_order_id

    @tail_payment_order_id.setter
    def tail_payment_order_id(self, value):
        self._tail_payment_order_id = value
    @property
    def tail_payment_order_price_yuan(self):
        return self._tail_payment_order_price_yuan

    @tail_payment_order_price_yuan.setter
    def tail_payment_order_price_yuan(self, value):
        self._tail_payment_order_price_yuan = value
    @property
    def tail_payment_order_status(self):
        return self._tail_payment_order_status

    @tail_payment_order_status.setter
    def tail_payment_order_status(self, value):
        self._tail_payment_order_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
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
        if self.order_success_time:
            if hasattr(self.order_success_time, 'to_alipay_dict'):
                params['order_success_time'] = self.order_success_time.to_alipay_dict()
            else:
                params['order_success_time'] = self.order_success_time
        if self.pay_invalid_time:
            if hasattr(self.pay_invalid_time, 'to_alipay_dict'):
                params['pay_invalid_time'] = self.pay_invalid_time.to_alipay_dict()
            else:
                params['pay_invalid_time'] = self.pay_invalid_time
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
        if self.tail_payment_id:
            if hasattr(self.tail_payment_id, 'to_alipay_dict'):
                params['tail_payment_id'] = self.tail_payment_id.to_alipay_dict()
            else:
                params['tail_payment_id'] = self.tail_payment_id
        if self.tail_payment_order_id:
            if hasattr(self.tail_payment_order_id, 'to_alipay_dict'):
                params['tail_payment_order_id'] = self.tail_payment_order_id.to_alipay_dict()
            else:
                params['tail_payment_order_id'] = self.tail_payment_order_id
        if self.tail_payment_order_price_yuan:
            if hasattr(self.tail_payment_order_price_yuan, 'to_alipay_dict'):
                params['tail_payment_order_price_yuan'] = self.tail_payment_order_price_yuan.to_alipay_dict()
            else:
                params['tail_payment_order_price_yuan'] = self.tail_payment_order_price_yuan
        if self.tail_payment_order_status:
            if hasattr(self.tail_payment_order_status, 'to_alipay_dict'):
                params['tail_payment_order_status'] = self.tail_payment_order_status.to_alipay_dict()
            else:
                params['tail_payment_order_status'] = self.tail_payment_order_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceTailPaymentOrder()
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'main_booking_order_id' in d:
            o.main_booking_order_id = d['main_booking_order_id']
        if 'main_order_id' in d:
            o.main_order_id = d['main_order_id']
        if 'order_success_time' in d:
            o.order_success_time = d['order_success_time']
        if 'pay_invalid_time' in d:
            o.pay_invalid_time = d['pay_invalid_time']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_programs' in d:
            o.service_programs = d['service_programs']
        if 'tail_payment_id' in d:
            o.tail_payment_id = d['tail_payment_id']
        if 'tail_payment_order_id' in d:
            o.tail_payment_order_id = d['tail_payment_order_id']
        if 'tail_payment_order_price_yuan' in d:
            o.tail_payment_order_price_yuan = d['tail_payment_order_price_yuan']
        if 'tail_payment_order_status' in d:
            o.tail_payment_order_status = d['tail_payment_order_status']
        return o


