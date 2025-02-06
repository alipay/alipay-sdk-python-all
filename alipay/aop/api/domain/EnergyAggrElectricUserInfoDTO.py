#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnergyAggrElectricUserInfoDTO(object):

    def __init__(self):
        self._address = None
        self._annual_electric_consumption_range = None
        self._buy_electric_from_state_grid = None
        self._company_name = None
        self._contact_name = None
        self._contact_num = None
        self._electric_account_id = None
        self._gmt_create = None
        self._payment_type = None
        self._province = None
        self._social_credit_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def annual_electric_consumption_range(self):
        return self._annual_electric_consumption_range

    @annual_electric_consumption_range.setter
    def annual_electric_consumption_range(self, value):
        self._annual_electric_consumption_range = value
    @property
    def buy_electric_from_state_grid(self):
        return self._buy_electric_from_state_grid

    @buy_electric_from_state_grid.setter
    def buy_electric_from_state_grid(self, value):
        self._buy_electric_from_state_grid = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_num(self):
        return self._contact_num

    @contact_num.setter
    def contact_num(self, value):
        self._contact_num = value
    @property
    def electric_account_id(self):
        return self._electric_account_id

    @electric_account_id.setter
    def electric_account_id(self, value):
        self._electric_account_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def social_credit_code(self):
        return self._social_credit_code

    @social_credit_code.setter
    def social_credit_code(self, value):
        self._social_credit_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.annual_electric_consumption_range:
            if hasattr(self.annual_electric_consumption_range, 'to_alipay_dict'):
                params['annual_electric_consumption_range'] = self.annual_electric_consumption_range.to_alipay_dict()
            else:
                params['annual_electric_consumption_range'] = self.annual_electric_consumption_range
        if self.buy_electric_from_state_grid:
            if hasattr(self.buy_electric_from_state_grid, 'to_alipay_dict'):
                params['buy_electric_from_state_grid'] = self.buy_electric_from_state_grid.to_alipay_dict()
            else:
                params['buy_electric_from_state_grid'] = self.buy_electric_from_state_grid
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_num:
            if hasattr(self.contact_num, 'to_alipay_dict'):
                params['contact_num'] = self.contact_num.to_alipay_dict()
            else:
                params['contact_num'] = self.contact_num
        if self.electric_account_id:
            if hasattr(self.electric_account_id, 'to_alipay_dict'):
                params['electric_account_id'] = self.electric_account_id.to_alipay_dict()
            else:
                params['electric_account_id'] = self.electric_account_id
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.social_credit_code:
            if hasattr(self.social_credit_code, 'to_alipay_dict'):
                params['social_credit_code'] = self.social_credit_code.to_alipay_dict()
            else:
                params['social_credit_code'] = self.social_credit_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnergyAggrElectricUserInfoDTO()
        if 'address' in d:
            o.address = d['address']
        if 'annual_electric_consumption_range' in d:
            o.annual_electric_consumption_range = d['annual_electric_consumption_range']
        if 'buy_electric_from_state_grid' in d:
            o.buy_electric_from_state_grid = d['buy_electric_from_state_grid']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_num' in d:
            o.contact_num = d['contact_num']
        if 'electric_account_id' in d:
            o.electric_account_id = d['electric_account_id']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'province' in d:
            o.province = d['province']
        if 'social_credit_code' in d:
            o.social_credit_code = d['social_credit_code']
        return o


