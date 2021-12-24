#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiPeopleDTO import OpenApiPeopleDTO
from alipay.aop.api.domain.ContractOpenApiAttachDTO import ContractOpenApiAttachDTO
from alipay.aop.api.domain.ContractOpenApiAttachDTO import ContractOpenApiAttachDTO
from alipay.aop.api.domain.OpenApiPartnerDTO import OpenApiPartnerDTO
from alipay.aop.api.domain.OpenApiPartnerDTO import OpenApiPartnerDTO
from alipay.aop.api.domain.OpenApiPeopleDTO import OpenApiPeopleDTO
from alipay.aop.api.domain.OpenApiPeopleDTO import OpenApiPeopleDTO
from alipay.aop.api.domain.OpenApiMatterMemberDTO import OpenApiMatterMemberDTO


class ContractDetailQueryDTO(object):

    def __init__(self):
        self._amount = None
        self._amount_type = None
        self._apply_end_time = None
        self._apply_people = None
        self._apply_start_time = None
        self._auto_renew_period = None
        self._auto_renew_period_unit = None
        self._biz_status = None
        self._business_id = None
        self._business_line = None
        self._chain_sign_order = None
        self._comment = None
        self._contract_attach_list = None
        self._contract_code = None
        self._contract_create_time = None
        self._contract_doc = None
        self._contract_duration = None
        self._contract_duration_unit = None
        self._contract_name = None
        self._contract_partner_a_list = None
        self._contract_partner_b_list = None
        self._contract_sign_type = None
        self._contract_tempalte_code = None
        self._corp_entity_list = None
        self._currency = None
        self._delivery_type = None
        self._effect_time = None
        self._effect_type = None
        self._expire_time = None
        self._first_contract_type = None
        self._give_back_type = None
        self._gm_mofified = None
        self._gmt_create = None
        self._in_charge_people_list = None
        self._in_effect_type = None
        self._invoice_target = None
        self._invoice_type = None
        self._is_template = None
        self._legal_peoples = None
        self._matter_code = None
        self._matter_member_list = None
        self._number = None
        self._payer = None
        self._remarks_on_printing = None
        self._seal_order = None
        self._second_contract_type = None
        self._show_biz_status = None
        self._sign_instant_id = None
        self._source_system_id = None
        self._tanant = None
        self._tax_rate = None

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
    def apply_end_time(self):
        return self._apply_end_time

    @apply_end_time.setter
    def apply_end_time(self, value):
        self._apply_end_time = value
    @property
    def apply_people(self):
        return self._apply_people

    @apply_people.setter
    def apply_people(self, value):
        if isinstance(value, OpenApiPeopleDTO):
            self._apply_people = value
        else:
            self._apply_people = OpenApiPeopleDTO.from_alipay_dict(value)
    @property
    def apply_start_time(self):
        return self._apply_start_time

    @apply_start_time.setter
    def apply_start_time(self, value):
        self._apply_start_time = value
    @property
    def auto_renew_period(self):
        return self._auto_renew_period

    @auto_renew_period.setter
    def auto_renew_period(self, value):
        self._auto_renew_period = value
    @property
    def auto_renew_period_unit(self):
        return self._auto_renew_period_unit

    @auto_renew_period_unit.setter
    def auto_renew_period_unit(self, value):
        self._auto_renew_period_unit = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
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
    def chain_sign_order(self):
        return self._chain_sign_order

    @chain_sign_order.setter
    def chain_sign_order(self, value):
        self._chain_sign_order = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def contract_attach_list(self):
        return self._contract_attach_list

    @contract_attach_list.setter
    def contract_attach_list(self, value):
        if isinstance(value, list):
            self._contract_attach_list = list()
            for i in value:
                if isinstance(i, ContractOpenApiAttachDTO):
                    self._contract_attach_list.append(i)
                else:
                    self._contract_attach_list.append(ContractOpenApiAttachDTO.from_alipay_dict(i))
    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def contract_create_time(self):
        return self._contract_create_time

    @contract_create_time.setter
    def contract_create_time(self, value):
        self._contract_create_time = value
    @property
    def contract_doc(self):
        return self._contract_doc

    @contract_doc.setter
    def contract_doc(self, value):
        if isinstance(value, ContractOpenApiAttachDTO):
            self._contract_doc = value
        else:
            self._contract_doc = ContractOpenApiAttachDTO.from_alipay_dict(value)
    @property
    def contract_duration(self):
        return self._contract_duration

    @contract_duration.setter
    def contract_duration(self, value):
        self._contract_duration = value
    @property
    def contract_duration_unit(self):
        return self._contract_duration_unit

    @contract_duration_unit.setter
    def contract_duration_unit(self, value):
        self._contract_duration_unit = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_partner_a_list(self):
        return self._contract_partner_a_list

    @contract_partner_a_list.setter
    def contract_partner_a_list(self, value):
        if isinstance(value, list):
            self._contract_partner_a_list = list()
            for i in value:
                if isinstance(i, OpenApiPartnerDTO):
                    self._contract_partner_a_list.append(i)
                else:
                    self._contract_partner_a_list.append(OpenApiPartnerDTO.from_alipay_dict(i))
    @property
    def contract_partner_b_list(self):
        return self._contract_partner_b_list

    @contract_partner_b_list.setter
    def contract_partner_b_list(self, value):
        if isinstance(value, list):
            self._contract_partner_b_list = list()
            for i in value:
                if isinstance(i, OpenApiPartnerDTO):
                    self._contract_partner_b_list.append(i)
                else:
                    self._contract_partner_b_list.append(OpenApiPartnerDTO.from_alipay_dict(i))
    @property
    def contract_sign_type(self):
        return self._contract_sign_type

    @contract_sign_type.setter
    def contract_sign_type(self, value):
        self._contract_sign_type = value
    @property
    def contract_tempalte_code(self):
        return self._contract_tempalte_code

    @contract_tempalte_code.setter
    def contract_tempalte_code(self, value):
        self._contract_tempalte_code = value
    @property
    def corp_entity_list(self):
        return self._corp_entity_list

    @corp_entity_list.setter
    def corp_entity_list(self, value):
        self._corp_entity_list = value
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
    def first_contract_type(self):
        return self._first_contract_type

    @first_contract_type.setter
    def first_contract_type(self, value):
        self._first_contract_type = value
    @property
    def give_back_type(self):
        return self._give_back_type

    @give_back_type.setter
    def give_back_type(self, value):
        self._give_back_type = value
    @property
    def gm_mofified(self):
        return self._gm_mofified

    @gm_mofified.setter
    def gm_mofified(self, value):
        self._gm_mofified = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def in_charge_people_list(self):
        return self._in_charge_people_list

    @in_charge_people_list.setter
    def in_charge_people_list(self, value):
        if isinstance(value, list):
            self._in_charge_people_list = list()
            for i in value:
                if isinstance(i, OpenApiPeopleDTO):
                    self._in_charge_people_list.append(i)
                else:
                    self._in_charge_people_list.append(OpenApiPeopleDTO.from_alipay_dict(i))
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
    def is_template(self):
        return self._is_template

    @is_template.setter
    def is_template(self, value):
        self._is_template = value
    @property
    def legal_peoples(self):
        return self._legal_peoples

    @legal_peoples.setter
    def legal_peoples(self, value):
        if isinstance(value, list):
            self._legal_peoples = list()
            for i in value:
                if isinstance(i, OpenApiPeopleDTO):
                    self._legal_peoples.append(i)
                else:
                    self._legal_peoples.append(OpenApiPeopleDTO.from_alipay_dict(i))
    @property
    def matter_code(self):
        return self._matter_code

    @matter_code.setter
    def matter_code(self, value):
        self._matter_code = value
    @property
    def matter_member_list(self):
        return self._matter_member_list

    @matter_member_list.setter
    def matter_member_list(self, value):
        if isinstance(value, list):
            self._matter_member_list = list()
            for i in value:
                if isinstance(i, OpenApiMatterMemberDTO):
                    self._matter_member_list.append(i)
                else:
                    self._matter_member_list.append(OpenApiMatterMemberDTO.from_alipay_dict(i))
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def payer(self):
        return self._payer

    @payer.setter
    def payer(self, value):
        self._payer = value
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
    def show_biz_status(self):
        return self._show_biz_status

    @show_biz_status.setter
    def show_biz_status(self, value):
        self._show_biz_status = value
    @property
    def sign_instant_id(self):
        return self._sign_instant_id

    @sign_instant_id.setter
    def sign_instant_id(self, value):
        self._sign_instant_id = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def tanant(self):
        return self._tanant

    @tanant.setter
    def tanant(self, value):
        self._tanant = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


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
        if self.apply_end_time:
            if hasattr(self.apply_end_time, 'to_alipay_dict'):
                params['apply_end_time'] = self.apply_end_time.to_alipay_dict()
            else:
                params['apply_end_time'] = self.apply_end_time
        if self.apply_people:
            if hasattr(self.apply_people, 'to_alipay_dict'):
                params['apply_people'] = self.apply_people.to_alipay_dict()
            else:
                params['apply_people'] = self.apply_people
        if self.apply_start_time:
            if hasattr(self.apply_start_time, 'to_alipay_dict'):
                params['apply_start_time'] = self.apply_start_time.to_alipay_dict()
            else:
                params['apply_start_time'] = self.apply_start_time
        if self.auto_renew_period:
            if hasattr(self.auto_renew_period, 'to_alipay_dict'):
                params['auto_renew_period'] = self.auto_renew_period.to_alipay_dict()
            else:
                params['auto_renew_period'] = self.auto_renew_period
        if self.auto_renew_period_unit:
            if hasattr(self.auto_renew_period_unit, 'to_alipay_dict'):
                params['auto_renew_period_unit'] = self.auto_renew_period_unit.to_alipay_dict()
            else:
                params['auto_renew_period_unit'] = self.auto_renew_period_unit
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
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
        if self.chain_sign_order:
            if hasattr(self.chain_sign_order, 'to_alipay_dict'):
                params['chain_sign_order'] = self.chain_sign_order.to_alipay_dict()
            else:
                params['chain_sign_order'] = self.chain_sign_order
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.contract_attach_list:
            if isinstance(self.contract_attach_list, list):
                for i in range(0, len(self.contract_attach_list)):
                    element = self.contract_attach_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_attach_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_attach_list, 'to_alipay_dict'):
                params['contract_attach_list'] = self.contract_attach_list.to_alipay_dict()
            else:
                params['contract_attach_list'] = self.contract_attach_list
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.contract_create_time:
            if hasattr(self.contract_create_time, 'to_alipay_dict'):
                params['contract_create_time'] = self.contract_create_time.to_alipay_dict()
            else:
                params['contract_create_time'] = self.contract_create_time
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
        if self.contract_duration_unit:
            if hasattr(self.contract_duration_unit, 'to_alipay_dict'):
                params['contract_duration_unit'] = self.contract_duration_unit.to_alipay_dict()
            else:
                params['contract_duration_unit'] = self.contract_duration_unit
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_partner_a_list:
            if isinstance(self.contract_partner_a_list, list):
                for i in range(0, len(self.contract_partner_a_list)):
                    element = self.contract_partner_a_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_partner_a_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_partner_a_list, 'to_alipay_dict'):
                params['contract_partner_a_list'] = self.contract_partner_a_list.to_alipay_dict()
            else:
                params['contract_partner_a_list'] = self.contract_partner_a_list
        if self.contract_partner_b_list:
            if isinstance(self.contract_partner_b_list, list):
                for i in range(0, len(self.contract_partner_b_list)):
                    element = self.contract_partner_b_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_partner_b_list[i] = element.to_alipay_dict()
            if hasattr(self.contract_partner_b_list, 'to_alipay_dict'):
                params['contract_partner_b_list'] = self.contract_partner_b_list.to_alipay_dict()
            else:
                params['contract_partner_b_list'] = self.contract_partner_b_list
        if self.contract_sign_type:
            if hasattr(self.contract_sign_type, 'to_alipay_dict'):
                params['contract_sign_type'] = self.contract_sign_type.to_alipay_dict()
            else:
                params['contract_sign_type'] = self.contract_sign_type
        if self.contract_tempalte_code:
            if hasattr(self.contract_tempalte_code, 'to_alipay_dict'):
                params['contract_tempalte_code'] = self.contract_tempalte_code.to_alipay_dict()
            else:
                params['contract_tempalte_code'] = self.contract_tempalte_code
        if self.corp_entity_list:
            if hasattr(self.corp_entity_list, 'to_alipay_dict'):
                params['corp_entity_list'] = self.corp_entity_list.to_alipay_dict()
            else:
                params['corp_entity_list'] = self.corp_entity_list
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
        if self.first_contract_type:
            if hasattr(self.first_contract_type, 'to_alipay_dict'):
                params['first_contract_type'] = self.first_contract_type.to_alipay_dict()
            else:
                params['first_contract_type'] = self.first_contract_type
        if self.give_back_type:
            if hasattr(self.give_back_type, 'to_alipay_dict'):
                params['give_back_type'] = self.give_back_type.to_alipay_dict()
            else:
                params['give_back_type'] = self.give_back_type
        if self.gm_mofified:
            if hasattr(self.gm_mofified, 'to_alipay_dict'):
                params['gm_mofified'] = self.gm_mofified.to_alipay_dict()
            else:
                params['gm_mofified'] = self.gm_mofified
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.in_charge_people_list:
            if isinstance(self.in_charge_people_list, list):
                for i in range(0, len(self.in_charge_people_list)):
                    element = self.in_charge_people_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.in_charge_people_list[i] = element.to_alipay_dict()
            if hasattr(self.in_charge_people_list, 'to_alipay_dict'):
                params['in_charge_people_list'] = self.in_charge_people_list.to_alipay_dict()
            else:
                params['in_charge_people_list'] = self.in_charge_people_list
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
        if self.is_template:
            if hasattr(self.is_template, 'to_alipay_dict'):
                params['is_template'] = self.is_template.to_alipay_dict()
            else:
                params['is_template'] = self.is_template
        if self.legal_peoples:
            if isinstance(self.legal_peoples, list):
                for i in range(0, len(self.legal_peoples)):
                    element = self.legal_peoples[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.legal_peoples[i] = element.to_alipay_dict()
            if hasattr(self.legal_peoples, 'to_alipay_dict'):
                params['legal_peoples'] = self.legal_peoples.to_alipay_dict()
            else:
                params['legal_peoples'] = self.legal_peoples
        if self.matter_code:
            if hasattr(self.matter_code, 'to_alipay_dict'):
                params['matter_code'] = self.matter_code.to_alipay_dict()
            else:
                params['matter_code'] = self.matter_code
        if self.matter_member_list:
            if isinstance(self.matter_member_list, list):
                for i in range(0, len(self.matter_member_list)):
                    element = self.matter_member_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.matter_member_list[i] = element.to_alipay_dict()
            if hasattr(self.matter_member_list, 'to_alipay_dict'):
                params['matter_member_list'] = self.matter_member_list.to_alipay_dict()
            else:
                params['matter_member_list'] = self.matter_member_list
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.payer:
            if hasattr(self.payer, 'to_alipay_dict'):
                params['payer'] = self.payer.to_alipay_dict()
            else:
                params['payer'] = self.payer
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
        if self.show_biz_status:
            if hasattr(self.show_biz_status, 'to_alipay_dict'):
                params['show_biz_status'] = self.show_biz_status.to_alipay_dict()
            else:
                params['show_biz_status'] = self.show_biz_status
        if self.sign_instant_id:
            if hasattr(self.sign_instant_id, 'to_alipay_dict'):
                params['sign_instant_id'] = self.sign_instant_id.to_alipay_dict()
            else:
                params['sign_instant_id'] = self.sign_instant_id
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.tanant:
            if hasattr(self.tanant, 'to_alipay_dict'):
                params['tanant'] = self.tanant.to_alipay_dict()
            else:
                params['tanant'] = self.tanant
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractDetailQueryDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_type' in d:
            o.amount_type = d['amount_type']
        if 'apply_end_time' in d:
            o.apply_end_time = d['apply_end_time']
        if 'apply_people' in d:
            o.apply_people = d['apply_people']
        if 'apply_start_time' in d:
            o.apply_start_time = d['apply_start_time']
        if 'auto_renew_period' in d:
            o.auto_renew_period = d['auto_renew_period']
        if 'auto_renew_period_unit' in d:
            o.auto_renew_period_unit = d['auto_renew_period_unit']
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'business_line' in d:
            o.business_line = d['business_line']
        if 'chain_sign_order' in d:
            o.chain_sign_order = d['chain_sign_order']
        if 'comment' in d:
            o.comment = d['comment']
        if 'contract_attach_list' in d:
            o.contract_attach_list = d['contract_attach_list']
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'contract_create_time' in d:
            o.contract_create_time = d['contract_create_time']
        if 'contract_doc' in d:
            o.contract_doc = d['contract_doc']
        if 'contract_duration' in d:
            o.contract_duration = d['contract_duration']
        if 'contract_duration_unit' in d:
            o.contract_duration_unit = d['contract_duration_unit']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_partner_a_list' in d:
            o.contract_partner_a_list = d['contract_partner_a_list']
        if 'contract_partner_b_list' in d:
            o.contract_partner_b_list = d['contract_partner_b_list']
        if 'contract_sign_type' in d:
            o.contract_sign_type = d['contract_sign_type']
        if 'contract_tempalte_code' in d:
            o.contract_tempalte_code = d['contract_tempalte_code']
        if 'corp_entity_list' in d:
            o.corp_entity_list = d['corp_entity_list']
        if 'currency' in d:
            o.currency = d['currency']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'effect_type' in d:
            o.effect_type = d['effect_type']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'first_contract_type' in d:
            o.first_contract_type = d['first_contract_type']
        if 'give_back_type' in d:
            o.give_back_type = d['give_back_type']
        if 'gm_mofified' in d:
            o.gm_mofified = d['gm_mofified']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'in_charge_people_list' in d:
            o.in_charge_people_list = d['in_charge_people_list']
        if 'in_effect_type' in d:
            o.in_effect_type = d['in_effect_type']
        if 'invoice_target' in d:
            o.invoice_target = d['invoice_target']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'is_template' in d:
            o.is_template = d['is_template']
        if 'legal_peoples' in d:
            o.legal_peoples = d['legal_peoples']
        if 'matter_code' in d:
            o.matter_code = d['matter_code']
        if 'matter_member_list' in d:
            o.matter_member_list = d['matter_member_list']
        if 'number' in d:
            o.number = d['number']
        if 'payer' in d:
            o.payer = d['payer']
        if 'remarks_on_printing' in d:
            o.remarks_on_printing = d['remarks_on_printing']
        if 'seal_order' in d:
            o.seal_order = d['seal_order']
        if 'second_contract_type' in d:
            o.second_contract_type = d['second_contract_type']
        if 'show_biz_status' in d:
            o.show_biz_status = d['show_biz_status']
        if 'sign_instant_id' in d:
            o.sign_instant_id = d['sign_instant_id']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tanant' in d:
            o.tanant = d['tanant']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


