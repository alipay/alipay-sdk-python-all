#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpIndustryModel import EpIndustryModel
from alipay.aop.api.domain.EpStockInfo import EpStockInfo


class EpBusinessBasicInfo(object):

    def __init__(self):
        self._address = None
        self._ajnsrpjnd = None
        self._approval_date = None
        self._build_date = None
        self._business_period_from = None
        self._business_period_to = None
        self._cancellation_date = None
        self._chief_representative = None
        self._email = None
        self._frdb = None
        self._industry_model = None
        self._investors = None
        self._jycs = None
        self._legal_representative = None
        self._legal_representative_or_pe = None
        self._manager_scope = None
        self._name = None
        self._old_name = None
        self._operator = None
        self._phone = None
        self._principal = None
        self._province_or_city = None
        self._qrdgsj = None
        self._registe_organ = None
        self._register_status = None
        self._registr_id = None
        self._registration_capital = None
        self._revocation_date = None
        self._sanitized_name = None
        self._sent_company_name = None
        self._standardized_name = None
        self._stock = None
        self._type = None
        self._type_code = None
        self._tyshxydm = None
        self._zczbbz = None
        self._zxhhr = None
        self._zxswhhr = None
        self._zxswhhrwpdb = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def ajnsrpjnd(self):
        return self._ajnsrpjnd

    @ajnsrpjnd.setter
    def ajnsrpjnd(self, value):
        if isinstance(value, list):
            self._ajnsrpjnd = list()
            for i in value:
                self._ajnsrpjnd.append(i)
    @property
    def approval_date(self):
        return self._approval_date

    @approval_date.setter
    def approval_date(self, value):
        self._approval_date = value
    @property
    def build_date(self):
        return self._build_date

    @build_date.setter
    def build_date(self, value):
        self._build_date = value
    @property
    def business_period_from(self):
        return self._business_period_from

    @business_period_from.setter
    def business_period_from(self, value):
        self._business_period_from = value
    @property
    def business_period_to(self):
        return self._business_period_to

    @business_period_to.setter
    def business_period_to(self, value):
        self._business_period_to = value
    @property
    def cancellation_date(self):
        return self._cancellation_date

    @cancellation_date.setter
    def cancellation_date(self, value):
        self._cancellation_date = value
    @property
    def chief_representative(self):
        return self._chief_representative

    @chief_representative.setter
    def chief_representative(self, value):
        self._chief_representative = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def frdb(self):
        return self._frdb

    @frdb.setter
    def frdb(self, value):
        self._frdb = value
    @property
    def industry_model(self):
        return self._industry_model

    @industry_model.setter
    def industry_model(self, value):
        if isinstance(value, EpIndustryModel):
            self._industry_model = value
        else:
            self._industry_model = EpIndustryModel.from_alipay_dict(value)
    @property
    def investors(self):
        return self._investors

    @investors.setter
    def investors(self, value):
        self._investors = value
    @property
    def jycs(self):
        return self._jycs

    @jycs.setter
    def jycs(self, value):
        self._jycs = value
    @property
    def legal_representative(self):
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, value):
        self._legal_representative = value
    @property
    def legal_representative_or_pe(self):
        return self._legal_representative_or_pe

    @legal_representative_or_pe.setter
    def legal_representative_or_pe(self, value):
        self._legal_representative_or_pe = value
    @property
    def manager_scope(self):
        return self._manager_scope

    @manager_scope.setter
    def manager_scope(self, value):
        self._manager_scope = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def old_name(self):
        return self._old_name

    @old_name.setter
    def old_name(self, value):
        self._old_name = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def province_or_city(self):
        return self._province_or_city

    @province_or_city.setter
    def province_or_city(self, value):
        self._province_or_city = value
    @property
    def qrdgsj(self):
        return self._qrdgsj

    @qrdgsj.setter
    def qrdgsj(self, value):
        self._qrdgsj = value
    @property
    def registe_organ(self):
        return self._registe_organ

    @registe_organ.setter
    def registe_organ(self, value):
        self._registe_organ = value
    @property
    def register_status(self):
        return self._register_status

    @register_status.setter
    def register_status(self, value):
        self._register_status = value
    @property
    def registr_id(self):
        return self._registr_id

    @registr_id.setter
    def registr_id(self, value):
        self._registr_id = value
    @property
    def registration_capital(self):
        return self._registration_capital

    @registration_capital.setter
    def registration_capital(self, value):
        self._registration_capital = value
    @property
    def revocation_date(self):
        return self._revocation_date

    @revocation_date.setter
    def revocation_date(self, value):
        self._revocation_date = value
    @property
    def sanitized_name(self):
        return self._sanitized_name

    @sanitized_name.setter
    def sanitized_name(self, value):
        self._sanitized_name = value
    @property
    def sent_company_name(self):
        return self._sent_company_name

    @sent_company_name.setter
    def sent_company_name(self, value):
        self._sent_company_name = value
    @property
    def standardized_name(self):
        return self._standardized_name

    @standardized_name.setter
    def standardized_name(self, value):
        self._standardized_name = value
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if isinstance(value, list):
            self._stock = list()
            for i in value:
                if isinstance(i, EpStockInfo):
                    self._stock.append(i)
                else:
                    self._stock.append(EpStockInfo.from_alipay_dict(i))
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def type_code(self):
        return self._type_code

    @type_code.setter
    def type_code(self, value):
        self._type_code = value
    @property
    def tyshxydm(self):
        return self._tyshxydm

    @tyshxydm.setter
    def tyshxydm(self, value):
        self._tyshxydm = value
    @property
    def zczbbz(self):
        return self._zczbbz

    @zczbbz.setter
    def zczbbz(self, value):
        self._zczbbz = value
    @property
    def zxhhr(self):
        return self._zxhhr

    @zxhhr.setter
    def zxhhr(self, value):
        self._zxhhr = value
    @property
    def zxswhhr(self):
        return self._zxswhhr

    @zxswhhr.setter
    def zxswhhr(self, value):
        self._zxswhhr = value
    @property
    def zxswhhrwpdb(self):
        return self._zxswhhrwpdb

    @zxswhhrwpdb.setter
    def zxswhhrwpdb(self, value):
        self._zxswhhrwpdb = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.ajnsrpjnd:
            if isinstance(self.ajnsrpjnd, list):
                for i in range(0, len(self.ajnsrpjnd)):
                    element = self.ajnsrpjnd[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ajnsrpjnd[i] = element.to_alipay_dict()
            if hasattr(self.ajnsrpjnd, 'to_alipay_dict'):
                params['ajnsrpjnd'] = self.ajnsrpjnd.to_alipay_dict()
            else:
                params['ajnsrpjnd'] = self.ajnsrpjnd
        if self.approval_date:
            if hasattr(self.approval_date, 'to_alipay_dict'):
                params['approval_date'] = self.approval_date.to_alipay_dict()
            else:
                params['approval_date'] = self.approval_date
        if self.build_date:
            if hasattr(self.build_date, 'to_alipay_dict'):
                params['build_date'] = self.build_date.to_alipay_dict()
            else:
                params['build_date'] = self.build_date
        if self.business_period_from:
            if hasattr(self.business_period_from, 'to_alipay_dict'):
                params['business_period_from'] = self.business_period_from.to_alipay_dict()
            else:
                params['business_period_from'] = self.business_period_from
        if self.business_period_to:
            if hasattr(self.business_period_to, 'to_alipay_dict'):
                params['business_period_to'] = self.business_period_to.to_alipay_dict()
            else:
                params['business_period_to'] = self.business_period_to
        if self.cancellation_date:
            if hasattr(self.cancellation_date, 'to_alipay_dict'):
                params['cancellation_date'] = self.cancellation_date.to_alipay_dict()
            else:
                params['cancellation_date'] = self.cancellation_date
        if self.chief_representative:
            if hasattr(self.chief_representative, 'to_alipay_dict'):
                params['chief_representative'] = self.chief_representative.to_alipay_dict()
            else:
                params['chief_representative'] = self.chief_representative
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.frdb:
            if hasattr(self.frdb, 'to_alipay_dict'):
                params['frdb'] = self.frdb.to_alipay_dict()
            else:
                params['frdb'] = self.frdb
        if self.industry_model:
            if hasattr(self.industry_model, 'to_alipay_dict'):
                params['industry_model'] = self.industry_model.to_alipay_dict()
            else:
                params['industry_model'] = self.industry_model
        if self.investors:
            if hasattr(self.investors, 'to_alipay_dict'):
                params['investors'] = self.investors.to_alipay_dict()
            else:
                params['investors'] = self.investors
        if self.jycs:
            if hasattr(self.jycs, 'to_alipay_dict'):
                params['jycs'] = self.jycs.to_alipay_dict()
            else:
                params['jycs'] = self.jycs
        if self.legal_representative:
            if hasattr(self.legal_representative, 'to_alipay_dict'):
                params['legal_representative'] = self.legal_representative.to_alipay_dict()
            else:
                params['legal_representative'] = self.legal_representative
        if self.legal_representative_or_pe:
            if hasattr(self.legal_representative_or_pe, 'to_alipay_dict'):
                params['legal_representative_or_pe'] = self.legal_representative_or_pe.to_alipay_dict()
            else:
                params['legal_representative_or_pe'] = self.legal_representative_or_pe
        if self.manager_scope:
            if hasattr(self.manager_scope, 'to_alipay_dict'):
                params['manager_scope'] = self.manager_scope.to_alipay_dict()
            else:
                params['manager_scope'] = self.manager_scope
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.old_name:
            if hasattr(self.old_name, 'to_alipay_dict'):
                params['old_name'] = self.old_name.to_alipay_dict()
            else:
                params['old_name'] = self.old_name
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.province_or_city:
            if hasattr(self.province_or_city, 'to_alipay_dict'):
                params['province_or_city'] = self.province_or_city.to_alipay_dict()
            else:
                params['province_or_city'] = self.province_or_city
        if self.qrdgsj:
            if hasattr(self.qrdgsj, 'to_alipay_dict'):
                params['qrdgsj'] = self.qrdgsj.to_alipay_dict()
            else:
                params['qrdgsj'] = self.qrdgsj
        if self.registe_organ:
            if hasattr(self.registe_organ, 'to_alipay_dict'):
                params['registe_organ'] = self.registe_organ.to_alipay_dict()
            else:
                params['registe_organ'] = self.registe_organ
        if self.register_status:
            if hasattr(self.register_status, 'to_alipay_dict'):
                params['register_status'] = self.register_status.to_alipay_dict()
            else:
                params['register_status'] = self.register_status
        if self.registr_id:
            if hasattr(self.registr_id, 'to_alipay_dict'):
                params['registr_id'] = self.registr_id.to_alipay_dict()
            else:
                params['registr_id'] = self.registr_id
        if self.registration_capital:
            if hasattr(self.registration_capital, 'to_alipay_dict'):
                params['registration_capital'] = self.registration_capital.to_alipay_dict()
            else:
                params['registration_capital'] = self.registration_capital
        if self.revocation_date:
            if hasattr(self.revocation_date, 'to_alipay_dict'):
                params['revocation_date'] = self.revocation_date.to_alipay_dict()
            else:
                params['revocation_date'] = self.revocation_date
        if self.sanitized_name:
            if hasattr(self.sanitized_name, 'to_alipay_dict'):
                params['sanitized_name'] = self.sanitized_name.to_alipay_dict()
            else:
                params['sanitized_name'] = self.sanitized_name
        if self.sent_company_name:
            if hasattr(self.sent_company_name, 'to_alipay_dict'):
                params['sent_company_name'] = self.sent_company_name.to_alipay_dict()
            else:
                params['sent_company_name'] = self.sent_company_name
        if self.standardized_name:
            if hasattr(self.standardized_name, 'to_alipay_dict'):
                params['standardized_name'] = self.standardized_name.to_alipay_dict()
            else:
                params['standardized_name'] = self.standardized_name
        if self.stock:
            if isinstance(self.stock, list):
                for i in range(0, len(self.stock)):
                    element = self.stock[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stock[i] = element.to_alipay_dict()
            if hasattr(self.stock, 'to_alipay_dict'):
                params['stock'] = self.stock.to_alipay_dict()
            else:
                params['stock'] = self.stock
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.type_code:
            if hasattr(self.type_code, 'to_alipay_dict'):
                params['type_code'] = self.type_code.to_alipay_dict()
            else:
                params['type_code'] = self.type_code
        if self.tyshxydm:
            if hasattr(self.tyshxydm, 'to_alipay_dict'):
                params['tyshxydm'] = self.tyshxydm.to_alipay_dict()
            else:
                params['tyshxydm'] = self.tyshxydm
        if self.zczbbz:
            if hasattr(self.zczbbz, 'to_alipay_dict'):
                params['zczbbz'] = self.zczbbz.to_alipay_dict()
            else:
                params['zczbbz'] = self.zczbbz
        if self.zxhhr:
            if hasattr(self.zxhhr, 'to_alipay_dict'):
                params['zxhhr'] = self.zxhhr.to_alipay_dict()
            else:
                params['zxhhr'] = self.zxhhr
        if self.zxswhhr:
            if hasattr(self.zxswhhr, 'to_alipay_dict'):
                params['zxswhhr'] = self.zxswhhr.to_alipay_dict()
            else:
                params['zxswhhr'] = self.zxswhhr
        if self.zxswhhrwpdb:
            if hasattr(self.zxswhhrwpdb, 'to_alipay_dict'):
                params['zxswhhrwpdb'] = self.zxswhhrwpdb.to_alipay_dict()
            else:
                params['zxswhhrwpdb'] = self.zxswhhrwpdb
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpBusinessBasicInfo()
        if 'address' in d:
            o.address = d['address']
        if 'ajnsrpjnd' in d:
            o.ajnsrpjnd = d['ajnsrpjnd']
        if 'approval_date' in d:
            o.approval_date = d['approval_date']
        if 'build_date' in d:
            o.build_date = d['build_date']
        if 'business_period_from' in d:
            o.business_period_from = d['business_period_from']
        if 'business_period_to' in d:
            o.business_period_to = d['business_period_to']
        if 'cancellation_date' in d:
            o.cancellation_date = d['cancellation_date']
        if 'chief_representative' in d:
            o.chief_representative = d['chief_representative']
        if 'email' in d:
            o.email = d['email']
        if 'frdb' in d:
            o.frdb = d['frdb']
        if 'industry_model' in d:
            o.industry_model = d['industry_model']
        if 'investors' in d:
            o.investors = d['investors']
        if 'jycs' in d:
            o.jycs = d['jycs']
        if 'legal_representative' in d:
            o.legal_representative = d['legal_representative']
        if 'legal_representative_or_pe' in d:
            o.legal_representative_or_pe = d['legal_representative_or_pe']
        if 'manager_scope' in d:
            o.manager_scope = d['manager_scope']
        if 'name' in d:
            o.name = d['name']
        if 'old_name' in d:
            o.old_name = d['old_name']
        if 'operator' in d:
            o.operator = d['operator']
        if 'phone' in d:
            o.phone = d['phone']
        if 'principal' in d:
            o.principal = d['principal']
        if 'province_or_city' in d:
            o.province_or_city = d['province_or_city']
        if 'qrdgsj' in d:
            o.qrdgsj = d['qrdgsj']
        if 'registe_organ' in d:
            o.registe_organ = d['registe_organ']
        if 'register_status' in d:
            o.register_status = d['register_status']
        if 'registr_id' in d:
            o.registr_id = d['registr_id']
        if 'registration_capital' in d:
            o.registration_capital = d['registration_capital']
        if 'revocation_date' in d:
            o.revocation_date = d['revocation_date']
        if 'sanitized_name' in d:
            o.sanitized_name = d['sanitized_name']
        if 'sent_company_name' in d:
            o.sent_company_name = d['sent_company_name']
        if 'standardized_name' in d:
            o.standardized_name = d['standardized_name']
        if 'stock' in d:
            o.stock = d['stock']
        if 'type' in d:
            o.type = d['type']
        if 'type_code' in d:
            o.type_code = d['type_code']
        if 'tyshxydm' in d:
            o.tyshxydm = d['tyshxydm']
        if 'zczbbz' in d:
            o.zczbbz = d['zczbbz']
        if 'zxhhr' in d:
            o.zxhhr = d['zxhhr']
        if 'zxswhhr' in d:
            o.zxswhhr = d['zxswhhr']
        if 'zxswhhrwpdb' in d:
            o.zxswhhrwpdb = d['zxswhhrwpdb']
        return o


