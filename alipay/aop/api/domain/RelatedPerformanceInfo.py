#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RelatedPerformanceInfo(object):

    def __init__(self):
        self._address = None
        self._cancel_date = None
        self._city = None
        self._con_form = None
        self._county = None
        self._credit_code = None
        self._currency = None
        self._ent_id = None
        self._ent_name = None
        self._ent_status = None
        self._ent_type = None
        self._es_date = None
        self._funde_ratio = None
        self._funded_ratio = None
        self._industry_code = None
        self._industry_name = None
        self._industry_phy_code = None
        self._industry_phy_name = None
        self._position = None
        self._province = None
        self._reg_cap = None
        self._reg_cap_cur = None
        self._reg_city = None
        self._reg_no = None
        self._revoke_date = None
        self._ry_name = None
        self._sub_conam = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def cancel_date(self):
        return self._cancel_date

    @cancel_date.setter
    def cancel_date(self, value):
        self._cancel_date = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def con_form(self):
        return self._con_form

    @con_form.setter
    def con_form(self, value):
        self._con_form = value
    @property
    def county(self):
        return self._county

    @county.setter
    def county(self, value):
        self._county = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def ent_id(self):
        return self._ent_id

    @ent_id.setter
    def ent_id(self, value):
        self._ent_id = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def ent_status(self):
        return self._ent_status

    @ent_status.setter
    def ent_status(self, value):
        self._ent_status = value
    @property
    def ent_type(self):
        return self._ent_type

    @ent_type.setter
    def ent_type(self, value):
        self._ent_type = value
    @property
    def es_date(self):
        return self._es_date

    @es_date.setter
    def es_date(self, value):
        self._es_date = value
    @property
    def funde_ratio(self):
        return self._funde_ratio

    @funde_ratio.setter
    def funde_ratio(self, value):
        self._funde_ratio = value
    @property
    def funded_ratio(self):
        return self._funded_ratio

    @funded_ratio.setter
    def funded_ratio(self, value):
        self._funded_ratio = value
    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def industry_name(self):
        return self._industry_name

    @industry_name.setter
    def industry_name(self, value):
        self._industry_name = value
    @property
    def industry_phy_code(self):
        return self._industry_phy_code

    @industry_phy_code.setter
    def industry_phy_code(self, value):
        self._industry_phy_code = value
    @property
    def industry_phy_name(self):
        return self._industry_phy_name

    @industry_phy_name.setter
    def industry_phy_name(self, value):
        self._industry_phy_name = value
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def reg_cap(self):
        return self._reg_cap

    @reg_cap.setter
    def reg_cap(self, value):
        self._reg_cap = value
    @property
    def reg_cap_cur(self):
        return self._reg_cap_cur

    @reg_cap_cur.setter
    def reg_cap_cur(self, value):
        self._reg_cap_cur = value
    @property
    def reg_city(self):
        return self._reg_city

    @reg_city.setter
    def reg_city(self, value):
        self._reg_city = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def revoke_date(self):
        return self._revoke_date

    @revoke_date.setter
    def revoke_date(self, value):
        self._revoke_date = value
    @property
    def ry_name(self):
        return self._ry_name

    @ry_name.setter
    def ry_name(self, value):
        self._ry_name = value
    @property
    def sub_conam(self):
        return self._sub_conam

    @sub_conam.setter
    def sub_conam(self, value):
        self._sub_conam = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.cancel_date:
            if hasattr(self.cancel_date, 'to_alipay_dict'):
                params['cancel_date'] = self.cancel_date.to_alipay_dict()
            else:
                params['cancel_date'] = self.cancel_date
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.con_form:
            if hasattr(self.con_form, 'to_alipay_dict'):
                params['con_form'] = self.con_form.to_alipay_dict()
            else:
                params['con_form'] = self.con_form
        if self.county:
            if hasattr(self.county, 'to_alipay_dict'):
                params['county'] = self.county.to_alipay_dict()
            else:
                params['county'] = self.county
        if self.credit_code:
            if hasattr(self.credit_code, 'to_alipay_dict'):
                params['credit_code'] = self.credit_code.to_alipay_dict()
            else:
                params['credit_code'] = self.credit_code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.ent_id:
            if hasattr(self.ent_id, 'to_alipay_dict'):
                params['ent_id'] = self.ent_id.to_alipay_dict()
            else:
                params['ent_id'] = self.ent_id
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.ent_status:
            if hasattr(self.ent_status, 'to_alipay_dict'):
                params['ent_status'] = self.ent_status.to_alipay_dict()
            else:
                params['ent_status'] = self.ent_status
        if self.ent_type:
            if hasattr(self.ent_type, 'to_alipay_dict'):
                params['ent_type'] = self.ent_type.to_alipay_dict()
            else:
                params['ent_type'] = self.ent_type
        if self.es_date:
            if hasattr(self.es_date, 'to_alipay_dict'):
                params['es_date'] = self.es_date.to_alipay_dict()
            else:
                params['es_date'] = self.es_date
        if self.funde_ratio:
            if hasattr(self.funde_ratio, 'to_alipay_dict'):
                params['funde_ratio'] = self.funde_ratio.to_alipay_dict()
            else:
                params['funde_ratio'] = self.funde_ratio
        if self.funded_ratio:
            if hasattr(self.funded_ratio, 'to_alipay_dict'):
                params['funded_ratio'] = self.funded_ratio.to_alipay_dict()
            else:
                params['funded_ratio'] = self.funded_ratio
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.industry_name:
            if hasattr(self.industry_name, 'to_alipay_dict'):
                params['industry_name'] = self.industry_name.to_alipay_dict()
            else:
                params['industry_name'] = self.industry_name
        if self.industry_phy_code:
            if hasattr(self.industry_phy_code, 'to_alipay_dict'):
                params['industry_phy_code'] = self.industry_phy_code.to_alipay_dict()
            else:
                params['industry_phy_code'] = self.industry_phy_code
        if self.industry_phy_name:
            if hasattr(self.industry_phy_name, 'to_alipay_dict'):
                params['industry_phy_name'] = self.industry_phy_name.to_alipay_dict()
            else:
                params['industry_phy_name'] = self.industry_phy_name
        if self.position:
            if hasattr(self.position, 'to_alipay_dict'):
                params['position'] = self.position.to_alipay_dict()
            else:
                params['position'] = self.position
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.reg_cap:
            if hasattr(self.reg_cap, 'to_alipay_dict'):
                params['reg_cap'] = self.reg_cap.to_alipay_dict()
            else:
                params['reg_cap'] = self.reg_cap
        if self.reg_cap_cur:
            if hasattr(self.reg_cap_cur, 'to_alipay_dict'):
                params['reg_cap_cur'] = self.reg_cap_cur.to_alipay_dict()
            else:
                params['reg_cap_cur'] = self.reg_cap_cur
        if self.reg_city:
            if hasattr(self.reg_city, 'to_alipay_dict'):
                params['reg_city'] = self.reg_city.to_alipay_dict()
            else:
                params['reg_city'] = self.reg_city
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
        if self.revoke_date:
            if hasattr(self.revoke_date, 'to_alipay_dict'):
                params['revoke_date'] = self.revoke_date.to_alipay_dict()
            else:
                params['revoke_date'] = self.revoke_date
        if self.ry_name:
            if hasattr(self.ry_name, 'to_alipay_dict'):
                params['ry_name'] = self.ry_name.to_alipay_dict()
            else:
                params['ry_name'] = self.ry_name
        if self.sub_conam:
            if hasattr(self.sub_conam, 'to_alipay_dict'):
                params['sub_conam'] = self.sub_conam.to_alipay_dict()
            else:
                params['sub_conam'] = self.sub_conam
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RelatedPerformanceInfo()
        if 'address' in d:
            o.address = d['address']
        if 'cancel_date' in d:
            o.cancel_date = d['cancel_date']
        if 'city' in d:
            o.city = d['city']
        if 'con_form' in d:
            o.con_form = d['con_form']
        if 'county' in d:
            o.county = d['county']
        if 'credit_code' in d:
            o.credit_code = d['credit_code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'ent_id' in d:
            o.ent_id = d['ent_id']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'ent_status' in d:
            o.ent_status = d['ent_status']
        if 'ent_type' in d:
            o.ent_type = d['ent_type']
        if 'es_date' in d:
            o.es_date = d['es_date']
        if 'funde_ratio' in d:
            o.funde_ratio = d['funde_ratio']
        if 'funded_ratio' in d:
            o.funded_ratio = d['funded_ratio']
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'industry_name' in d:
            o.industry_name = d['industry_name']
        if 'industry_phy_code' in d:
            o.industry_phy_code = d['industry_phy_code']
        if 'industry_phy_name' in d:
            o.industry_phy_name = d['industry_phy_name']
        if 'position' in d:
            o.position = d['position']
        if 'province' in d:
            o.province = d['province']
        if 'reg_cap' in d:
            o.reg_cap = d['reg_cap']
        if 'reg_cap_cur' in d:
            o.reg_cap_cur = d['reg_cap_cur']
        if 'reg_city' in d:
            o.reg_city = d['reg_city']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'revoke_date' in d:
            o.revoke_date = d['revoke_date']
        if 'ry_name' in d:
            o.ry_name = d['ry_name']
        if 'sub_conam' in d:
            o.sub_conam = d['sub_conam']
        return o


