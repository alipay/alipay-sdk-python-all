#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantInformation(object):

    def __init__(self):
        self._address = None
        self._advance_amount = None
        self._city_desc = None
        self._collection_settlement = None
        self._country_desc = None
        self._district_desc = None
        self._mcc_code = None
        self._mcc_industry_one = None
        self._mcc_industry_two = None
        self._merchant_name = None
        self._mid = None
        self._zip_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def advance_amount(self):
        return self._advance_amount

    @advance_amount.setter
    def advance_amount(self, value):
        self._advance_amount = value
    @property
    def city_desc(self):
        return self._city_desc

    @city_desc.setter
    def city_desc(self, value):
        self._city_desc = value
    @property
    def collection_settlement(self):
        return self._collection_settlement

    @collection_settlement.setter
    def collection_settlement(self, value):
        self._collection_settlement = value
    @property
    def country_desc(self):
        return self._country_desc

    @country_desc.setter
    def country_desc(self, value):
        self._country_desc = value
    @property
    def district_desc(self):
        return self._district_desc

    @district_desc.setter
    def district_desc(self, value):
        self._district_desc = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def mcc_industry_one(self):
        return self._mcc_industry_one

    @mcc_industry_one.setter
    def mcc_industry_one(self, value):
        self._mcc_industry_one = value
    @property
    def mcc_industry_two(self):
        return self._mcc_industry_two

    @mcc_industry_two.setter
    def mcc_industry_two(self, value):
        self._mcc_industry_two = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.advance_amount:
            if hasattr(self.advance_amount, 'to_alipay_dict'):
                params['advance_amount'] = self.advance_amount.to_alipay_dict()
            else:
                params['advance_amount'] = self.advance_amount
        if self.city_desc:
            if hasattr(self.city_desc, 'to_alipay_dict'):
                params['city_desc'] = self.city_desc.to_alipay_dict()
            else:
                params['city_desc'] = self.city_desc
        if self.collection_settlement:
            if hasattr(self.collection_settlement, 'to_alipay_dict'):
                params['collection_settlement'] = self.collection_settlement.to_alipay_dict()
            else:
                params['collection_settlement'] = self.collection_settlement
        if self.country_desc:
            if hasattr(self.country_desc, 'to_alipay_dict'):
                params['country_desc'] = self.country_desc.to_alipay_dict()
            else:
                params['country_desc'] = self.country_desc
        if self.district_desc:
            if hasattr(self.district_desc, 'to_alipay_dict'):
                params['district_desc'] = self.district_desc.to_alipay_dict()
            else:
                params['district_desc'] = self.district_desc
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.mcc_industry_one:
            if hasattr(self.mcc_industry_one, 'to_alipay_dict'):
                params['mcc_industry_one'] = self.mcc_industry_one.to_alipay_dict()
            else:
                params['mcc_industry_one'] = self.mcc_industry_one
        if self.mcc_industry_two:
            if hasattr(self.mcc_industry_two, 'to_alipay_dict'):
                params['mcc_industry_two'] = self.mcc_industry_two.to_alipay_dict()
            else:
                params['mcc_industry_two'] = self.mcc_industry_two
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.zip_code:
            if hasattr(self.zip_code, 'to_alipay_dict'):
                params['zip_code'] = self.zip_code.to_alipay_dict()
            else:
                params['zip_code'] = self.zip_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantInformation()
        if 'address' in d:
            o.address = d['address']
        if 'advance_amount' in d:
            o.advance_amount = d['advance_amount']
        if 'city_desc' in d:
            o.city_desc = d['city_desc']
        if 'collection_settlement' in d:
            o.collection_settlement = d['collection_settlement']
        if 'country_desc' in d:
            o.country_desc = d['country_desc']
        if 'district_desc' in d:
            o.district_desc = d['district_desc']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'mcc_industry_one' in d:
            o.mcc_industry_one = d['mcc_industry_one']
        if 'mcc_industry_two' in d:
            o.mcc_industry_two = d['mcc_industry_two']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'mid' in d:
            o.mid = d['mid']
        if 'zip_code' in d:
            o.zip_code = d['zip_code']
        return o


