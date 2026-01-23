#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class IitBizDetailBillDetailOpenApiDTO(object):

    def __init__(self):
        self._actual_amount = None
        self._bill_amt = None
        self._birthday = None
        self._biz_id = None
        self._biz_scene_code = None
        self._city_main_const_tax_amount = None
        self._contact = None
        self._country = None
        self._disability_cert_no = None
        self._edu_surcharge_amount = None
        self._gender = None
        self._id = None
        self._idempotent_id = None
        self._iit_amount = None
        self._iit_project = None
        self._inst_id = None
        self._local_edu_surcharge_amount = None
        self._period = None
        self._tax_base_type = None
        self._taxpayer_cert_no = None
        self._taxpayer_cert_type = None
        self._taxpayer_name = None
        self._total_tax_amount = None
        self._user_is_disability = None
        self._vat_amount = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._actual_amount = value
        else:
            self._actual_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def bill_amt(self):
        return self._bill_amt

    @bill_amt.setter
    def bill_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._bill_amt = value
        else:
            self._bill_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_scene_code(self):
        return self._biz_scene_code

    @biz_scene_code.setter
    def biz_scene_code(self, value):
        self._biz_scene_code = value
    @property
    def city_main_const_tax_amount(self):
        return self._city_main_const_tax_amount

    @city_main_const_tax_amount.setter
    def city_main_const_tax_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._city_main_const_tax_amount = value
        else:
            self._city_main_const_tax_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def disability_cert_no(self):
        return self._disability_cert_no

    @disability_cert_no.setter
    def disability_cert_no(self, value):
        self._disability_cert_no = value
    @property
    def edu_surcharge_amount(self):
        return self._edu_surcharge_amount

    @edu_surcharge_amount.setter
    def edu_surcharge_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._edu_surcharge_amount = value
        else:
            self._edu_surcharge_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def idempotent_id(self):
        return self._idempotent_id

    @idempotent_id.setter
    def idempotent_id(self, value):
        self._idempotent_id = value
    @property
    def iit_amount(self):
        return self._iit_amount

    @iit_amount.setter
    def iit_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._iit_amount = value
        else:
            self._iit_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def iit_project(self):
        return self._iit_project

    @iit_project.setter
    def iit_project(self, value):
        self._iit_project = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def local_edu_surcharge_amount(self):
        return self._local_edu_surcharge_amount

    @local_edu_surcharge_amount.setter
    def local_edu_surcharge_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._local_edu_surcharge_amount = value
        else:
            self._local_edu_surcharge_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def tax_base_type(self):
        return self._tax_base_type

    @tax_base_type.setter
    def tax_base_type(self, value):
        self._tax_base_type = value
    @property
    def taxpayer_cert_no(self):
        return self._taxpayer_cert_no

    @taxpayer_cert_no.setter
    def taxpayer_cert_no(self, value):
        self._taxpayer_cert_no = value
    @property
    def taxpayer_cert_type(self):
        return self._taxpayer_cert_type

    @taxpayer_cert_type.setter
    def taxpayer_cert_type(self, value):
        self._taxpayer_cert_type = value
    @property
    def taxpayer_name(self):
        return self._taxpayer_name

    @taxpayer_name.setter
    def taxpayer_name(self, value):
        self._taxpayer_name = value
    @property
    def total_tax_amount(self):
        return self._total_tax_amount

    @total_tax_amount.setter
    def total_tax_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_tax_amount = value
        else:
            self._total_tax_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def user_is_disability(self):
        return self._user_is_disability

    @user_is_disability.setter
    def user_is_disability(self, value):
        self._user_is_disability = value
    @property
    def vat_amount(self):
        return self._vat_amount

    @vat_amount.setter
    def vat_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._vat_amount = value
        else:
            self._vat_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.bill_amt:
            if hasattr(self.bill_amt, 'to_alipay_dict'):
                params['bill_amt'] = self.bill_amt.to_alipay_dict()
            else:
                params['bill_amt'] = self.bill_amt
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_scene_code:
            if hasattr(self.biz_scene_code, 'to_alipay_dict'):
                params['biz_scene_code'] = self.biz_scene_code.to_alipay_dict()
            else:
                params['biz_scene_code'] = self.biz_scene_code
        if self.city_main_const_tax_amount:
            if hasattr(self.city_main_const_tax_amount, 'to_alipay_dict'):
                params['city_main_const_tax_amount'] = self.city_main_const_tax_amount.to_alipay_dict()
            else:
                params['city_main_const_tax_amount'] = self.city_main_const_tax_amount
        if self.contact:
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.disability_cert_no:
            if hasattr(self.disability_cert_no, 'to_alipay_dict'):
                params['disability_cert_no'] = self.disability_cert_no.to_alipay_dict()
            else:
                params['disability_cert_no'] = self.disability_cert_no
        if self.edu_surcharge_amount:
            if hasattr(self.edu_surcharge_amount, 'to_alipay_dict'):
                params['edu_surcharge_amount'] = self.edu_surcharge_amount.to_alipay_dict()
            else:
                params['edu_surcharge_amount'] = self.edu_surcharge_amount
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.idempotent_id:
            if hasattr(self.idempotent_id, 'to_alipay_dict'):
                params['idempotent_id'] = self.idempotent_id.to_alipay_dict()
            else:
                params['idempotent_id'] = self.idempotent_id
        if self.iit_amount:
            if hasattr(self.iit_amount, 'to_alipay_dict'):
                params['iit_amount'] = self.iit_amount.to_alipay_dict()
            else:
                params['iit_amount'] = self.iit_amount
        if self.iit_project:
            if hasattr(self.iit_project, 'to_alipay_dict'):
                params['iit_project'] = self.iit_project.to_alipay_dict()
            else:
                params['iit_project'] = self.iit_project
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.local_edu_surcharge_amount:
            if hasattr(self.local_edu_surcharge_amount, 'to_alipay_dict'):
                params['local_edu_surcharge_amount'] = self.local_edu_surcharge_amount.to_alipay_dict()
            else:
                params['local_edu_surcharge_amount'] = self.local_edu_surcharge_amount
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.tax_base_type:
            if hasattr(self.tax_base_type, 'to_alipay_dict'):
                params['tax_base_type'] = self.tax_base_type.to_alipay_dict()
            else:
                params['tax_base_type'] = self.tax_base_type
        if self.taxpayer_cert_no:
            if hasattr(self.taxpayer_cert_no, 'to_alipay_dict'):
                params['taxpayer_cert_no'] = self.taxpayer_cert_no.to_alipay_dict()
            else:
                params['taxpayer_cert_no'] = self.taxpayer_cert_no
        if self.taxpayer_cert_type:
            if hasattr(self.taxpayer_cert_type, 'to_alipay_dict'):
                params['taxpayer_cert_type'] = self.taxpayer_cert_type.to_alipay_dict()
            else:
                params['taxpayer_cert_type'] = self.taxpayer_cert_type
        if self.taxpayer_name:
            if hasattr(self.taxpayer_name, 'to_alipay_dict'):
                params['taxpayer_name'] = self.taxpayer_name.to_alipay_dict()
            else:
                params['taxpayer_name'] = self.taxpayer_name
        if self.total_tax_amount:
            if hasattr(self.total_tax_amount, 'to_alipay_dict'):
                params['total_tax_amount'] = self.total_tax_amount.to_alipay_dict()
            else:
                params['total_tax_amount'] = self.total_tax_amount
        if self.user_is_disability:
            if hasattr(self.user_is_disability, 'to_alipay_dict'):
                params['user_is_disability'] = self.user_is_disability.to_alipay_dict()
            else:
                params['user_is_disability'] = self.user_is_disability
        if self.vat_amount:
            if hasattr(self.vat_amount, 'to_alipay_dict'):
                params['vat_amount'] = self.vat_amount.to_alipay_dict()
            else:
                params['vat_amount'] = self.vat_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IitBizDetailBillDetailOpenApiDTO()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'bill_amt' in d:
            o.bill_amt = d['bill_amt']
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_scene_code' in d:
            o.biz_scene_code = d['biz_scene_code']
        if 'city_main_const_tax_amount' in d:
            o.city_main_const_tax_amount = d['city_main_const_tax_amount']
        if 'contact' in d:
            o.contact = d['contact']
        if 'country' in d:
            o.country = d['country']
        if 'disability_cert_no' in d:
            o.disability_cert_no = d['disability_cert_no']
        if 'edu_surcharge_amount' in d:
            o.edu_surcharge_amount = d['edu_surcharge_amount']
        if 'gender' in d:
            o.gender = d['gender']
        if 'id' in d:
            o.id = d['id']
        if 'idempotent_id' in d:
            o.idempotent_id = d['idempotent_id']
        if 'iit_amount' in d:
            o.iit_amount = d['iit_amount']
        if 'iit_project' in d:
            o.iit_project = d['iit_project']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'local_edu_surcharge_amount' in d:
            o.local_edu_surcharge_amount = d['local_edu_surcharge_amount']
        if 'period' in d:
            o.period = d['period']
        if 'tax_base_type' in d:
            o.tax_base_type = d['tax_base_type']
        if 'taxpayer_cert_no' in d:
            o.taxpayer_cert_no = d['taxpayer_cert_no']
        if 'taxpayer_cert_type' in d:
            o.taxpayer_cert_type = d['taxpayer_cert_type']
        if 'taxpayer_name' in d:
            o.taxpayer_name = d['taxpayer_name']
        if 'total_tax_amount' in d:
            o.total_tax_amount = d['total_tax_amount']
        if 'user_is_disability' in d:
            o.user_is_disability = d['user_is_disability']
        if 'vat_amount' in d:
            o.vat_amount = d['vat_amount']
        return o


