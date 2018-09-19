#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.BankCardInfo import BankCardInfo
from alipay.aop.api.domain.ContactInfo import ContactInfo
from alipay.aop.api.domain.SiteInfo import SiteInfo


class AntMerchantExpandIndirectOnlineModifyModel(object):

    def __init__(self):
        self._address_info = None
        self._alias_name = None
        self._bank_pid = None
        self._bankcard_info = None
        self._business_license = None
        self._business_license_type = None
        self._contact_info = None
        self._isv_pid = None
        self._logon_id = None
        self._mcc = None
        self._memo = None
        self._name = None
        self._pay_code_info = None
        self._service_phone = None
        self._sign_bank_time = None
        self._site_info = None
        self._sub_merchant_id = None
        self._unique_id_by_bank = None
        self._unique_id_by_isv = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, list):
            self._address_info = list()
            for i in value:
                if isinstance(i, AddressInfo):
                    self._address_info.append(i)
                else:
                    self._address_info.append(AddressInfo.from_alipay_dict(i))
    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def bank_pid(self):
        return self._bank_pid

    @bank_pid.setter
    def bank_pid(self, value):
        self._bank_pid = value
    @property
    def bankcard_info(self):
        return self._bankcard_info

    @bankcard_info.setter
    def bankcard_info(self, value):
        if isinstance(value, list):
            self._bankcard_info = list()
            for i in value:
                if isinstance(i, BankCardInfo):
                    self._bankcard_info.append(i)
                else:
                    self._bankcard_info.append(BankCardInfo.from_alipay_dict(i))
    @property
    def business_license(self):
        return self._business_license

    @business_license.setter
    def business_license(self, value):
        self._business_license = value
    @property
    def business_license_type(self):
        return self._business_license_type

    @business_license_type.setter
    def business_license_type(self, value):
        self._business_license_type = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, list):
            self._contact_info = list()
            for i in value:
                if isinstance(i, ContactInfo):
                    self._contact_info.append(i)
                else:
                    self._contact_info.append(ContactInfo.from_alipay_dict(i))
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        if isinstance(value, list):
            self._logon_id = list()
            for i in value:
                self._logon_id.append(i)
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pay_code_info(self):
        return self._pay_code_info

    @pay_code_info.setter
    def pay_code_info(self, value):
        if isinstance(value, list):
            self._pay_code_info = list()
            for i in value:
                self._pay_code_info.append(i)
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def sign_bank_time(self):
        return self._sign_bank_time

    @sign_bank_time.setter
    def sign_bank_time(self, value):
        self._sign_bank_time = value
    @property
    def site_info(self):
        return self._site_info

    @site_info.setter
    def site_info(self, value):
        if isinstance(value, list):
            self._site_info = list()
            for i in value:
                if isinstance(i, SiteInfo):
                    self._site_info.append(i)
                else:
                    self._site_info.append(SiteInfo.from_alipay_dict(i))
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def unique_id_by_bank(self):
        return self._unique_id_by_bank

    @unique_id_by_bank.setter
    def unique_id_by_bank(self, value):
        self._unique_id_by_bank = value
    @property
    def unique_id_by_isv(self):
        return self._unique_id_by_isv

    @unique_id_by_isv.setter
    def unique_id_by_isv(self, value):
        self._unique_id_by_isv = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if isinstance(self.address_info, list):
                for i in range(0, len(self.address_info)):
                    element = self.address_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.address_info[i] = element.to_alipay_dict()
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.bank_pid:
            if hasattr(self.bank_pid, 'to_alipay_dict'):
                params['bank_pid'] = self.bank_pid.to_alipay_dict()
            else:
                params['bank_pid'] = self.bank_pid
        if self.bankcard_info:
            if isinstance(self.bankcard_info, list):
                for i in range(0, len(self.bankcard_info)):
                    element = self.bankcard_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bankcard_info[i] = element.to_alipay_dict()
            if hasattr(self.bankcard_info, 'to_alipay_dict'):
                params['bankcard_info'] = self.bankcard_info.to_alipay_dict()
            else:
                params['bankcard_info'] = self.bankcard_info
        if self.business_license:
            if hasattr(self.business_license, 'to_alipay_dict'):
                params['business_license'] = self.business_license.to_alipay_dict()
            else:
                params['business_license'] = self.business_license
        if self.business_license_type:
            if hasattr(self.business_license_type, 'to_alipay_dict'):
                params['business_license_type'] = self.business_license_type.to_alipay_dict()
            else:
                params['business_license_type'] = self.business_license_type
        if self.contact_info:
            if isinstance(self.contact_info, list):
                for i in range(0, len(self.contact_info)):
                    element = self.contact_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_info[i] = element.to_alipay_dict()
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.logon_id:
            if isinstance(self.logon_id, list):
                for i in range(0, len(self.logon_id)):
                    element = self.logon_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logon_id[i] = element.to_alipay_dict()
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pay_code_info:
            if isinstance(self.pay_code_info, list):
                for i in range(0, len(self.pay_code_info)):
                    element = self.pay_code_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_code_info[i] = element.to_alipay_dict()
            if hasattr(self.pay_code_info, 'to_alipay_dict'):
                params['pay_code_info'] = self.pay_code_info.to_alipay_dict()
            else:
                params['pay_code_info'] = self.pay_code_info
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        if self.sign_bank_time:
            if hasattr(self.sign_bank_time, 'to_alipay_dict'):
                params['sign_bank_time'] = self.sign_bank_time.to_alipay_dict()
            else:
                params['sign_bank_time'] = self.sign_bank_time
        if self.site_info:
            if isinstance(self.site_info, list):
                for i in range(0, len(self.site_info)):
                    element = self.site_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.site_info[i] = element.to_alipay_dict()
            if hasattr(self.site_info, 'to_alipay_dict'):
                params['site_info'] = self.site_info.to_alipay_dict()
            else:
                params['site_info'] = self.site_info
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.unique_id_by_bank:
            if hasattr(self.unique_id_by_bank, 'to_alipay_dict'):
                params['unique_id_by_bank'] = self.unique_id_by_bank.to_alipay_dict()
            else:
                params['unique_id_by_bank'] = self.unique_id_by_bank
        if self.unique_id_by_isv:
            if hasattr(self.unique_id_by_isv, 'to_alipay_dict'):
                params['unique_id_by_isv'] = self.unique_id_by_isv.to_alipay_dict()
            else:
                params['unique_id_by_isv'] = self.unique_id_by_isv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectOnlineModifyModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'bank_pid' in d:
            o.bank_pid = d['bank_pid']
        if 'bankcard_info' in d:
            o.bankcard_info = d['bankcard_info']
        if 'business_license' in d:
            o.business_license = d['business_license']
        if 'business_license_type' in d:
            o.business_license_type = d['business_license_type']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'pay_code_info' in d:
            o.pay_code_info = d['pay_code_info']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'sign_bank_time' in d:
            o.sign_bank_time = d['sign_bank_time']
        if 'site_info' in d:
            o.site_info = d['site_info']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'unique_id_by_bank' in d:
            o.unique_id_by_bank = d['unique_id_by_bank']
        if 'unique_id_by_isv' in d:
            o.unique_id_by_isv = d['unique_id_by_isv']
        return o


