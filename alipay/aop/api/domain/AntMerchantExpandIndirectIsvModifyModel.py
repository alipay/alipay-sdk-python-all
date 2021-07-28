#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.ContactInfo import ContactInfo


class AntMerchantExpandIndirectIsvModifyModel(object):

    def __init__(self):
        self._address_info = None
        self._alias_name = None
        self._business_license = None
        self._business_license_photo = None
        self._business_license_type = None
        self._contact_info = None
        self._mcc = None
        self._name = None
        self._service_phone = None
        self._sub_merchant_id = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, AddressInfo):
            self._address_info = value
        else:
            self._address_info = AddressInfo.from_alipay_dict(value)
    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def business_license(self):
        return self._business_license

    @business_license.setter
    def business_license(self, value):
        self._business_license = value
    @property
    def business_license_photo(self):
        return self._business_license_photo

    @business_license_photo.setter
    def business_license_photo(self, value):
        self._business_license_photo = value
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
        if isinstance(value, ContactInfo):
            self._contact_info = value
        else:
            self._contact_info = ContactInfo.from_alipay_dict(value)
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.business_license:
            if hasattr(self.business_license, 'to_alipay_dict'):
                params['business_license'] = self.business_license.to_alipay_dict()
            else:
                params['business_license'] = self.business_license
        if self.business_license_photo:
            if hasattr(self.business_license_photo, 'to_alipay_dict'):
                params['business_license_photo'] = self.business_license_photo.to_alipay_dict()
            else:
                params['business_license_photo'] = self.business_license_photo
        if self.business_license_type:
            if hasattr(self.business_license_type, 'to_alipay_dict'):
                params['business_license_type'] = self.business_license_type.to_alipay_dict()
            else:
                params['business_license_type'] = self.business_license_type
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
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
        o = AntMerchantExpandIndirectIsvModifyModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'business_license' in d:
            o.business_license = d['business_license']
        if 'business_license_photo' in d:
            o.business_license_photo = d['business_license_photo']
        if 'business_license_type' in d:
            o.business_license_type = d['business_license_type']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'name' in d:
            o.name = d['name']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


