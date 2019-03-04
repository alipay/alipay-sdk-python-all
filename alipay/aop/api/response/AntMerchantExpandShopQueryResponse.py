#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.ShopBusinessTime import ShopBusinessTime
from alipay.aop.api.domain.ContactInfo import ContactInfo
from alipay.aop.api.domain.ShopExtInfo import ShopExtInfo
from alipay.aop.api.domain.IndustryQualificationInfo import IndustryQualificationInfo


class AntMerchantExpandShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandShopQueryResponse, self).__init__()
        self._brand_id = None
        self._business_address = None
        self._business_time = None
        self._cert_image = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._contact_infos = None
        self._contact_mobile = None
        self._contact_phone = None
        self._ext_infos = None
        self._ip_role_id = None
        self._legal_cert_no = None
        self._legal_name = None
        self._license_auth_letter_image = None
        self._memo = None
        self._out_door_images = None
        self._qualifications = None
        self._scene = None
        self._settle_alipay_logon_id = None
        self._shop_category = None
        self._shop_id = None
        self._shop_name = None
        self._shop_type = None
        self._store_id = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
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
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, ShopBusinessTime):
                    self._business_time.append(i)
                else:
                    self._business_time.append(ShopBusinessTime.from_alipay_dict(i))
    @property
    def cert_image(self):
        return self._cert_image

    @cert_image.setter
    def cert_image(self, value):
        self._cert_image = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def contact_infos(self):
        return self._contact_infos

    @contact_infos.setter
    def contact_infos(self, value):
        if isinstance(value, list):
            self._contact_infos = list()
            for i in value:
                if isinstance(i, ContactInfo):
                    self._contact_infos.append(i)
                else:
                    self._contact_infos.append(ContactInfo.from_alipay_dict(i))
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        if isinstance(value, list):
            self._ext_infos = list()
            for i in value:
                if isinstance(i, ShopExtInfo):
                    self._ext_infos.append(i)
                else:
                    self._ext_infos.append(ShopExtInfo.from_alipay_dict(i))
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def legal_cert_no(self):
        return self._legal_cert_no

    @legal_cert_no.setter
    def legal_cert_no(self, value):
        self._legal_cert_no = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def license_auth_letter_image(self):
        return self._license_auth_letter_image

    @license_auth_letter_image.setter
    def license_auth_letter_image(self, value):
        self._license_auth_letter_image = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_door_images(self):
        return self._out_door_images

    @out_door_images.setter
    def out_door_images(self, value):
        if isinstance(value, list):
            self._out_door_images = list()
            for i in value:
                self._out_door_images.append(i)
    @property
    def qualifications(self):
        return self._qualifications

    @qualifications.setter
    def qualifications(self, value):
        if isinstance(value, list):
            self._qualifications = list()
            for i in value:
                if isinstance(i, IndustryQualificationInfo):
                    self._qualifications.append(i)
                else:
                    self._qualifications.append(IndustryQualificationInfo.from_alipay_dict(i))
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def settle_alipay_logon_id(self):
        return self._settle_alipay_logon_id

    @settle_alipay_logon_id.setter
    def settle_alipay_logon_id(self, value):
        self._settle_alipay_logon_id = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
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
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandShopQueryResponse, self).parse_response_content(response_content)
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
        if 'business_address' in response:
            self.business_address = response['business_address']
        if 'business_time' in response:
            self.business_time = response['business_time']
        if 'cert_image' in response:
            self.cert_image = response['cert_image']
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'contact_infos' in response:
            self.contact_infos = response['contact_infos']
        if 'contact_mobile' in response:
            self.contact_mobile = response['contact_mobile']
        if 'contact_phone' in response:
            self.contact_phone = response['contact_phone']
        if 'ext_infos' in response:
            self.ext_infos = response['ext_infos']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'legal_cert_no' in response:
            self.legal_cert_no = response['legal_cert_no']
        if 'legal_name' in response:
            self.legal_name = response['legal_name']
        if 'license_auth_letter_image' in response:
            self.license_auth_letter_image = response['license_auth_letter_image']
        if 'memo' in response:
            self.memo = response['memo']
        if 'out_door_images' in response:
            self.out_door_images = response['out_door_images']
        if 'qualifications' in response:
            self.qualifications = response['qualifications']
        if 'scene' in response:
            self.scene = response['scene']
        if 'settle_alipay_logon_id' in response:
            self.settle_alipay_logon_id = response['settle_alipay_logon_id']
        if 'shop_category' in response:
            self.shop_category = response['shop_category']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_type' in response:
            self.shop_type = response['shop_type']
        if 'store_id' in response:
            self.store_id = response['store_id']
