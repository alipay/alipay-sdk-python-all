#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LucBusinessLicenseInfo import LucBusinessLicenseInfo
from alipay.aop.api.domain.LucContactWayInfo import LucContactWayInfo
from alipay.aop.api.domain.LucLegalPersonInfo import LucLegalPersonInfo
from alipay.aop.api.domain.LucStoreAddressInfo import LucStoreAddressInfo


class AlipayCommerceLifeserviceShopCreateModel(object):

    def __init__(self):
        self._authorization_letter = None
        self._brand_id = None
        self._business_license_info = None
        self._contact_ways = None
        self._legal_person_info = None
        self._qualification_business_license = None
        self._qualification_certificates = None
        self._qualification_expiration_date = None
        self._qualification_type = None
        self._shop_category = None
        self._shop_category_name = None
        self._shop_name = None
        self._shop_type = None
        self._store_address_info = None
        self._supplementary_material_type = None
        self._supplementary_material_url = None

    @property
    def authorization_letter(self):
        return self._authorization_letter

    @authorization_letter.setter
    def authorization_letter(self, value):
        self._authorization_letter = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def business_license_info(self):
        return self._business_license_info

    @business_license_info.setter
    def business_license_info(self, value):
        if isinstance(value, LucBusinessLicenseInfo):
            self._business_license_info = value
        else:
            self._business_license_info = LucBusinessLicenseInfo.from_alipay_dict(value)
    @property
    def contact_ways(self):
        return self._contact_ways

    @contact_ways.setter
    def contact_ways(self, value):
        if isinstance(value, list):
            self._contact_ways = list()
            for i in value:
                if isinstance(i, LucContactWayInfo):
                    self._contact_ways.append(i)
                else:
                    self._contact_ways.append(LucContactWayInfo.from_alipay_dict(i))
    @property
    def legal_person_info(self):
        return self._legal_person_info

    @legal_person_info.setter
    def legal_person_info(self, value):
        if isinstance(value, LucLegalPersonInfo):
            self._legal_person_info = value
        else:
            self._legal_person_info = LucLegalPersonInfo.from_alipay_dict(value)
    @property
    def qualification_business_license(self):
        return self._qualification_business_license

    @qualification_business_license.setter
    def qualification_business_license(self, value):
        self._qualification_business_license = value
    @property
    def qualification_certificates(self):
        return self._qualification_certificates

    @qualification_certificates.setter
    def qualification_certificates(self, value):
        self._qualification_certificates = value
    @property
    def qualification_expiration_date(self):
        return self._qualification_expiration_date

    @qualification_expiration_date.setter
    def qualification_expiration_date(self, value):
        self._qualification_expiration_date = value
    @property
    def qualification_type(self):
        return self._qualification_type

    @qualification_type.setter
    def qualification_type(self, value):
        self._qualification_type = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
    @property
    def shop_category_name(self):
        return self._shop_category_name

    @shop_category_name.setter
    def shop_category_name(self, value):
        self._shop_category_name = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def store_address_info(self):
        return self._store_address_info

    @store_address_info.setter
    def store_address_info(self, value):
        if isinstance(value, LucStoreAddressInfo):
            self._store_address_info = value
        else:
            self._store_address_info = LucStoreAddressInfo.from_alipay_dict(value)
    @property
    def supplementary_material_type(self):
        return self._supplementary_material_type

    @supplementary_material_type.setter
    def supplementary_material_type(self, value):
        self._supplementary_material_type = value
    @property
    def supplementary_material_url(self):
        return self._supplementary_material_url

    @supplementary_material_url.setter
    def supplementary_material_url(self, value):
        self._supplementary_material_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization_letter:
            if hasattr(self.authorization_letter, 'to_alipay_dict'):
                params['authorization_letter'] = self.authorization_letter.to_alipay_dict()
            else:
                params['authorization_letter'] = self.authorization_letter
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.business_license_info:
            if hasattr(self.business_license_info, 'to_alipay_dict'):
                params['business_license_info'] = self.business_license_info.to_alipay_dict()
            else:
                params['business_license_info'] = self.business_license_info
        if self.contact_ways:
            if isinstance(self.contact_ways, list):
                for i in range(0, len(self.contact_ways)):
                    element = self.contact_ways[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_ways[i] = element.to_alipay_dict()
            if hasattr(self.contact_ways, 'to_alipay_dict'):
                params['contact_ways'] = self.contact_ways.to_alipay_dict()
            else:
                params['contact_ways'] = self.contact_ways
        if self.legal_person_info:
            if hasattr(self.legal_person_info, 'to_alipay_dict'):
                params['legal_person_info'] = self.legal_person_info.to_alipay_dict()
            else:
                params['legal_person_info'] = self.legal_person_info
        if self.qualification_business_license:
            if hasattr(self.qualification_business_license, 'to_alipay_dict'):
                params['qualification_business_license'] = self.qualification_business_license.to_alipay_dict()
            else:
                params['qualification_business_license'] = self.qualification_business_license
        if self.qualification_certificates:
            if hasattr(self.qualification_certificates, 'to_alipay_dict'):
                params['qualification_certificates'] = self.qualification_certificates.to_alipay_dict()
            else:
                params['qualification_certificates'] = self.qualification_certificates
        if self.qualification_expiration_date:
            if hasattr(self.qualification_expiration_date, 'to_alipay_dict'):
                params['qualification_expiration_date'] = self.qualification_expiration_date.to_alipay_dict()
            else:
                params['qualification_expiration_date'] = self.qualification_expiration_date
        if self.qualification_type:
            if hasattr(self.qualification_type, 'to_alipay_dict'):
                params['qualification_type'] = self.qualification_type.to_alipay_dict()
            else:
                params['qualification_type'] = self.qualification_type
        if self.shop_category:
            if hasattr(self.shop_category, 'to_alipay_dict'):
                params['shop_category'] = self.shop_category.to_alipay_dict()
            else:
                params['shop_category'] = self.shop_category
        if self.shop_category_name:
            if hasattr(self.shop_category_name, 'to_alipay_dict'):
                params['shop_category_name'] = self.shop_category_name.to_alipay_dict()
            else:
                params['shop_category_name'] = self.shop_category_name
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.store_address_info:
            if hasattr(self.store_address_info, 'to_alipay_dict'):
                params['store_address_info'] = self.store_address_info.to_alipay_dict()
            else:
                params['store_address_info'] = self.store_address_info
        if self.supplementary_material_type:
            if hasattr(self.supplementary_material_type, 'to_alipay_dict'):
                params['supplementary_material_type'] = self.supplementary_material_type.to_alipay_dict()
            else:
                params['supplementary_material_type'] = self.supplementary_material_type
        if self.supplementary_material_url:
            if hasattr(self.supplementary_material_url, 'to_alipay_dict'):
                params['supplementary_material_url'] = self.supplementary_material_url.to_alipay_dict()
            else:
                params['supplementary_material_url'] = self.supplementary_material_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceShopCreateModel()
        if 'authorization_letter' in d:
            o.authorization_letter = d['authorization_letter']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'business_license_info' in d:
            o.business_license_info = d['business_license_info']
        if 'contact_ways' in d:
            o.contact_ways = d['contact_ways']
        if 'legal_person_info' in d:
            o.legal_person_info = d['legal_person_info']
        if 'qualification_business_license' in d:
            o.qualification_business_license = d['qualification_business_license']
        if 'qualification_certificates' in d:
            o.qualification_certificates = d['qualification_certificates']
        if 'qualification_expiration_date' in d:
            o.qualification_expiration_date = d['qualification_expiration_date']
        if 'qualification_type' in d:
            o.qualification_type = d['qualification_type']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_category_name' in d:
            o.shop_category_name = d['shop_category_name']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'store_address_info' in d:
            o.store_address_info = d['store_address_info']
        if 'supplementary_material_type' in d:
            o.supplementary_material_type = d['supplementary_material_type']
        if 'supplementary_material_url' in d:
            o.supplementary_material_url = d['supplementary_material_url']
        return o


