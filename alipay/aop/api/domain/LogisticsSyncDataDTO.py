#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsSyncDataDTO(object):

    def __init__(self):
        self._accept_address = None
        self._accept_time = None
        self._actual_weight = None
        self._auth_code = None
        self._auth_type = None
        self._cancel_reason = None
        self._cancel_time = None
        self._courier_name = None
        self._courier_phone = None
        self._discount_amount = None
        self._inbound_address = None
        self._inbound_time = None
        self._insured_weight_amount = None
        self._logistics_no = None
        self._main_amount = None
        self._op_code = None
        self._out_biz_no = None
        self._out_logistics_no = None
        self._over_weight_amount = None
        self._package_amount = None
        self._pay_url = None
        self._receipt_addition = None
        self._receipt_first = None
        self._receipt_total = None
        self._receive_time = None
        self._remark = None
        self._sign_time = None
        self._signer_address = None
        self._signer_name = None
        self._signer_phone = None
        self._user_need_pay = None
        self._user_real_pay = None

    @property
    def accept_address(self):
        return self._accept_address

    @accept_address.setter
    def accept_address(self, value):
        self._accept_address = value
    @property
    def accept_time(self):
        return self._accept_time

    @accept_time.setter
    def accept_time(self, value):
        self._accept_time = value
    @property
    def actual_weight(self):
        return self._actual_weight

    @actual_weight.setter
    def actual_weight(self, value):
        self._actual_weight = value
    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def courier_name(self):
        return self._courier_name

    @courier_name.setter
    def courier_name(self, value):
        self._courier_name = value
    @property
    def courier_phone(self):
        return self._courier_phone

    @courier_phone.setter
    def courier_phone(self, value):
        self._courier_phone = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def inbound_address(self):
        return self._inbound_address

    @inbound_address.setter
    def inbound_address(self, value):
        self._inbound_address = value
    @property
    def inbound_time(self):
        return self._inbound_time

    @inbound_time.setter
    def inbound_time(self, value):
        self._inbound_time = value
    @property
    def insured_weight_amount(self):
        return self._insured_weight_amount

    @insured_weight_amount.setter
    def insured_weight_amount(self, value):
        self._insured_weight_amount = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def main_amount(self):
        return self._main_amount

    @main_amount.setter
    def main_amount(self, value):
        self._main_amount = value
    @property
    def op_code(self):
        return self._op_code

    @op_code.setter
    def op_code(self, value):
        self._op_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_logistics_no(self):
        return self._out_logistics_no

    @out_logistics_no.setter
    def out_logistics_no(self, value):
        self._out_logistics_no = value
    @property
    def over_weight_amount(self):
        return self._over_weight_amount

    @over_weight_amount.setter
    def over_weight_amount(self, value):
        self._over_weight_amount = value
    @property
    def package_amount(self):
        return self._package_amount

    @package_amount.setter
    def package_amount(self, value):
        self._package_amount = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def receipt_addition(self):
        return self._receipt_addition

    @receipt_addition.setter
    def receipt_addition(self, value):
        self._receipt_addition = value
    @property
    def receipt_first(self):
        return self._receipt_first

    @receipt_first.setter
    def receipt_first(self, value):
        self._receipt_first = value
    @property
    def receipt_total(self):
        return self._receipt_total

    @receipt_total.setter
    def receipt_total(self, value):
        self._receipt_total = value
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def signer_address(self):
        return self._signer_address

    @signer_address.setter
    def signer_address(self, value):
        self._signer_address = value
    @property
    def signer_name(self):
        return self._signer_name

    @signer_name.setter
    def signer_name(self, value):
        self._signer_name = value
    @property
    def signer_phone(self):
        return self._signer_phone

    @signer_phone.setter
    def signer_phone(self, value):
        self._signer_phone = value
    @property
    def user_need_pay(self):
        return self._user_need_pay

    @user_need_pay.setter
    def user_need_pay(self, value):
        self._user_need_pay = value
    @property
    def user_real_pay(self):
        return self._user_real_pay

    @user_real_pay.setter
    def user_real_pay(self, value):
        self._user_real_pay = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_address:
            if hasattr(self.accept_address, 'to_alipay_dict'):
                params['accept_address'] = self.accept_address.to_alipay_dict()
            else:
                params['accept_address'] = self.accept_address
        if self.accept_time:
            if hasattr(self.accept_time, 'to_alipay_dict'):
                params['accept_time'] = self.accept_time.to_alipay_dict()
            else:
                params['accept_time'] = self.accept_time
        if self.actual_weight:
            if hasattr(self.actual_weight, 'to_alipay_dict'):
                params['actual_weight'] = self.actual_weight.to_alipay_dict()
            else:
                params['actual_weight'] = self.actual_weight
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.courier_name:
            if hasattr(self.courier_name, 'to_alipay_dict'):
                params['courier_name'] = self.courier_name.to_alipay_dict()
            else:
                params['courier_name'] = self.courier_name
        if self.courier_phone:
            if hasattr(self.courier_phone, 'to_alipay_dict'):
                params['courier_phone'] = self.courier_phone.to_alipay_dict()
            else:
                params['courier_phone'] = self.courier_phone
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.inbound_address:
            if hasattr(self.inbound_address, 'to_alipay_dict'):
                params['inbound_address'] = self.inbound_address.to_alipay_dict()
            else:
                params['inbound_address'] = self.inbound_address
        if self.inbound_time:
            if hasattr(self.inbound_time, 'to_alipay_dict'):
                params['inbound_time'] = self.inbound_time.to_alipay_dict()
            else:
                params['inbound_time'] = self.inbound_time
        if self.insured_weight_amount:
            if hasattr(self.insured_weight_amount, 'to_alipay_dict'):
                params['insured_weight_amount'] = self.insured_weight_amount.to_alipay_dict()
            else:
                params['insured_weight_amount'] = self.insured_weight_amount
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.main_amount:
            if hasattr(self.main_amount, 'to_alipay_dict'):
                params['main_amount'] = self.main_amount.to_alipay_dict()
            else:
                params['main_amount'] = self.main_amount
        if self.op_code:
            if hasattr(self.op_code, 'to_alipay_dict'):
                params['op_code'] = self.op_code.to_alipay_dict()
            else:
                params['op_code'] = self.op_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_logistics_no:
            if hasattr(self.out_logistics_no, 'to_alipay_dict'):
                params['out_logistics_no'] = self.out_logistics_no.to_alipay_dict()
            else:
                params['out_logistics_no'] = self.out_logistics_no
        if self.over_weight_amount:
            if hasattr(self.over_weight_amount, 'to_alipay_dict'):
                params['over_weight_amount'] = self.over_weight_amount.to_alipay_dict()
            else:
                params['over_weight_amount'] = self.over_weight_amount
        if self.package_amount:
            if hasattr(self.package_amount, 'to_alipay_dict'):
                params['package_amount'] = self.package_amount.to_alipay_dict()
            else:
                params['package_amount'] = self.package_amount
        if self.pay_url:
            if hasattr(self.pay_url, 'to_alipay_dict'):
                params['pay_url'] = self.pay_url.to_alipay_dict()
            else:
                params['pay_url'] = self.pay_url
        if self.receipt_addition:
            if hasattr(self.receipt_addition, 'to_alipay_dict'):
                params['receipt_addition'] = self.receipt_addition.to_alipay_dict()
            else:
                params['receipt_addition'] = self.receipt_addition
        if self.receipt_first:
            if hasattr(self.receipt_first, 'to_alipay_dict'):
                params['receipt_first'] = self.receipt_first.to_alipay_dict()
            else:
                params['receipt_first'] = self.receipt_first
        if self.receipt_total:
            if hasattr(self.receipt_total, 'to_alipay_dict'):
                params['receipt_total'] = self.receipt_total.to_alipay_dict()
            else:
                params['receipt_total'] = self.receipt_total
        if self.receive_time:
            if hasattr(self.receive_time, 'to_alipay_dict'):
                params['receive_time'] = self.receive_time.to_alipay_dict()
            else:
                params['receive_time'] = self.receive_time
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.signer_address:
            if hasattr(self.signer_address, 'to_alipay_dict'):
                params['signer_address'] = self.signer_address.to_alipay_dict()
            else:
                params['signer_address'] = self.signer_address
        if self.signer_name:
            if hasattr(self.signer_name, 'to_alipay_dict'):
                params['signer_name'] = self.signer_name.to_alipay_dict()
            else:
                params['signer_name'] = self.signer_name
        if self.signer_phone:
            if hasattr(self.signer_phone, 'to_alipay_dict'):
                params['signer_phone'] = self.signer_phone.to_alipay_dict()
            else:
                params['signer_phone'] = self.signer_phone
        if self.user_need_pay:
            if hasattr(self.user_need_pay, 'to_alipay_dict'):
                params['user_need_pay'] = self.user_need_pay.to_alipay_dict()
            else:
                params['user_need_pay'] = self.user_need_pay
        if self.user_real_pay:
            if hasattr(self.user_real_pay, 'to_alipay_dict'):
                params['user_real_pay'] = self.user_real_pay.to_alipay_dict()
            else:
                params['user_real_pay'] = self.user_real_pay
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsSyncDataDTO()
        if 'accept_address' in d:
            o.accept_address = d['accept_address']
        if 'accept_time' in d:
            o.accept_time = d['accept_time']
        if 'actual_weight' in d:
            o.actual_weight = d['actual_weight']
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'courier_name' in d:
            o.courier_name = d['courier_name']
        if 'courier_phone' in d:
            o.courier_phone = d['courier_phone']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'inbound_address' in d:
            o.inbound_address = d['inbound_address']
        if 'inbound_time' in d:
            o.inbound_time = d['inbound_time']
        if 'insured_weight_amount' in d:
            o.insured_weight_amount = d['insured_weight_amount']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'main_amount' in d:
            o.main_amount = d['main_amount']
        if 'op_code' in d:
            o.op_code = d['op_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_logistics_no' in d:
            o.out_logistics_no = d['out_logistics_no']
        if 'over_weight_amount' in d:
            o.over_weight_amount = d['over_weight_amount']
        if 'package_amount' in d:
            o.package_amount = d['package_amount']
        if 'pay_url' in d:
            o.pay_url = d['pay_url']
        if 'receipt_addition' in d:
            o.receipt_addition = d['receipt_addition']
        if 'receipt_first' in d:
            o.receipt_first = d['receipt_first']
        if 'receipt_total' in d:
            o.receipt_total = d['receipt_total']
        if 'receive_time' in d:
            o.receive_time = d['receive_time']
        if 'remark' in d:
            o.remark = d['remark']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'signer_address' in d:
            o.signer_address = d['signer_address']
        if 'signer_name' in d:
            o.signer_name = d['signer_name']
        if 'signer_phone' in d:
            o.signer_phone = d['signer_phone']
        if 'user_need_pay' in d:
            o.user_need_pay = d['user_need_pay']
        if 'user_real_pay' in d:
            o.user_real_pay = d['user_real_pay']
        return o


