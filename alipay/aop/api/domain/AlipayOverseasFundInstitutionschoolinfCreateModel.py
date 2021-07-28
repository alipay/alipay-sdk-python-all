#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasFundInstitutionschoolinfCreateModel(object):

    def __init__(self):
        self._attr_code = None
        self._bussess_adr = None
        self._city_code = None
        self._city_name = None
        self._country_code = None
        self._cust_type = None
        self._declare_type = None
        self._district_code = None
        self._district_name = None
        self._economy_type_code = None
        self._ext_info = None
        self._investment_country_code_one = None
        self._is_special_economic_zone = None
        self._isv_name = None
        self._isv_phone = None
        self._isv_request_no = None
        self._link_man_name = None
        self._link_phone = None
        self._office_adr_en = None
        self._org_name_en = None
        self._org_type = None
        self._province_code = None
        self._province_name = None
        self._remark_info = None
        self._school_address = None
        self._school_country = None
        self._school_en_name = None
        self._school_icon = None
        self._school_icon_type = None
        self._school_mcc = None
        self._school_name = None
        self._school_pid = None
        self._school_stdcode = None
        self._school_type = None
        self._school_zipcode = None
        self._special_economic_zone_company_type = None
        self._trans_email = None

    @property
    def attr_code(self):
        return self._attr_code

    @attr_code.setter
    def attr_code(self, value):
        self._attr_code = value
    @property
    def bussess_adr(self):
        return self._bussess_adr

    @bussess_adr.setter
    def bussess_adr(self, value):
        self._bussess_adr = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def cust_type(self):
        return self._cust_type

    @cust_type.setter
    def cust_type(self, value):
        self._cust_type = value
    @property
    def declare_type(self):
        return self._declare_type

    @declare_type.setter
    def declare_type(self, value):
        self._declare_type = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def economy_type_code(self):
        return self._economy_type_code

    @economy_type_code.setter
    def economy_type_code(self, value):
        self._economy_type_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def investment_country_code_one(self):
        return self._investment_country_code_one

    @investment_country_code_one.setter
    def investment_country_code_one(self, value):
        self._investment_country_code_one = value
    @property
    def is_special_economic_zone(self):
        return self._is_special_economic_zone

    @is_special_economic_zone.setter
    def is_special_economic_zone(self, value):
        self._is_special_economic_zone = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_phone(self):
        return self._isv_phone

    @isv_phone.setter
    def isv_phone(self, value):
        self._isv_phone = value
    @property
    def isv_request_no(self):
        return self._isv_request_no

    @isv_request_no.setter
    def isv_request_no(self, value):
        self._isv_request_no = value
    @property
    def link_man_name(self):
        return self._link_man_name

    @link_man_name.setter
    def link_man_name(self, value):
        self._link_man_name = value
    @property
    def link_phone(self):
        return self._link_phone

    @link_phone.setter
    def link_phone(self, value):
        self._link_phone = value
    @property
    def office_adr_en(self):
        return self._office_adr_en

    @office_adr_en.setter
    def office_adr_en(self, value):
        self._office_adr_en = value
    @property
    def org_name_en(self):
        return self._org_name_en

    @org_name_en.setter
    def org_name_en(self, value):
        self._org_name_en = value
    @property
    def org_type(self):
        return self._org_type

    @org_type.setter
    def org_type(self, value):
        self._org_type = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def remark_info(self):
        return self._remark_info

    @remark_info.setter
    def remark_info(self, value):
        self._remark_info = value
    @property
    def school_address(self):
        return self._school_address

    @school_address.setter
    def school_address(self, value):
        self._school_address = value
    @property
    def school_country(self):
        return self._school_country

    @school_country.setter
    def school_country(self, value):
        self._school_country = value
    @property
    def school_en_name(self):
        return self._school_en_name

    @school_en_name.setter
    def school_en_name(self, value):
        self._school_en_name = value
    @property
    def school_icon(self):
        return self._school_icon

    @school_icon.setter
    def school_icon(self, value):
        self._school_icon = value
    @property
    def school_icon_type(self):
        return self._school_icon_type

    @school_icon_type.setter
    def school_icon_type(self, value):
        self._school_icon_type = value
    @property
    def school_mcc(self):
        return self._school_mcc

    @school_mcc.setter
    def school_mcc(self, value):
        self._school_mcc = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value
    @property
    def school_type(self):
        return self._school_type

    @school_type.setter
    def school_type(self, value):
        self._school_type = value
    @property
    def school_zipcode(self):
        return self._school_zipcode

    @school_zipcode.setter
    def school_zipcode(self, value):
        self._school_zipcode = value
    @property
    def special_economic_zone_company_type(self):
        return self._special_economic_zone_company_type

    @special_economic_zone_company_type.setter
    def special_economic_zone_company_type(self, value):
        self._special_economic_zone_company_type = value
    @property
    def trans_email(self):
        return self._trans_email

    @trans_email.setter
    def trans_email(self, value):
        self._trans_email = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_code:
            if hasattr(self.attr_code, 'to_alipay_dict'):
                params['attr_code'] = self.attr_code.to_alipay_dict()
            else:
                params['attr_code'] = self.attr_code
        if self.bussess_adr:
            if hasattr(self.bussess_adr, 'to_alipay_dict'):
                params['bussess_adr'] = self.bussess_adr.to_alipay_dict()
            else:
                params['bussess_adr'] = self.bussess_adr
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
        if self.cust_type:
            if hasattr(self.cust_type, 'to_alipay_dict'):
                params['cust_type'] = self.cust_type.to_alipay_dict()
            else:
                params['cust_type'] = self.cust_type
        if self.declare_type:
            if hasattr(self.declare_type, 'to_alipay_dict'):
                params['declare_type'] = self.declare_type.to_alipay_dict()
            else:
                params['declare_type'] = self.declare_type
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.economy_type_code:
            if hasattr(self.economy_type_code, 'to_alipay_dict'):
                params['economy_type_code'] = self.economy_type_code.to_alipay_dict()
            else:
                params['economy_type_code'] = self.economy_type_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.investment_country_code_one:
            if hasattr(self.investment_country_code_one, 'to_alipay_dict'):
                params['investment_country_code_one'] = self.investment_country_code_one.to_alipay_dict()
            else:
                params['investment_country_code_one'] = self.investment_country_code_one
        if self.is_special_economic_zone:
            if hasattr(self.is_special_economic_zone, 'to_alipay_dict'):
                params['is_special_economic_zone'] = self.is_special_economic_zone.to_alipay_dict()
            else:
                params['is_special_economic_zone'] = self.is_special_economic_zone
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_phone:
            if hasattr(self.isv_phone, 'to_alipay_dict'):
                params['isv_phone'] = self.isv_phone.to_alipay_dict()
            else:
                params['isv_phone'] = self.isv_phone
        if self.isv_request_no:
            if hasattr(self.isv_request_no, 'to_alipay_dict'):
                params['isv_request_no'] = self.isv_request_no.to_alipay_dict()
            else:
                params['isv_request_no'] = self.isv_request_no
        if self.link_man_name:
            if hasattr(self.link_man_name, 'to_alipay_dict'):
                params['link_man_name'] = self.link_man_name.to_alipay_dict()
            else:
                params['link_man_name'] = self.link_man_name
        if self.link_phone:
            if hasattr(self.link_phone, 'to_alipay_dict'):
                params['link_phone'] = self.link_phone.to_alipay_dict()
            else:
                params['link_phone'] = self.link_phone
        if self.office_adr_en:
            if hasattr(self.office_adr_en, 'to_alipay_dict'):
                params['office_adr_en'] = self.office_adr_en.to_alipay_dict()
            else:
                params['office_adr_en'] = self.office_adr_en
        if self.org_name_en:
            if hasattr(self.org_name_en, 'to_alipay_dict'):
                params['org_name_en'] = self.org_name_en.to_alipay_dict()
            else:
                params['org_name_en'] = self.org_name_en
        if self.org_type:
            if hasattr(self.org_type, 'to_alipay_dict'):
                params['org_type'] = self.org_type.to_alipay_dict()
            else:
                params['org_type'] = self.org_type
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.remark_info:
            if hasattr(self.remark_info, 'to_alipay_dict'):
                params['remark_info'] = self.remark_info.to_alipay_dict()
            else:
                params['remark_info'] = self.remark_info
        if self.school_address:
            if hasattr(self.school_address, 'to_alipay_dict'):
                params['school_address'] = self.school_address.to_alipay_dict()
            else:
                params['school_address'] = self.school_address
        if self.school_country:
            if hasattr(self.school_country, 'to_alipay_dict'):
                params['school_country'] = self.school_country.to_alipay_dict()
            else:
                params['school_country'] = self.school_country
        if self.school_en_name:
            if hasattr(self.school_en_name, 'to_alipay_dict'):
                params['school_en_name'] = self.school_en_name.to_alipay_dict()
            else:
                params['school_en_name'] = self.school_en_name
        if self.school_icon:
            if hasattr(self.school_icon, 'to_alipay_dict'):
                params['school_icon'] = self.school_icon.to_alipay_dict()
            else:
                params['school_icon'] = self.school_icon
        if self.school_icon_type:
            if hasattr(self.school_icon_type, 'to_alipay_dict'):
                params['school_icon_type'] = self.school_icon_type.to_alipay_dict()
            else:
                params['school_icon_type'] = self.school_icon_type
        if self.school_mcc:
            if hasattr(self.school_mcc, 'to_alipay_dict'):
                params['school_mcc'] = self.school_mcc.to_alipay_dict()
            else:
                params['school_mcc'] = self.school_mcc
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.school_stdcode:
            if hasattr(self.school_stdcode, 'to_alipay_dict'):
                params['school_stdcode'] = self.school_stdcode.to_alipay_dict()
            else:
                params['school_stdcode'] = self.school_stdcode
        if self.school_type:
            if hasattr(self.school_type, 'to_alipay_dict'):
                params['school_type'] = self.school_type.to_alipay_dict()
            else:
                params['school_type'] = self.school_type
        if self.school_zipcode:
            if hasattr(self.school_zipcode, 'to_alipay_dict'):
                params['school_zipcode'] = self.school_zipcode.to_alipay_dict()
            else:
                params['school_zipcode'] = self.school_zipcode
        if self.special_economic_zone_company_type:
            if hasattr(self.special_economic_zone_company_type, 'to_alipay_dict'):
                params['special_economic_zone_company_type'] = self.special_economic_zone_company_type.to_alipay_dict()
            else:
                params['special_economic_zone_company_type'] = self.special_economic_zone_company_type
        if self.trans_email:
            if hasattr(self.trans_email, 'to_alipay_dict'):
                params['trans_email'] = self.trans_email.to_alipay_dict()
            else:
                params['trans_email'] = self.trans_email
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasFundInstitutionschoolinfCreateModel()
        if 'attr_code' in d:
            o.attr_code = d['attr_code']
        if 'bussess_adr' in d:
            o.bussess_adr = d['bussess_adr']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'cust_type' in d:
            o.cust_type = d['cust_type']
        if 'declare_type' in d:
            o.declare_type = d['declare_type']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'economy_type_code' in d:
            o.economy_type_code = d['economy_type_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'investment_country_code_one' in d:
            o.investment_country_code_one = d['investment_country_code_one']
        if 'is_special_economic_zone' in d:
            o.is_special_economic_zone = d['is_special_economic_zone']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_phone' in d:
            o.isv_phone = d['isv_phone']
        if 'isv_request_no' in d:
            o.isv_request_no = d['isv_request_no']
        if 'link_man_name' in d:
            o.link_man_name = d['link_man_name']
        if 'link_phone' in d:
            o.link_phone = d['link_phone']
        if 'office_adr_en' in d:
            o.office_adr_en = d['office_adr_en']
        if 'org_name_en' in d:
            o.org_name_en = d['org_name_en']
        if 'org_type' in d:
            o.org_type = d['org_type']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'remark_info' in d:
            o.remark_info = d['remark_info']
        if 'school_address' in d:
            o.school_address = d['school_address']
        if 'school_country' in d:
            o.school_country = d['school_country']
        if 'school_en_name' in d:
            o.school_en_name = d['school_en_name']
        if 'school_icon' in d:
            o.school_icon = d['school_icon']
        if 'school_icon_type' in d:
            o.school_icon_type = d['school_icon_type']
        if 'school_mcc' in d:
            o.school_mcc = d['school_mcc']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        if 'school_type' in d:
            o.school_type = d['school_type']
        if 'school_zipcode' in d:
            o.school_zipcode = d['school_zipcode']
        if 'special_economic_zone_company_type' in d:
            o.special_economic_zone_company_type = d['special_economic_zone_company_type']
        if 'trans_email' in d:
            o.trans_email = d['trans_email']
        return o


