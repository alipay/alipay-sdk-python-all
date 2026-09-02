#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LudBusinessLicenseInfo import LudBusinessLicenseInfo
from alipay.aop.api.domain.LudContactWayInfo import LudContactWayInfo
from alipay.aop.api.domain.LudLegalPersonInfo import LudLegalPersonInfo
from alipay.aop.api.domain.LudStoreAddressInfo import LudStoreAddressInfo


class AlipayCommerceLifeserviceShopdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceShopdetailQueryResponse, self).__init__()
        self._authorization_letter = None
        self._authorization_letter_url = None
        self._brand_id = None
        self._business_license_info = None
        self._contact_ways = None
        self._gmt_create = None
        self._gmt_modified = None
        self._legal_person_info = None
        self._mcc_code = None
        self._qualification_business_license = None
        self._qualification_certificates = None
        self._qualification_expiration_date = None
        self._qualification_type = None
        self._shop_category = None
        self._shop_category_name = None
        self._shop_id = None
        self._shop_name = None
        self._shop_type = None
        self._status = None
        self._store_address_info = None
        self._store_id = None
        self._supplementary_material_type = None
        self._supplementary_material_url = None

    @property
    def authorization_letter(self):
        return self._authorization_letter

    @authorization_letter.setter
    def authorization_letter(self, value):
        self._authorization_letter = value
    @property
    def authorization_letter_url(self):
        return self._authorization_letter_url

    @authorization_letter_url.setter
    def authorization_letter_url(self, value):
        self._authorization_letter_url = value
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
        if isinstance(value, LudBusinessLicenseInfo):
            self._business_license_info = value
        else:
            self._business_license_info = LudBusinessLicenseInfo.from_alipay_dict(value)
    @property
    def contact_ways(self):
        return self._contact_ways

    @contact_ways.setter
    def contact_ways(self, value):
        if isinstance(value, list):
            self._contact_ways = list()
            for i in value:
                if isinstance(i, LudContactWayInfo):
                    self._contact_ways.append(i)
                else:
                    self._contact_ways.append(LudContactWayInfo.from_alipay_dict(i))
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def legal_person_info(self):
        return self._legal_person_info

    @legal_person_info.setter
    def legal_person_info(self, value):
        if isinstance(value, LudLegalPersonInfo):
            self._legal_person_info = value
        else:
            self._legal_person_info = LudLegalPersonInfo.from_alipay_dict(value)
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
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
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_address_info(self):
        return self._store_address_info

    @store_address_info.setter
    def store_address_info(self, value):
        if isinstance(value, LudStoreAddressInfo):
            self._store_address_info = value
        else:
            self._store_address_info = LudStoreAddressInfo.from_alipay_dict(value)
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceShopdetailQueryResponse, self).parse_response_content(response_content)
        if 'authorization_letter' in response:
            self.authorization_letter = response['authorization_letter']
        if 'authorization_letter_url' in response:
            self.authorization_letter_url = response['authorization_letter_url']
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
        if 'business_license_info' in response:
            self.business_license_info = response['business_license_info']
        if 'contact_ways' in response:
            self.contact_ways = response['contact_ways']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'legal_person_info' in response:
            self.legal_person_info = response['legal_person_info']
        if 'mcc_code' in response:
            self.mcc_code = response['mcc_code']
        if 'qualification_business_license' in response:
            self.qualification_business_license = response['qualification_business_license']
        if 'qualification_certificates' in response:
            self.qualification_certificates = response['qualification_certificates']
        if 'qualification_expiration_date' in response:
            self.qualification_expiration_date = response['qualification_expiration_date']
        if 'qualification_type' in response:
            self.qualification_type = response['qualification_type']
        if 'shop_category' in response:
            self.shop_category = response['shop_category']
        if 'shop_category_name' in response:
            self.shop_category_name = response['shop_category_name']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_type' in response:
            self.shop_type = response['shop_type']
        if 'status' in response:
            self.status = response['status']
        if 'store_address_info' in response:
            self.store_address_info = response['store_address_info']
        if 'store_id' in response:
            self.store_id = response['store_id']
        if 'supplementary_material_type' in response:
            self.supplementary_material_type = response['supplementary_material_type']
        if 'supplementary_material_url' in response:
            self.supplementary_material_url = response['supplementary_material_url']
