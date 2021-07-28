#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsShopStatusDTO import LogisticsShopStatusDTO


class AlipayOpenInstantdeliveryMerchantshopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInstantdeliveryMerchantshopQueryResponse, self).__init__()
        self._contact_name = None
        self._detail_address = None
        self._enterprise_city = None
        self._enterprise_district = None
        self._enterprise_province = None
        self._latitude = None
        self._logistics_shop_status = None
        self._longitude = None
        self._phone = None
        self._poiid = None
        self._shop_category = None
        self._shop_name = None
        self._shop_no = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def enterprise_city(self):
        return self._enterprise_city

    @enterprise_city.setter
    def enterprise_city(self, value):
        self._enterprise_city = value
    @property
    def enterprise_district(self):
        return self._enterprise_district

    @enterprise_district.setter
    def enterprise_district(self, value):
        self._enterprise_district = value
    @property
    def enterprise_province(self):
        return self._enterprise_province

    @enterprise_province.setter
    def enterprise_province(self, value):
        self._enterprise_province = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def logistics_shop_status(self):
        return self._logistics_shop_status

    @logistics_shop_status.setter
    def logistics_shop_status(self, value):
        if isinstance(value, list):
            self._logistics_shop_status = list()
            for i in value:
                if isinstance(i, LogisticsShopStatusDTO):
                    self._logistics_shop_status.append(i)
                else:
                    self._logistics_shop_status.append(LogisticsShopStatusDTO.from_alipay_dict(i))
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def poiid(self):
        return self._poiid

    @poiid.setter
    def poiid(self, value):
        self._poiid = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_no(self):
        return self._shop_no

    @shop_no.setter
    def shop_no(self, value):
        self._shop_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInstantdeliveryMerchantshopQueryResponse, self).parse_response_content(response_content)
        if 'contact_name' in response:
            self.contact_name = response['contact_name']
        if 'detail_address' in response:
            self.detail_address = response['detail_address']
        if 'enterprise_city' in response:
            self.enterprise_city = response['enterprise_city']
        if 'enterprise_district' in response:
            self.enterprise_district = response['enterprise_district']
        if 'enterprise_province' in response:
            self.enterprise_province = response['enterprise_province']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'logistics_shop_status' in response:
            self.logistics_shop_status = response['logistics_shop_status']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'phone' in response:
            self.phone = response['phone']
        if 'poiid' in response:
            self.poiid = response['poiid']
        if 'shop_category' in response:
            self.shop_category = response['shop_category']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_no' in response:
            self.shop_no = response['shop_no']
