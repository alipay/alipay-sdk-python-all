#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.BankCardInfo import BankCardInfo
from alipay.aop.api.domain.ContactInfo import ContactInfo
from alipay.aop.api.domain.SiteInfo import SiteInfo


class AntMerchantExpandIndirectModifyModel(object):

    def __init__(self):
        self._address_info = None
        self._alias_name = None
        self._bankcard_info = None
        self._business_license = None
        self._business_license_type = None
        self._category_id = None
        self._contact_info = None
        self._external_id = None
        self._logon_id = None
        self._mcc = None
        self._memo = None
        self._name = None
        self._org_pid = None
        self._pay_code_info = None
        self._service_codes = None
        self._service_phone = None
        self._site_info = None
        self._source = None
        self._sub_merchant_id = None

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
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
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
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
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
    def org_pid(self):
        return self._org_pid

    @org_pid.setter
    def org_pid(self, value):
        self._org_pid = value
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
    def service_codes(self):
        return self._service_codes

    @service_codes.setter
    def service_codes(self, value):
        if isinstance(value, list):
            self._service_codes = list()
            for i in value:
                self._service_codes.append(i)
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
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
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


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
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
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
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
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
        if self.org_pid:
            if hasattr(self.org_pid, 'to_alipay_dict'):
                params['org_pid'] = self.org_pid.to_alipay_dict()
            else:
                params['org_pid'] = self.org_pid
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
        if self.service_codes:
            if isinstance(self.service_codes, list):
                for i in range(0, len(self.service_codes)):
                    element = self.service_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_codes[i] = element.to_alipay_dict()
            if hasattr(self.service_codes, 'to_alipay_dict'):
                params['service_codes'] = self.service_codes.to_alipay_dict()
            else:
                params['service_codes'] = self.service_codes
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
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
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectModifyModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'bankcard_info' in d:
            o.bankcard_info = d['bankcard_info']
        if 'business_license' in d:
            o.business_license = d['business_license']
        if 'business_license_type' in d:
            o.business_license_type = d['business_license_type']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'org_pid' in d:
            o.org_pid = d['org_pid']
        if 'pay_code_info' in d:
            o.pay_code_info = d['pay_code_info']
        if 'service_codes' in d:
            o.service_codes = d['service_codes']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'site_info' in d:
            o.site_info = d['site_info']
        if 'source' in d:
            o.source = d['source']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


