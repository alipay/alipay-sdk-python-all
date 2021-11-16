#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractPeople import ContractPeople
from alipay.aop.api.domain.ContractAttach import ContractAttach
from alipay.aop.api.domain.ContractAttach import ContractAttach
from alipay.aop.api.domain.ContractPeople import ContractPeople
from alipay.aop.api.domain.ContractPeople import ContractPeople
from alipay.aop.api.domain.Partner import Partner
from alipay.aop.api.domain.Partner import Partner
from alipay.aop.api.domain.SealDisplayRequest import SealDisplayRequest


class AlipayBossProdContractOnestepsignCreateModel(object):

    def __init__(self):
        self._amount = None
        self._amount_type = None
        self._ante_dated_voucher_id = None
        self._apply_people = None
        self._approve_instant_id = None
        self._auto_renew_period = None
        self._business_id = None
        self._business_line = None
        self._comment = None
        self._contract_attaches = None
        self._contract_code = None
        self._contract_doc = None
        self._contract_duration = None
        self._contract_name = None
        self._contract_sign_type = None
        self._currency = None
        self._delivery_type = None
        self._duration_unit = None
        self._effect_time = None
        self._effect_type = None
        self._expire_time = None
        self._ext = None
        self._fifth_contract_type = None
        self._first_contract_type = None
        self._fourth_contract_type = None
        self._give_back_type = None
        self._in_charge_people = None
        self._in_effect_type = None
        self._invoice_target = None
        self._invoice_type = None
        self._legal_people = None
        self._number = None
        self._part_a = None
        self._part_b = None
        self._payer = None
        self._phy_seal_type = None
        self._remarks_on_printing = None
        self._seal_order = None
        self._second_contract_type = None
        self._sign_params = None
        self._sixth_contract_type = None
        self._source_system_id = None
        self._tax_rate = None
        self._tenant = None
        self._third_contract_type = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def amount_type(self):
        return self._amount_type

    @amount_type.setter
    def amount_type(self, value):
        self._amount_type = value
    @property
    def ante_dated_voucher_id(self):
        return self._ante_dated_voucher_id

    @ante_dated_voucher_id.setter
    def ante_dated_voucher_id(self, value):
        self._ante_dated_voucher_id = value
    @property
    def apply_people(self):
        return self._apply_people

    @apply_people.setter
    def apply_people(self, value):
        if isinstance(value, ContractPeople):
            self._apply_people = value
        else:
            self._apply_people = ContractPeople.from_alipay_dict(value)
    @property
    def approve_instant_id(self):
        return self._approve_instant_id

    @approve_instant_id.setter
    def approve_instant_id(self, value):
        self._approve_instant_id = value
    @property
    def auto_renew_period(self):
        return self._auto_renew_period

    @auto_renew_period.setter
    def auto_renew_period(self, value):
        self._auto_renew_period = value
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def business_line(self):
        return self._business_line

    @business_line.setter
    def business_line(self, value):
        self._business_line = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def contract_attaches(self):
        return self._contract_attaches

    @contract_attaches.setter
    def contract_attaches(self, value):
        if isinstance(value, list):
            self._contract_attaches = list()
            for i in value:
                if isinstance(i, ContractAttach):
                    self._contract_attaches.append(i)
                else:
                    self._contract_attaches.append(ContractAttach.from_alipay_dict(i))
    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def contract_doc(self):
        return self._contract_doc

    @contract_doc.setter
    def contract_doc(self, value):
        if isinstance(value, ContractAttach):
            self._contract_doc = value
        else:
            self._contract_doc = ContractAttach.from_alipay_dict(value)
    @property
    def contract_duration(self):
        return self._contract_duration

    @contract_duration.setter
    def contract_duration(self, value):
        self._contract_duration = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_sign_type(self):
        return self._contract_sign_type

    @contract_sign_type.setter
    def contract_sign_type(self, value):
        self._contract_sign_type = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def duration_unit(self):
        return self._duration_unit

    @duration_unit.setter
    def duration_unit(self, value):
        self._duration_unit = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def effect_type(self):
        return self._effect_type

    @effect_type.setter
    def effect_type(self, value):
        self._effect_type = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def fifth_contract_type(self):
        return self._fifth_contract_type

    @fifth_contract_type.setter
    def fifth_contract_type(self, value):
        self._fifth_contract_type = value
    @property
    def first_contract_type(self):
        return self._first_contract_type

    @first_contract_type.setter
    def first_contract_type(self, value):
        self._first_contract_type = value
    @property
    def fourth_contract_type(self):
        return self._fourth_contract_type

    @fourth_contract_type.setter
    def fourth_contract_type(self, value):
        self._fourth_contract_type = value
    @property
    def give_back_type(self):
        return self._give_back_type

    @give_back_type.setter
    def give_back_type(self, value):
        self._give_back_type = value
    @property
    def in_charge_people(self):
        return self._in_charge_people

    @in_charge_people.setter
    def in_charge_people(self, value):
        if isinstance(value, list):
            self._in_charge_people = list()
            for i in value:
                if isinstance(i, ContractPeople):
                    self._in_charge_people.append(i)
                else:
                    self._in_charge_people.append(ContractPeople.from_alipay_dict(i))
    @property
    def in_effect_type(self):
        return self._in_effect_type

    @in_effect_type.setter
    def in_effect_type(self, value):
        self._in_effect_type = value
    @property
    def invoice_target(self):
        return self._invoice_target

    @invoice_target.setter
    def invoice_target(self, value):
        self._invoice_target = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def legal_people(self):
        return self._legal_people

    @legal_people.setter
    def legal_people(self, value):
        if isinstance(value, list):
            self._legal_people = list()
            for i in value:
                if isinstance(i, ContractPeople):
                    self._legal_people.append(i)
                else:
                    self._legal_people.append(ContractPeople.from_alipay_dict(i))
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def part_a(self):
        return self._part_a

    @part_a.setter
    def part_a(self, value):
        if isinstance(value, list):
            self._part_a = list()
            for i in value:
                if isinstance(i, Partner):
                    self._part_a.append(i)
                else:
                    self._part_a.append(Partner.from_alipay_dict(i))
    @property
    def part_b(self):
        return self._part_b

    @part_b.setter
    def part_b(self, value):
        if isinstance(value, list):
            self._part_b = list()
            for i in value:
                if isinstance(i, Partner):
                    self._part_b.append(i)
                else:
                    self._part_b.append(Partner.from_alipay_dict(i))
    @property
    def payer(self):
        return self._payer

    @payer.setter
    def payer(self, value):
        self._payer = value
    @property
    def phy_seal_type(self):
        return self._phy_seal_type

    @phy_seal_type.setter
    def phy_seal_type(self, value):
        self._phy_seal_type = value
    @property
    def remarks_on_printing(self):
        return self._remarks_on_printing

    @remarks_on_printing.setter
    def remarks_on_printing(self, value):
        self._remarks_on_printing = value
    @property
    def seal_order(self):
        return self._seal_order

    @seal_order.setter
    def seal_order(self, value):
        self._seal_order = value
    @property
    def second_contract_type(self):
        return self._second_contract_type

    @second_contract_type.setter
    def second_contract_type(self, value):
        self._second_contract_type = value
    @property
    def sign_params(self):
        return self._sign_params

    @sign_params.setter
    def sign_params(self, value):
        if isinstance(value, list):
            self._sign_params = list()
            for i in value:
                if isinstance(i, SealDisplayRequest):
                    self._sign_params.append(i)
                else:
                    self._sign_params.append(SealDisplayRequest.from_alipay_dict(i))
    @property
    def sixth_contract_type(self):
        return self._sixth_contract_type

    @sixth_contract_type.setter
    def sixth_contract_type(self, value):
        self._sixth_contract_type = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def third_contract_type(self):
        return self._third_contract_type

    @third_contract_type.setter
    def third_contract_type(self, value):
        self._third_contract_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.amount_type:
            if hasattr(self.amount_type, 'to_alipay_dict'):
                params['amount_type'] = self.amount_type.to_alipay_dict()
            else:
                params['amount_type'] = self.amount_type
        if self.ante_dated_voucher_id:
            if hasattr(self.ante_dated_voucher_id, 'to_alipay_dict'):
                params['ante_dated_voucher_id'] = self.ante_dated_voucher_id.to_alipay_dict()
            else:
                params['ante_dated_voucher_id'] = self.ante_dated_voucher_id
        if self.apply_people:
            if hasattr(self.apply_people, 'to_alipay_dict'):
                params['apply_people'] = self.apply_people.to_alipay_dict()
            else:
                params['apply_people'] = self.apply_people
        if self.approve_instant_id:
            if hasattr(self.approve_instant_id, 'to_alipay_dict'):
                params['approve_instant_id'] = self.approve_instant_id.to_alipay_dict()
            else:
                params['approve_instant_id'] = self.approve_instant_id
        if self.auto_renew_period:
            if hasattr(self.auto_renew_period, 'to_alipay_dict'):
                params['auto_renew_period'] = self.auto_renew_period.to_alipay_dict()
            else:
                params['auto_renew_period'] = self.auto_renew_period
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.business_line:
            if hasattr(self.business_line, 'to_alipay_dict'):
                params['business_line'] = self.business_line.to_alipay_dict()
            else:
                params['business_line'] = self.business_line
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.contract_attaches:
            if isinstance(self.contract_attaches, list):
                for i in range(0, len(self.contract_attaches)):
                    element = self.contract_attaches[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_attaches[i] = element.to_alipay_dict()
            if hasattr(self.contract_attaches, 'to_alipay_dict'):
                params['contract_attaches'] = self.contract_attaches.to_alipay_dict()
            else:
                params['contract_attaches'] = self.contract_attaches
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.contract_doc:
            if hasattr(self.contract_doc, 'to_alipay_dict'):
                params['contract_doc'] = self.contract_doc.to_alipay_dict()
            else:
                params['contract_doc'] = self.contract_doc
        if self.contract_duration:
            if hasattr(self.contract_duration, 'to_alipay_dict'):
                params['contract_duration'] = self.contract_duration.to_alipay_dict()
            else:
                params['contract_duration'] = self.contract_duration
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_sign_type:
            if hasattr(self.contract_sign_type, 'to_alipay_dict'):
                params['contract_sign_type'] = self.contract_sign_type.to_alipay_dict()
            else:
                params['contract_sign_type'] = self.contract_sign_type
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.duration_unit:
            if hasattr(self.duration_unit, 'to_alipay_dict'):
                params['duration_unit'] = self.duration_unit.to_alipay_dict()
            else:
                params['duration_unit'] = self.duration_unit
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.effect_type:
            if hasattr(self.effect_type, 'to_alipay_dict'):
                params['effect_type'] = self.effect_type.to_alipay_dict()
            else:
                params['effect_type'] = self.effect_type
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.fifth_contract_type:
            if hasattr(self.fifth_contract_type, 'to_alipay_dict'):
                params['fifth_contract_type'] = self.fifth_contract_type.to_alipay_dict()
            else:
                params['fifth_contract_type'] = self.fifth_contract_type
        if self.first_contract_type:
            if hasattr(self.first_contract_type, 'to_alipay_dict'):
                params['first_contract_type'] = self.first_contract_type.to_alipay_dict()
            else:
                params['first_contract_type'] = self.first_contract_type
        if self.fourth_contract_type:
            if hasattr(self.fourth_contract_type, 'to_alipay_dict'):
                params['fourth_contract_type'] = self.fourth_contract_type.to_alipay_dict()
            else:
                params['fourth_contract_type'] = self.fourth_contract_type
        if self.give_back_type:
            if hasattr(self.give_back_type, 'to_alipay_dict'):
                params['give_back_type'] = self.give_back_type.to_alipay_dict()
            else:
                params['give_back_type'] = self.give_back_type
        if self.in_charge_people:
            if isinstance(self.in_charge_people, list):
                for i in range(0, len(self.in_charge_people)):
                    element = self.in_charge_people[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.in_charge_people[i] = element.to_alipay_dict()
            if hasattr(self.in_charge_people, 'to_alipay_dict'):
                params['in_charge_people'] = self.in_charge_people.to_alipay_dict()
            else:
                params['in_charge_people'] = self.in_charge_people
        if self.in_effect_type:
            if hasattr(self.in_effect_type, 'to_alipay_dict'):
                params['in_effect_type'] = self.in_effect_type.to_alipay_dict()
            else:
                params['in_effect_type'] = self.in_effect_type
        if self.invoice_target:
            if hasattr(self.invoice_target, 'to_alipay_dict'):
                params['invoice_target'] = self.invoice_target.to_alipay_dict()
            else:
                params['invoice_target'] = self.invoice_target
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.legal_people:
            if isinstance(self.legal_people, list):
                for i in range(0, len(self.legal_people)):
                    element = self.legal_people[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.legal_people[i] = element.to_alipay_dict()
            if hasattr(self.legal_people, 'to_alipay_dict'):
                params['legal_people'] = self.legal_people.to_alipay_dict()
            else:
                params['legal_people'] = self.legal_people
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.part_a:
            if isinstance(self.part_a, list):
                for i in range(0, len(self.part_a)):
                    element = self.part_a[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.part_a[i] = element.to_alipay_dict()
            if hasattr(self.part_a, 'to_alipay_dict'):
                params['part_a'] = self.part_a.to_alipay_dict()
            else:
                params['part_a'] = self.part_a
        if self.part_b:
            if isinstance(self.part_b, list):
                for i in range(0, len(self.part_b)):
                    element = self.part_b[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.part_b[i] = element.to_alipay_dict()
            if hasattr(self.part_b, 'to_alipay_dict'):
                params['part_b'] = self.part_b.to_alipay_dict()
            else:
                params['part_b'] = self.part_b
        if self.payer:
            if hasattr(self.payer, 'to_alipay_dict'):
                params['payer'] = self.payer.to_alipay_dict()
            else:
                params['payer'] = self.payer
        if self.phy_seal_type:
            if hasattr(self.phy_seal_type, 'to_alipay_dict'):
                params['phy_seal_type'] = self.phy_seal_type.to_alipay_dict()
            else:
                params['phy_seal_type'] = self.phy_seal_type
        if self.remarks_on_printing:
            if hasattr(self.remarks_on_printing, 'to_alipay_dict'):
                params['remarks_on_printing'] = self.remarks_on_printing.to_alipay_dict()
            else:
                params['remarks_on_printing'] = self.remarks_on_printing
        if self.seal_order:
            if hasattr(self.seal_order, 'to_alipay_dict'):
                params['seal_order'] = self.seal_order.to_alipay_dict()
            else:
                params['seal_order'] = self.seal_order
        if self.second_contract_type:
            if hasattr(self.second_contract_type, 'to_alipay_dict'):
                params['second_contract_type'] = self.second_contract_type.to_alipay_dict()
            else:
                params['second_contract_type'] = self.second_contract_type
        if self.sign_params:
            if isinstance(self.sign_params, list):
                for i in range(0, len(self.sign_params)):
                    element = self.sign_params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_params[i] = element.to_alipay_dict()
            if hasattr(self.sign_params, 'to_alipay_dict'):
                params['sign_params'] = self.sign_params.to_alipay_dict()
            else:
                params['sign_params'] = self.sign_params
        if self.sixth_contract_type:
            if hasattr(self.sixth_contract_type, 'to_alipay_dict'):
                params['sixth_contract_type'] = self.sixth_contract_type.to_alipay_dict()
            else:
                params['sixth_contract_type'] = self.sixth_contract_type
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.third_contract_type:
            if hasattr(self.third_contract_type, 'to_alipay_dict'):
                params['third_contract_type'] = self.third_contract_type.to_alipay_dict()
            else:
                params['third_contract_type'] = self.third_contract_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdContractOnestepsignCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_type' in d:
            o.amount_type = d['amount_type']
        if 'ante_dated_voucher_id' in d:
            o.ante_dated_voucher_id = d['ante_dated_voucher_id']
        if 'apply_people' in d:
            o.apply_people = d['apply_people']
        if 'approve_instant_id' in d:
            o.approve_instant_id = d['approve_instant_id']
        if 'auto_renew_period' in d:
            o.auto_renew_period = d['auto_renew_period']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'business_line' in d:
            o.business_line = d['business_line']
        if 'comment' in d:
            o.comment = d['comment']
        if 'contract_attaches' in d:
            o.contract_attaches = d['contract_attaches']
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'contract_doc' in d:
            o.contract_doc = d['contract_doc']
        if 'contract_duration' in d:
            o.contract_duration = d['contract_duration']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_sign_type' in d:
            o.contract_sign_type = d['contract_sign_type']
        if 'currency' in d:
            o.currency = d['currency']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'duration_unit' in d:
            o.duration_unit = d['duration_unit']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'effect_type' in d:
            o.effect_type = d['effect_type']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'ext' in d:
            o.ext = d['ext']
        if 'fifth_contract_type' in d:
            o.fifth_contract_type = d['fifth_contract_type']
        if 'first_contract_type' in d:
            o.first_contract_type = d['first_contract_type']
        if 'fourth_contract_type' in d:
            o.fourth_contract_type = d['fourth_contract_type']
        if 'give_back_type' in d:
            o.give_back_type = d['give_back_type']
        if 'in_charge_people' in d:
            o.in_charge_people = d['in_charge_people']
        if 'in_effect_type' in d:
            o.in_effect_type = d['in_effect_type']
        if 'invoice_target' in d:
            o.invoice_target = d['invoice_target']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'legal_people' in d:
            o.legal_people = d['legal_people']
        if 'number' in d:
            o.number = d['number']
        if 'part_a' in d:
            o.part_a = d['part_a']
        if 'part_b' in d:
            o.part_b = d['part_b']
        if 'payer' in d:
            o.payer = d['payer']
        if 'phy_seal_type' in d:
            o.phy_seal_type = d['phy_seal_type']
        if 'remarks_on_printing' in d:
            o.remarks_on_printing = d['remarks_on_printing']
        if 'seal_order' in d:
            o.seal_order = d['seal_order']
        if 'second_contract_type' in d:
            o.second_contract_type = d['second_contract_type']
        if 'sign_params' in d:
            o.sign_params = d['sign_params']
        if 'sixth_contract_type' in d:
            o.sixth_contract_type = d['sixth_contract_type']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'third_contract_type' in d:
            o.third_contract_type = d['third_contract_type']
        if 'type' in d:
            o.type = d['type']
        return o


