#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalOrderPayChannel import MedicalOrderPayChannel


class AlipayCommerceMedicalPaymentOrderSyncModel(object):

    def __init__(self):
        self._alipay_amount = None
        self._alipay_trade_no = None
        self._biz_trace_no = None
        self._biz_type = None
        self._fee_sumamt = None
        self._fund_pay = None
        self._gmt_paid = None
        self._medical_org_name = None
        self._medical_org_no = None
        self._opt_type = None
        self._other_pay_channel = None
        self._out_biz_no = None
        self._own_pay_amt = None
        self._payment_city_code = None
        self._payment_place = None
        self._payment_place_code = None
        self._psn_acct_pay = None
        self._qr_code = None
        self._status = None
        self._subject = None
        self._sys_service_provider_id = None

    @property
    def alipay_amount(self):
        return self._alipay_amount

    @alipay_amount.setter
    def alipay_amount(self, value):
        self._alipay_amount = value
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def biz_trace_no(self):
        return self._biz_trace_no

    @biz_trace_no.setter
    def biz_trace_no(self, value):
        if isinstance(value, list):
            self._biz_trace_no = list()
            for i in value:
                self._biz_trace_no.append(i)
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def fee_sumamt(self):
        return self._fee_sumamt

    @fee_sumamt.setter
    def fee_sumamt(self, value):
        self._fee_sumamt = value
    @property
    def fund_pay(self):
        return self._fund_pay

    @fund_pay.setter
    def fund_pay(self, value):
        self._fund_pay = value
    @property
    def gmt_paid(self):
        return self._gmt_paid

    @gmt_paid.setter
    def gmt_paid(self, value):
        self._gmt_paid = value
    @property
    def medical_org_name(self):
        return self._medical_org_name

    @medical_org_name.setter
    def medical_org_name(self, value):
        self._medical_org_name = value
    @property
    def medical_org_no(self):
        return self._medical_org_no

    @medical_org_no.setter
    def medical_org_no(self, value):
        self._medical_org_no = value
    @property
    def opt_type(self):
        return self._opt_type

    @opt_type.setter
    def opt_type(self, value):
        self._opt_type = value
    @property
    def other_pay_channel(self):
        return self._other_pay_channel

    @other_pay_channel.setter
    def other_pay_channel(self, value):
        if isinstance(value, list):
            self._other_pay_channel = list()
            for i in value:
                if isinstance(i, MedicalOrderPayChannel):
                    self._other_pay_channel.append(i)
                else:
                    self._other_pay_channel.append(MedicalOrderPayChannel.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def own_pay_amt(self):
        return self._own_pay_amt

    @own_pay_amt.setter
    def own_pay_amt(self, value):
        self._own_pay_amt = value
    @property
    def payment_city_code(self):
        return self._payment_city_code

    @payment_city_code.setter
    def payment_city_code(self, value):
        self._payment_city_code = value
    @property
    def payment_place(self):
        return self._payment_place

    @payment_place.setter
    def payment_place(self, value):
        self._payment_place = value
    @property
    def payment_place_code(self):
        return self._payment_place_code

    @payment_place_code.setter
    def payment_place_code(self, value):
        self._payment_place_code = value
    @property
    def psn_acct_pay(self):
        return self._psn_acct_pay

    @psn_acct_pay.setter
    def psn_acct_pay(self, value):
        self._psn_acct_pay = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_amount:
            if hasattr(self.alipay_amount, 'to_alipay_dict'):
                params['alipay_amount'] = self.alipay_amount.to_alipay_dict()
            else:
                params['alipay_amount'] = self.alipay_amount
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.biz_trace_no:
            if isinstance(self.biz_trace_no, list):
                for i in range(0, len(self.biz_trace_no)):
                    element = self.biz_trace_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_trace_no[i] = element.to_alipay_dict()
            if hasattr(self.biz_trace_no, 'to_alipay_dict'):
                params['biz_trace_no'] = self.biz_trace_no.to_alipay_dict()
            else:
                params['biz_trace_no'] = self.biz_trace_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.fee_sumamt:
            if hasattr(self.fee_sumamt, 'to_alipay_dict'):
                params['fee_sumamt'] = self.fee_sumamt.to_alipay_dict()
            else:
                params['fee_sumamt'] = self.fee_sumamt
        if self.fund_pay:
            if hasattr(self.fund_pay, 'to_alipay_dict'):
                params['fund_pay'] = self.fund_pay.to_alipay_dict()
            else:
                params['fund_pay'] = self.fund_pay
        if self.gmt_paid:
            if hasattr(self.gmt_paid, 'to_alipay_dict'):
                params['gmt_paid'] = self.gmt_paid.to_alipay_dict()
            else:
                params['gmt_paid'] = self.gmt_paid
        if self.medical_org_name:
            if hasattr(self.medical_org_name, 'to_alipay_dict'):
                params['medical_org_name'] = self.medical_org_name.to_alipay_dict()
            else:
                params['medical_org_name'] = self.medical_org_name
        if self.medical_org_no:
            if hasattr(self.medical_org_no, 'to_alipay_dict'):
                params['medical_org_no'] = self.medical_org_no.to_alipay_dict()
            else:
                params['medical_org_no'] = self.medical_org_no
        if self.opt_type:
            if hasattr(self.opt_type, 'to_alipay_dict'):
                params['opt_type'] = self.opt_type.to_alipay_dict()
            else:
                params['opt_type'] = self.opt_type
        if self.other_pay_channel:
            if isinstance(self.other_pay_channel, list):
                for i in range(0, len(self.other_pay_channel)):
                    element = self.other_pay_channel[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_pay_channel[i] = element.to_alipay_dict()
            if hasattr(self.other_pay_channel, 'to_alipay_dict'):
                params['other_pay_channel'] = self.other_pay_channel.to_alipay_dict()
            else:
                params['other_pay_channel'] = self.other_pay_channel
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.own_pay_amt:
            if hasattr(self.own_pay_amt, 'to_alipay_dict'):
                params['own_pay_amt'] = self.own_pay_amt.to_alipay_dict()
            else:
                params['own_pay_amt'] = self.own_pay_amt
        if self.payment_city_code:
            if hasattr(self.payment_city_code, 'to_alipay_dict'):
                params['payment_city_code'] = self.payment_city_code.to_alipay_dict()
            else:
                params['payment_city_code'] = self.payment_city_code
        if self.payment_place:
            if hasattr(self.payment_place, 'to_alipay_dict'):
                params['payment_place'] = self.payment_place.to_alipay_dict()
            else:
                params['payment_place'] = self.payment_place
        if self.payment_place_code:
            if hasattr(self.payment_place_code, 'to_alipay_dict'):
                params['payment_place_code'] = self.payment_place_code.to_alipay_dict()
            else:
                params['payment_place_code'] = self.payment_place_code
        if self.psn_acct_pay:
            if hasattr(self.psn_acct_pay, 'to_alipay_dict'):
                params['psn_acct_pay'] = self.psn_acct_pay.to_alipay_dict()
            else:
                params['psn_acct_pay'] = self.psn_acct_pay
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPaymentOrderSyncModel()
        if 'alipay_amount' in d:
            o.alipay_amount = d['alipay_amount']
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'biz_trace_no' in d:
            o.biz_trace_no = d['biz_trace_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'fee_sumamt' in d:
            o.fee_sumamt = d['fee_sumamt']
        if 'fund_pay' in d:
            o.fund_pay = d['fund_pay']
        if 'gmt_paid' in d:
            o.gmt_paid = d['gmt_paid']
        if 'medical_org_name' in d:
            o.medical_org_name = d['medical_org_name']
        if 'medical_org_no' in d:
            o.medical_org_no = d['medical_org_no']
        if 'opt_type' in d:
            o.opt_type = d['opt_type']
        if 'other_pay_channel' in d:
            o.other_pay_channel = d['other_pay_channel']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'own_pay_amt' in d:
            o.own_pay_amt = d['own_pay_amt']
        if 'payment_city_code' in d:
            o.payment_city_code = d['payment_city_code']
        if 'payment_place' in d:
            o.payment_place = d['payment_place']
        if 'payment_place_code' in d:
            o.payment_place_code = d['payment_place_code']
        if 'psn_acct_pay' in d:
            o.psn_acct_pay = d['psn_acct_pay']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'status' in d:
            o.status = d['status']
        if 'subject' in d:
            o.subject = d['subject']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o


