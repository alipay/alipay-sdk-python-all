#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.BankCardInfo import BankCardInfo
from alipay.aop.api.domain.ContactInfo import ContactInfo
from alipay.aop.api.domain.SiteInfo import SiteInfo


class AntMerchantExpandIndirectOnlineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectOnlineQueryResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectOnlineQueryResponse, self).parse_response_content(response_content)
        if 'address_info' in response:
            self.address_info = response['address_info']
        if 'alias_name' in response:
            self.alias_name = response['alias_name']
        if 'bank_pid' in response:
            self.bank_pid = response['bank_pid']
        if 'bankcard_info' in response:
            self.bankcard_info = response['bankcard_info']
        if 'business_license' in response:
            self.business_license = response['business_license']
        if 'business_license_type' in response:
            self.business_license_type = response['business_license_type']
        if 'contact_info' in response:
            self.contact_info = response['contact_info']
        if 'isv_pid' in response:
            self.isv_pid = response['isv_pid']
        if 'logon_id' in response:
            self.logon_id = response['logon_id']
        if 'mcc' in response:
            self.mcc = response['mcc']
        if 'memo' in response:
            self.memo = response['memo']
        if 'name' in response:
            self.name = response['name']
        if 'pay_code_info' in response:
            self.pay_code_info = response['pay_code_info']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
        if 'sign_bank_time' in response:
            self.sign_bank_time = response['sign_bank_time']
        if 'site_info' in response:
            self.site_info = response['site_info']
        if 'unique_id_by_bank' in response:
            self.unique_id_by_bank = response['unique_id_by_bank']
        if 'unique_id_by_isv' in response:
            self.unique_id_by_isv = response['unique_id_by_isv']
