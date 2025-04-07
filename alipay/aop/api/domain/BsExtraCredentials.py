#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsExtraCredentials(object):

    def __init__(self):
        self._brand_name = None
        self._merchant_confirmation_letter = None
        self._power_bank = None
        self._power_bank_img = None
        self._supply_isv_contact_phone_no = None
        self._supply_isv_leads_level = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def merchant_confirmation_letter(self):
        return self._merchant_confirmation_letter

    @merchant_confirmation_letter.setter
    def merchant_confirmation_letter(self, value):
        self._merchant_confirmation_letter = value
    @property
    def power_bank(self):
        return self._power_bank

    @power_bank.setter
    def power_bank(self, value):
        self._power_bank = value
    @property
    def power_bank_img(self):
        return self._power_bank_img

    @power_bank_img.setter
    def power_bank_img(self, value):
        self._power_bank_img = value
    @property
    def supply_isv_contact_phone_no(self):
        return self._supply_isv_contact_phone_no

    @supply_isv_contact_phone_no.setter
    def supply_isv_contact_phone_no(self, value):
        self._supply_isv_contact_phone_no = value
    @property
    def supply_isv_leads_level(self):
        return self._supply_isv_leads_level

    @supply_isv_leads_level.setter
    def supply_isv_leads_level(self, value):
        self._supply_isv_leads_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.merchant_confirmation_letter:
            if hasattr(self.merchant_confirmation_letter, 'to_alipay_dict'):
                params['merchant_confirmation_letter'] = self.merchant_confirmation_letter.to_alipay_dict()
            else:
                params['merchant_confirmation_letter'] = self.merchant_confirmation_letter
        if self.power_bank:
            if hasattr(self.power_bank, 'to_alipay_dict'):
                params['power_bank'] = self.power_bank.to_alipay_dict()
            else:
                params['power_bank'] = self.power_bank
        if self.power_bank_img:
            if hasattr(self.power_bank_img, 'to_alipay_dict'):
                params['power_bank_img'] = self.power_bank_img.to_alipay_dict()
            else:
                params['power_bank_img'] = self.power_bank_img
        if self.supply_isv_contact_phone_no:
            if hasattr(self.supply_isv_contact_phone_no, 'to_alipay_dict'):
                params['supply_isv_contact_phone_no'] = self.supply_isv_contact_phone_no.to_alipay_dict()
            else:
                params['supply_isv_contact_phone_no'] = self.supply_isv_contact_phone_no
        if self.supply_isv_leads_level:
            if hasattr(self.supply_isv_leads_level, 'to_alipay_dict'):
                params['supply_isv_leads_level'] = self.supply_isv_leads_level.to_alipay_dict()
            else:
                params['supply_isv_leads_level'] = self.supply_isv_leads_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsExtraCredentials()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'merchant_confirmation_letter' in d:
            o.merchant_confirmation_letter = d['merchant_confirmation_letter']
        if 'power_bank' in d:
            o.power_bank = d['power_bank']
        if 'power_bank_img' in d:
            o.power_bank_img = d['power_bank_img']
        if 'supply_isv_contact_phone_no' in d:
            o.supply_isv_contact_phone_no = d['supply_isv_contact_phone_no']
        if 'supply_isv_leads_level' in d:
            o.supply_isv_leads_level = d['supply_isv_leads_level']
        return o


