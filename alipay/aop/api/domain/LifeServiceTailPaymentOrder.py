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
        self._main_order_type = None
        self._open_id = None
        self._order_success_time = None
        self._out_order_id = None
        self._pay_invalid_time = None
        self._payee_uid = None
        self._service_desc = None
        self._service_programs = None
        self._settle_shop_id = None
        self._tail_payment_id = None
        self._tail_payment_order_id = None
        self._tail_payment_order_price_yuan = None
        self._tail_payment_order_status = None
        self._third_category_code = None

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
    def main_order_type(self):
        return self._main_order_type

    @main_order_type.setter
    def main_order_type(self, value):
        self._main_order_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_success_time(self):
        return self._order_success_time

    @order_success_time.setter
    def order_success_time(self, value):
        self._order_success_time = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def pay_invalid_time(self):
        return self._pay_invalid_time

    @pay_invalid_time.setter
    def pay_invalid_time(self, value):
        self._pay_invalid_time = value
    @property
    def payee_uid(self):
        return self._payee_uid

    @payee_uid.setter
    def payee_uid(self, value):
        self._payee_uid = value
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
    def settle_shop_id(self):
        return self._settle_shop_id

    @settle_shop_id.setter
    def settle_shop_id(self, value):
        self._settle_shop_id = value
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
    @property
    def third_category_code(self):
        return self._third_category_code

    @third_category_code.setter
    def third_category_code(self, value):
        self._third_category_code = value


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
        if self.main_order_type:
            if hasattr(self.main_order_type, 'to_alipay_dict'):
                params['main_order_type'] = self.main_order_type.to_alipay_dict()
            else:
                params['main_order_type'] = self.main_order_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_success_time:
            if hasattr(self.order_success_time, 'to_alipay_dict'):
                params['order_success_time'] = self.order_success_time.to_alipay_dict()
            else:
                params['order_success_time'] = self.order_success_time
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.pay_invalid_time:
            if hasattr(self.pay_invalid_time, 'to_alipay_dict'):
                params['pay_invalid_time'] = self.pay_invalid_time.to_alipay_dict()
            else:
                params['pay_invalid_time'] = self.pay_invalid_time
        if self.payee_uid:
            if hasattr(self.payee_uid, 'to_alipay_dict'):
                params['payee_uid'] = self.payee_uid.to_alipay_dict()
            else:
                params['payee_uid'] = self.payee_uid
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
        if self.settle_shop_id:
            if hasattr(self.settle_shop_id, 'to_alipay_dict'):
                params['settle_shop_id'] = self.settle_shop_id.to_alipay_dict()
            else:
                params['settle_shop_id'] = self.settle_shop_id
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
        if self.third_category_code:
            if hasattr(self.third_category_code, 'to_alipay_dict'):
                params['third_category_code'] = self.third_category_code.to_alipay_dict()
            else:
                params['third_category_code'] = self.third_category_code
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
        if 'main_order_type' in d:
            o.main_order_type = d['main_order_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_success_time' in d:
            o.order_success_time = d['order_success_time']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'pay_invalid_time' in d:
            o.pay_invalid_time = d['pay_invalid_time']
        if 'payee_uid' in d:
            o.payee_uid = d['payee_uid']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_programs' in d:
            o.service_programs = d['service_programs']
        if 'settle_shop_id' in d:
            o.settle_shop_id = d['settle_shop_id']
        if 'tail_payment_id' in d:
            o.tail_payment_id = d['tail_payment_id']
        if 'tail_payment_order_id' in d:
            o.tail_payment_order_id = d['tail_payment_order_id']
        if 'tail_payment_order_price_yuan' in d:
            o.tail_payment_order_price_yuan = d['tail_payment_order_price_yuan']
        if 'tail_payment_order_status' in d:
            o.tail_payment_order_status = d['tail_payment_order_status']
        if 'third_category_code' in d:
            o.third_category_code = d['third_category_code']
        return o


