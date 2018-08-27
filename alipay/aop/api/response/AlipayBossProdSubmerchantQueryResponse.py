#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdSubmerchantQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdSubmerchantQueryResponse, self).__init__()
        self._address = None
        self._alias_name = None
        self._business_license = None
        self._category_id = None
        self._city_code = None
        self._contact_email = None
        self._contact_mobile = None
        self._contact_name = None
        self._contact_phone = None
        self._district_code = None
        self._external_id = None
        self._id_card = None
        self._memo = None
        self._name = None
        self._province_code = None
        self._service_phone = None
        self._source = None
        self._sub_merchant_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
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
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
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
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdSubmerchantQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'alias_name' in response:
            self.alias_name = response['alias_name']
        if 'business_license' in response:
            self.business_license = response['business_license']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'contact_email' in response:
            self.contact_email = response['contact_email']
        if 'contact_mobile' in response:
            self.contact_mobile = response['contact_mobile']
        if 'contact_name' in response:
            self.contact_name = response['contact_name']
        if 'contact_phone' in response:
            self.contact_phone = response['contact_phone']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'id_card' in response:
            self.id_card = response['id_card']
        if 'memo' in response:
            self.memo = response['memo']
        if 'name' in response:
            self.name = response['name']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
        if 'source' in response:
            self.source = response['source']
        if 'sub_merchant_id' in response:
            self.sub_merchant_id = response['sub_merchant_id']
