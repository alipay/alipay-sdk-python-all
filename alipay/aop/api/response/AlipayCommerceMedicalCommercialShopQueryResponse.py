#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopBusinessAddress import ShopBusinessAddress


class AlipayCommerceMedicalCommercialShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialShopQueryResponse, self).__init__()
        self._advertise_service_cert = None
        self._business_address = None
        self._cert_image = None
        self._logo = None
        self._medical_level_tags = None
        self._medical_service_cert = None
        self._merchant_name = None
        self._pid = None
        self._shop_id = None
        self._shop_images = None
        self._shop_name = None

    @property
    def advertise_service_cert(self):
        return self._advertise_service_cert

    @advertise_service_cert.setter
    def advertise_service_cert(self, value):
        self._advertise_service_cert = value
    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        if isinstance(value, ShopBusinessAddress):
            self._business_address = value
        else:
            self._business_address = ShopBusinessAddress.from_alipay_dict(value)
    @property
    def cert_image(self):
        return self._cert_image

    @cert_image.setter
    def cert_image(self, value):
        self._cert_image = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def medical_level_tags(self):
        return self._medical_level_tags

    @medical_level_tags.setter
    def medical_level_tags(self, value):
        if isinstance(value, list):
            self._medical_level_tags = list()
            for i in value:
                self._medical_level_tags.append(i)
    @property
    def medical_service_cert(self):
        return self._medical_service_cert

    @medical_service_cert.setter
    def medical_service_cert(self, value):
        self._medical_service_cert = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_images(self):
        return self._shop_images

    @shop_images.setter
    def shop_images(self, value):
        if isinstance(value, list):
            self._shop_images = list()
            for i in value:
                self._shop_images.append(i)
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialShopQueryResponse, self).parse_response_content(response_content)
        if 'advertise_service_cert' in response:
            self.advertise_service_cert = response['advertise_service_cert']
        if 'business_address' in response:
            self.business_address = response['business_address']
        if 'cert_image' in response:
            self.cert_image = response['cert_image']
        if 'logo' in response:
            self.logo = response['logo']
        if 'medical_level_tags' in response:
            self.medical_level_tags = response['medical_level_tags']
        if 'medical_service_cert' in response:
            self.medical_service_cert = response['medical_service_cert']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'pid' in response:
            self.pid = response['pid']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_images' in response:
            self.shop_images = response['shop_images']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
