#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarInsuranceRenewalOrderInfo(object):

    def __init__(self):
        self._city_code = None
        self._commercial_insurance_amount = None
        self._compulsory_insurance_amount = None
        self._energy_type = None
        self._engine_no = None
        self._insurance_company_name = None
        self._order_amount = None
        self._policy_no = None
        self._promotion_store_id = None
        self._promotion_store_name = None
        self._register_date = None
        self._uscc = None
        self._use_type = None
        self._veh_model_name = None
        self._veh_owner_id_card_no = None
        self._veh_owner_name = None
        self._veh_owner_phone = None
        self._vi_number = None
        self._vin = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def commercial_insurance_amount(self):
        return self._commercial_insurance_amount

    @commercial_insurance_amount.setter
    def commercial_insurance_amount(self, value):
        self._commercial_insurance_amount = value
    @property
    def compulsory_insurance_amount(self):
        return self._compulsory_insurance_amount

    @compulsory_insurance_amount.setter
    def compulsory_insurance_amount(self, value):
        self._compulsory_insurance_amount = value
    @property
    def energy_type(self):
        return self._energy_type

    @energy_type.setter
    def energy_type(self, value):
        self._energy_type = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def insurance_company_name(self):
        return self._insurance_company_name

    @insurance_company_name.setter
    def insurance_company_name(self, value):
        self._insurance_company_name = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def promotion_store_id(self):
        return self._promotion_store_id

    @promotion_store_id.setter
    def promotion_store_id(self, value):
        self._promotion_store_id = value
    @property
    def promotion_store_name(self):
        return self._promotion_store_name

    @promotion_store_name.setter
    def promotion_store_name(self, value):
        self._promotion_store_name = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value
    @property
    def use_type(self):
        return self._use_type

    @use_type.setter
    def use_type(self, value):
        self._use_type = value
    @property
    def veh_model_name(self):
        return self._veh_model_name

    @veh_model_name.setter
    def veh_model_name(self, value):
        self._veh_model_name = value
    @property
    def veh_owner_id_card_no(self):
        return self._veh_owner_id_card_no

    @veh_owner_id_card_no.setter
    def veh_owner_id_card_no(self, value):
        self._veh_owner_id_card_no = value
    @property
    def veh_owner_name(self):
        return self._veh_owner_name

    @veh_owner_name.setter
    def veh_owner_name(self, value):
        self._veh_owner_name = value
    @property
    def veh_owner_phone(self):
        return self._veh_owner_phone

    @veh_owner_phone.setter
    def veh_owner_phone(self, value):
        self._veh_owner_phone = value
    @property
    def vi_number(self):
        return self._vi_number

    @vi_number.setter
    def vi_number(self, value):
        self._vi_number = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.commercial_insurance_amount:
            if hasattr(self.commercial_insurance_amount, 'to_alipay_dict'):
                params['commercial_insurance_amount'] = self.commercial_insurance_amount.to_alipay_dict()
            else:
                params['commercial_insurance_amount'] = self.commercial_insurance_amount
        if self.compulsory_insurance_amount:
            if hasattr(self.compulsory_insurance_amount, 'to_alipay_dict'):
                params['compulsory_insurance_amount'] = self.compulsory_insurance_amount.to_alipay_dict()
            else:
                params['compulsory_insurance_amount'] = self.compulsory_insurance_amount
        if self.energy_type:
            if hasattr(self.energy_type, 'to_alipay_dict'):
                params['energy_type'] = self.energy_type.to_alipay_dict()
            else:
                params['energy_type'] = self.energy_type
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.insurance_company_name:
            if hasattr(self.insurance_company_name, 'to_alipay_dict'):
                params['insurance_company_name'] = self.insurance_company_name.to_alipay_dict()
            else:
                params['insurance_company_name'] = self.insurance_company_name
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.promotion_store_id:
            if hasattr(self.promotion_store_id, 'to_alipay_dict'):
                params['promotion_store_id'] = self.promotion_store_id.to_alipay_dict()
            else:
                params['promotion_store_id'] = self.promotion_store_id
        if self.promotion_store_name:
            if hasattr(self.promotion_store_name, 'to_alipay_dict'):
                params['promotion_store_name'] = self.promotion_store_name.to_alipay_dict()
            else:
                params['promotion_store_name'] = self.promotion_store_name
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        if self.use_type:
            if hasattr(self.use_type, 'to_alipay_dict'):
                params['use_type'] = self.use_type.to_alipay_dict()
            else:
                params['use_type'] = self.use_type
        if self.veh_model_name:
            if hasattr(self.veh_model_name, 'to_alipay_dict'):
                params['veh_model_name'] = self.veh_model_name.to_alipay_dict()
            else:
                params['veh_model_name'] = self.veh_model_name
        if self.veh_owner_id_card_no:
            if hasattr(self.veh_owner_id_card_no, 'to_alipay_dict'):
                params['veh_owner_id_card_no'] = self.veh_owner_id_card_no.to_alipay_dict()
            else:
                params['veh_owner_id_card_no'] = self.veh_owner_id_card_no
        if self.veh_owner_name:
            if hasattr(self.veh_owner_name, 'to_alipay_dict'):
                params['veh_owner_name'] = self.veh_owner_name.to_alipay_dict()
            else:
                params['veh_owner_name'] = self.veh_owner_name
        if self.veh_owner_phone:
            if hasattr(self.veh_owner_phone, 'to_alipay_dict'):
                params['veh_owner_phone'] = self.veh_owner_phone.to_alipay_dict()
            else:
                params['veh_owner_phone'] = self.veh_owner_phone
        if self.vi_number:
            if hasattr(self.vi_number, 'to_alipay_dict'):
                params['vi_number'] = self.vi_number.to_alipay_dict()
            else:
                params['vi_number'] = self.vi_number
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarInsuranceRenewalOrderInfo()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'commercial_insurance_amount' in d:
            o.commercial_insurance_amount = d['commercial_insurance_amount']
        if 'compulsory_insurance_amount' in d:
            o.compulsory_insurance_amount = d['compulsory_insurance_amount']
        if 'energy_type' in d:
            o.energy_type = d['energy_type']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'insurance_company_name' in d:
            o.insurance_company_name = d['insurance_company_name']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'promotion_store_id' in d:
            o.promotion_store_id = d['promotion_store_id']
        if 'promotion_store_name' in d:
            o.promotion_store_name = d['promotion_store_name']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'uscc' in d:
            o.uscc = d['uscc']
        if 'use_type' in d:
            o.use_type = d['use_type']
        if 'veh_model_name' in d:
            o.veh_model_name = d['veh_model_name']
        if 'veh_owner_id_card_no' in d:
            o.veh_owner_id_card_no = d['veh_owner_id_card_no']
        if 'veh_owner_name' in d:
            o.veh_owner_name = d['veh_owner_name']
        if 'veh_owner_phone' in d:
            o.veh_owner_phone = d['veh_owner_phone']
        if 'vi_number' in d:
            o.vi_number = d['vi_number']
        if 'vin' in d:
            o.vin = d['vin']
        return o


