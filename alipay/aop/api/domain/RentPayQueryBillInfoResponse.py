#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayQueryBillInfoResponse(object):

    def __init__(self):
        self._accfund_result = None
        self._application_date = None
        self._cert_num = None
        self._cert_type = None
        self._draw_interest = None
        self._draw_item = None
        self._draw_principal = None
        self._payment_date = None
        self._payment_state = None
        self._principal_interest_total = None
        self._recipient_bank_code = None
        self._recipient_bank_num = None
        self._recipient_bank_username = None
        self._user_name = None
        self._user_record_no = None

    @property
    def accfund_result(self):
        return self._accfund_result

    @accfund_result.setter
    def accfund_result(self, value):
        self._accfund_result = value
    @property
    def application_date(self):
        return self._application_date

    @application_date.setter
    def application_date(self, value):
        self._application_date = value
    @property
    def cert_num(self):
        return self._cert_num

    @cert_num.setter
    def cert_num(self, value):
        self._cert_num = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def draw_interest(self):
        return self._draw_interest

    @draw_interest.setter
    def draw_interest(self, value):
        self._draw_interest = value
    @property
    def draw_item(self):
        return self._draw_item

    @draw_item.setter
    def draw_item(self, value):
        self._draw_item = value
    @property
    def draw_principal(self):
        return self._draw_principal

    @draw_principal.setter
    def draw_principal(self, value):
        self._draw_principal = value
    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value
    @property
    def payment_state(self):
        return self._payment_state

    @payment_state.setter
    def payment_state(self, value):
        self._payment_state = value
    @property
    def principal_interest_total(self):
        return self._principal_interest_total

    @principal_interest_total.setter
    def principal_interest_total(self, value):
        self._principal_interest_total = value
    @property
    def recipient_bank_code(self):
        return self._recipient_bank_code

    @recipient_bank_code.setter
    def recipient_bank_code(self, value):
        self._recipient_bank_code = value
    @property
    def recipient_bank_num(self):
        return self._recipient_bank_num

    @recipient_bank_num.setter
    def recipient_bank_num(self, value):
        self._recipient_bank_num = value
    @property
    def recipient_bank_username(self):
        return self._recipient_bank_username

    @recipient_bank_username.setter
    def recipient_bank_username(self, value):
        self._recipient_bank_username = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_record_no(self):
        return self._user_record_no

    @user_record_no.setter
    def user_record_no(self, value):
        self._user_record_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.accfund_result:
            if hasattr(self.accfund_result, 'to_alipay_dict'):
                params['accfund_result'] = self.accfund_result.to_alipay_dict()
            else:
                params['accfund_result'] = self.accfund_result
        if self.application_date:
            if hasattr(self.application_date, 'to_alipay_dict'):
                params['application_date'] = self.application_date.to_alipay_dict()
            else:
                params['application_date'] = self.application_date
        if self.cert_num:
            if hasattr(self.cert_num, 'to_alipay_dict'):
                params['cert_num'] = self.cert_num.to_alipay_dict()
            else:
                params['cert_num'] = self.cert_num
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.draw_interest:
            if hasattr(self.draw_interest, 'to_alipay_dict'):
                params['draw_interest'] = self.draw_interest.to_alipay_dict()
            else:
                params['draw_interest'] = self.draw_interest
        if self.draw_item:
            if hasattr(self.draw_item, 'to_alipay_dict'):
                params['draw_item'] = self.draw_item.to_alipay_dict()
            else:
                params['draw_item'] = self.draw_item
        if self.draw_principal:
            if hasattr(self.draw_principal, 'to_alipay_dict'):
                params['draw_principal'] = self.draw_principal.to_alipay_dict()
            else:
                params['draw_principal'] = self.draw_principal
        if self.payment_date:
            if hasattr(self.payment_date, 'to_alipay_dict'):
                params['payment_date'] = self.payment_date.to_alipay_dict()
            else:
                params['payment_date'] = self.payment_date
        if self.payment_state:
            if hasattr(self.payment_state, 'to_alipay_dict'):
                params['payment_state'] = self.payment_state.to_alipay_dict()
            else:
                params['payment_state'] = self.payment_state
        if self.principal_interest_total:
            if hasattr(self.principal_interest_total, 'to_alipay_dict'):
                params['principal_interest_total'] = self.principal_interest_total.to_alipay_dict()
            else:
                params['principal_interest_total'] = self.principal_interest_total
        if self.recipient_bank_code:
            if hasattr(self.recipient_bank_code, 'to_alipay_dict'):
                params['recipient_bank_code'] = self.recipient_bank_code.to_alipay_dict()
            else:
                params['recipient_bank_code'] = self.recipient_bank_code
        if self.recipient_bank_num:
            if hasattr(self.recipient_bank_num, 'to_alipay_dict'):
                params['recipient_bank_num'] = self.recipient_bank_num.to_alipay_dict()
            else:
                params['recipient_bank_num'] = self.recipient_bank_num
        if self.recipient_bank_username:
            if hasattr(self.recipient_bank_username, 'to_alipay_dict'):
                params['recipient_bank_username'] = self.recipient_bank_username.to_alipay_dict()
            else:
                params['recipient_bank_username'] = self.recipient_bank_username
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_record_no:
            if hasattr(self.user_record_no, 'to_alipay_dict'):
                params['user_record_no'] = self.user_record_no.to_alipay_dict()
            else:
                params['user_record_no'] = self.user_record_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPayQueryBillInfoResponse()
        if 'accfund_result' in d:
            o.accfund_result = d['accfund_result']
        if 'application_date' in d:
            o.application_date = d['application_date']
        if 'cert_num' in d:
            o.cert_num = d['cert_num']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'draw_interest' in d:
            o.draw_interest = d['draw_interest']
        if 'draw_item' in d:
            o.draw_item = d['draw_item']
        if 'draw_principal' in d:
            o.draw_principal = d['draw_principal']
        if 'payment_date' in d:
            o.payment_date = d['payment_date']
        if 'payment_state' in d:
            o.payment_state = d['payment_state']
        if 'principal_interest_total' in d:
            o.principal_interest_total = d['principal_interest_total']
        if 'recipient_bank_code' in d:
            o.recipient_bank_code = d['recipient_bank_code']
        if 'recipient_bank_num' in d:
            o.recipient_bank_num = d['recipient_bank_num']
        if 'recipient_bank_username' in d:
            o.recipient_bank_username = d['recipient_bank_username']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_record_no' in d:
            o.user_record_no = d['user_record_no']
        return o


