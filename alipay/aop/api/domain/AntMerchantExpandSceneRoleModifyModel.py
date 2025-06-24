#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.MerchantContactPerson import MerchantContactPerson
from alipay.aop.api.domain.MerchantCertificateInfo import MerchantCertificateInfo
from alipay.aop.api.domain.MerchantCertificateInfo import MerchantCertificateInfo


class AntMerchantExpandSceneRoleModifyModel(object):

    def __init__(self):
        self._alias_name = None
        self._business_address = None
        self._category_code = None
        self._contact_persons = None
        self._contact_phones = None
        self._external_id = None
        self._legal_info = None
        self._license_info = None
        self._master_partner_id = None
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


    def to_alipay_dict(self):
        params = dict()
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.business_address:
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.contact_persons:
            if hasattr(self.contact_persons, 'to_alipay_dict'):
                params['contact_persons'] = self.contact_persons.to_alipay_dict()
            else:
                params['contact_persons'] = self.contact_persons
        if self.contact_phones:
            if isinstance(self.contact_phones, list):
                for i in range(0, len(self.contact_phones)):
                    element = self.contact_phones[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_phones[i] = element.to_alipay_dict()
            if hasattr(self.contact_phones, 'to_alipay_dict'):
                params['contact_phones'] = self.contact_phones.to_alipay_dict()
            else:
                params['contact_phones'] = self.contact_phones
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.legal_info:
            if hasattr(self.legal_info, 'to_alipay_dict'):
                params['legal_info'] = self.legal_info.to_alipay_dict()
            else:
                params['legal_info'] = self.legal_info
        if self.license_info:
            if hasattr(self.license_info, 'to_alipay_dict'):
                params['license_info'] = self.license_info.to_alipay_dict()
            else:
                params['license_info'] = self.license_info
        if self.master_partner_id:
            if hasattr(self.master_partner_id, 'to_alipay_dict'):
                params['master_partner_id'] = self.master_partner_id.to_alipay_dict()
            else:
                params['master_partner_id'] = self.master_partner_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_door_pic:
            if hasattr(self.out_door_pic, 'to_alipay_dict'):
                params['out_door_pic'] = self.out_door_pic.to_alipay_dict()
            else:
                params['out_door_pic'] = self.out_door_pic
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.service_phones:
            if isinstance(self.service_phones, list):
                for i in range(0, len(self.service_phones)):
                    element = self.service_phones[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_phones[i] = element.to_alipay_dict()
            if hasattr(self.service_phones, 'to_alipay_dict'):
                params['service_phones'] = self.service_phones.to_alipay_dict()
            else:
                params['service_phones'] = self.service_phones
        if self.settle_alipay_logon_id:
            if hasattr(self.settle_alipay_logon_id, 'to_alipay_dict'):
                params['settle_alipay_logon_id'] = self.settle_alipay_logon_id.to_alipay_dict()
            else:
                params['settle_alipay_logon_id'] = self.settle_alipay_logon_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandSceneRoleModifyModel()
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'contact_persons' in d:
            o.contact_persons = d['contact_persons']
        if 'contact_phones' in d:
            o.contact_phones = d['contact_phones']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'legal_info' in d:
            o.legal_info = d['legal_info']
        if 'license_info' in d:
            o.license_info = d['license_info']
        if 'master_partner_id' in d:
            o.master_partner_id = d['master_partner_id']
        if 'name' in d:
            o.name = d['name']
        if 'out_door_pic' in d:
            o.out_door_pic = d['out_door_pic']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'service_phones' in d:
            o.service_phones = d['service_phones']
        if 'settle_alipay_logon_id' in d:
            o.settle_alipay_logon_id = d['settle_alipay_logon_id']
        return o


