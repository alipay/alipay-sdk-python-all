#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.MerchantContactPerson import MerchantContactPerson
from alipay.aop.api.domain.MerchantCertificateInfo import MerchantCertificateInfo
from alipay.aop.api.domain.MerchantCertificateInfo import MerchantCertificateInfo


class AntMerchantExpandSceneRoleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandSceneRoleQueryResponse, self).__init__()
        self._alias_name = None
        self._business_address = None
        self._category_code = None
        self._contact_persons = None
        self._contact_phones = None
        self._external_id = None
        self._legal_info = None
        self._license_info = None
        self._master_partner_id = None
        self._merchant_type = None
        self._name = None
        self._out_door_pic = None
        self._partner_id = None
        self._scene = None
        self._service_phones = None
        self._settle_alipay_logon_id = None

    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        if isinstance(value, AddressInfo):
            self._business_address = value
        else:
            self._business_address = AddressInfo.from_alipay_dict(value)
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def contact_persons(self):
        return self._contact_persons

    @contact_persons.setter
    def contact_persons(self, value):
        if isinstance(value, MerchantContactPerson):
            self._contact_persons = value
        else:
            self._contact_persons = MerchantContactPerson.from_alipay_dict(value)
    @property
    def contact_phones(self):
        return self._contact_phones

    @contact_phones.setter
    def contact_phones(self, value):
        if isinstance(value, list):
            self._contact_phones = list()
            for i in value:
                self._contact_phones.append(i)
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def legal_info(self):
        return self._legal_info

    @legal_info.setter
    def legal_info(self, value):
        if isinstance(value, MerchantCertificateInfo):
            self._legal_info = value
        else:
            self._legal_info = MerchantCertificateInfo.from_alipay_dict(value)
    @property
    def license_info(self):
        return self._license_info

    @license_info.setter
    def license_info(self, value):
        if isinstance(value, MerchantCertificateInfo):
            self._license_info = value
        else:
            self._license_info = MerchantCertificateInfo.from_alipay_dict(value)
    @property
    def master_partner_id(self):
        return self._master_partner_id

    @master_partner_id.setter
    def master_partner_id(self, value):
        self._master_partner_id = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_door_pic(self):
        return self._out_door_pic

    @out_door_pic.setter
    def out_door_pic(self, value):
        self._out_door_pic = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def service_phones(self):
        return self._service_phones

    @service_phones.setter
    def service_phones(self, value):
        if isinstance(value, list):
            self._service_phones = list()
            for i in value:
                self._service_phones.append(i)
    @property
    def settle_alipay_logon_id(self):
        return self._settle_alipay_logon_id

    @settle_alipay_logon_id.setter
    def settle_alipay_logon_id(self, value):
        self._settle_alipay_logon_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandSceneRoleQueryResponse, self).parse_response_content(response_content)
        if 'alias_name' in response:
            self.alias_name = response['alias_name']
        if 'business_address' in response:
            self.business_address = response['business_address']
        if 'category_code' in response:
            self.category_code = response['category_code']
        if 'contact_persons' in response:
            self.contact_persons = response['contact_persons']
        if 'contact_phones' in response:
            self.contact_phones = response['contact_phones']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'legal_info' in response:
            self.legal_info = response['legal_info']
        if 'license_info' in response:
            self.license_info = response['license_info']
        if 'master_partner_id' in response:
            self.master_partner_id = response['master_partner_id']
        if 'merchant_type' in response:
            self.merchant_type = response['merchant_type']
        if 'name' in response:
            self.name = response['name']
        if 'out_door_pic' in response:
            self.out_door_pic = response['out_door_pic']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'scene' in response:
            self.scene = response['scene']
        if 'service_phones' in response:
            self.service_phones = response['service_phones']
        if 'settle_alipay_logon_id' in response:
            self.settle_alipay_logon_id = response['settle_alipay_logon_id']
