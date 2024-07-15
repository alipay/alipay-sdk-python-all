#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MedicalShopTimePeriod import MedicalShopTimePeriod
from alipay.aop.api.domain.MedicalShopDeliveryInfo import MedicalShopDeliveryInfo
from alipay.aop.api.domain.MedicalShopMarketingActivity import MedicalShopMarketingActivity
from alipay.aop.api.domain.MedicalShopTag import MedicalShopTag


class AlipayCommerceMedicalMedicineShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedicineShopQueryResponse, self).__init__()
        self._address = None
        self._business_status = None
        self._business_time = None
        self._city_code = None
        self._delivery_info = None
        self._district_code = None
        self._latitude = None
        self._longitude = None
        self._marketing_activity = None
        self._medical_org_no = None
        self._out_store_id = None
        self._poiid = None
        self._province_code = None
        self._shop_category = None
        self._shop_id = None
        self._shop_logo = None
        self._shop_name = None
        self._shop_tags = None
        self._shop_type = None
        self._shop_url = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def business_status(self):
        return self._business_status

    @business_status.setter
    def business_status(self, value):
        self._business_status = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, MedicalShopTimePeriod):
                    self._business_time.append(i)
                else:
                    self._business_time.append(MedicalShopTimePeriod.from_alipay_dict(i))
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        if isinstance(value, list):
            self._delivery_info = list()
            for i in value:
                if isinstance(i, MedicalShopDeliveryInfo):
                    self._delivery_info.append(i)
                else:
                    self._delivery_info.append(MedicalShopDeliveryInfo.from_alipay_dict(i))
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def marketing_activity(self):
        return self._marketing_activity

    @marketing_activity.setter
    def marketing_activity(self, value):
        if isinstance(value, list):
            self._marketing_activity = list()
            for i in value:
                if isinstance(i, MedicalShopMarketingActivity):
                    self._marketing_activity.append(i)
                else:
                    self._marketing_activity.append(MedicalShopMarketingActivity.from_alipay_dict(i))
    @property
    def medical_org_no(self):
        return self._medical_org_no

    @medical_org_no.setter
    def medical_org_no(self, value):
        self._medical_org_no = value
    @property
    def out_store_id(self):
        return self._out_store_id

    @out_store_id.setter
    def out_store_id(self, value):
        self._out_store_id = value
    @property
    def poiid(self):
        return self._poiid

    @poiid.setter
    def poiid(self, value):
        self._poiid = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
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
    def shop_logo(self):
        return self._shop_logo

    @shop_logo.setter
    def shop_logo(self, value):
        self._shop_logo = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_tags(self):
        return self._shop_tags

    @shop_tags.setter
    def shop_tags(self, value):
        if isinstance(value, list):
            self._shop_tags = list()
            for i in value:
                if isinstance(i, MedicalShopTag):
                    self._shop_tags.append(i)
                else:
                    self._shop_tags.append(MedicalShopTag.from_alipay_dict(i))
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def shop_url(self):
        return self._shop_url

    @shop_url.setter
    def shop_url(self, value):
        self._shop_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedicineShopQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'business_status' in response:
            self.business_status = response['business_status']
        if 'business_time' in response:
            self.business_time = response['business_time']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'delivery_info' in response:
            self.delivery_info = response['delivery_info']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'marketing_activity' in response:
            self.marketing_activity = response['marketing_activity']
        if 'medical_org_no' in response:
            self.medical_org_no = response['medical_org_no']
        if 'out_store_id' in response:
            self.out_store_id = response['out_store_id']
        if 'poiid' in response:
            self.poiid = response['poiid']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'shop_category' in response:
            self.shop_category = response['shop_category']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_logo' in response:
            self.shop_logo = response['shop_logo']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_tags' in response:
            self.shop_tags = response['shop_tags']
        if 'shop_type' in response:
            self.shop_type = response['shop_type']
        if 'shop_url' in response:
            self.shop_url = response['shop_url']
