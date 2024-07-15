#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalShopTimePeriod import MedicalShopTimePeriod
from alipay.aop.api.domain.MedicalShopDeliveryInfo import MedicalShopDeliveryInfo
from alipay.aop.api.domain.MedicalShopMarketingActivity import MedicalShopMarketingActivity
from alipay.aop.api.domain.MedicalShopTag import MedicalShopTag


class AlipayCommerceMedicalMedicineShopCreateModel(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.business_status:
            if hasattr(self.business_status, 'to_alipay_dict'):
                params['business_status'] = self.business_status.to_alipay_dict()
            else:
                params['business_status'] = self.business_status
        if self.business_time:
            if isinstance(self.business_time, list):
                for i in range(0, len(self.business_time)):
                    element = self.business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_time[i] = element.to_alipay_dict()
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.delivery_info:
            if isinstance(self.delivery_info, list):
                for i in range(0, len(self.delivery_info)):
                    element = self.delivery_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_info[i] = element.to_alipay_dict()
            if hasattr(self.delivery_info, 'to_alipay_dict'):
                params['delivery_info'] = self.delivery_info.to_alipay_dict()
            else:
                params['delivery_info'] = self.delivery_info
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.marketing_activity:
            if isinstance(self.marketing_activity, list):
                for i in range(0, len(self.marketing_activity)):
                    element = self.marketing_activity[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.marketing_activity[i] = element.to_alipay_dict()
            if hasattr(self.marketing_activity, 'to_alipay_dict'):
                params['marketing_activity'] = self.marketing_activity.to_alipay_dict()
            else:
                params['marketing_activity'] = self.marketing_activity
        if self.medical_org_no:
            if hasattr(self.medical_org_no, 'to_alipay_dict'):
                params['medical_org_no'] = self.medical_org_no.to_alipay_dict()
            else:
                params['medical_org_no'] = self.medical_org_no
        if self.out_store_id:
            if hasattr(self.out_store_id, 'to_alipay_dict'):
                params['out_store_id'] = self.out_store_id.to_alipay_dict()
            else:
                params['out_store_id'] = self.out_store_id
        if self.poiid:
            if hasattr(self.poiid, 'to_alipay_dict'):
                params['poiid'] = self.poiid.to_alipay_dict()
            else:
                params['poiid'] = self.poiid
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.shop_category:
            if hasattr(self.shop_category, 'to_alipay_dict'):
                params['shop_category'] = self.shop_category.to_alipay_dict()
            else:
                params['shop_category'] = self.shop_category
        if self.shop_logo:
            if hasattr(self.shop_logo, 'to_alipay_dict'):
                params['shop_logo'] = self.shop_logo.to_alipay_dict()
            else:
                params['shop_logo'] = self.shop_logo
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_tags:
            if isinstance(self.shop_tags, list):
                for i in range(0, len(self.shop_tags)):
                    element = self.shop_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_tags[i] = element.to_alipay_dict()
            if hasattr(self.shop_tags, 'to_alipay_dict'):
                params['shop_tags'] = self.shop_tags.to_alipay_dict()
            else:
                params['shop_tags'] = self.shop_tags
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.shop_url:
            if hasattr(self.shop_url, 'to_alipay_dict'):
                params['shop_url'] = self.shop_url.to_alipay_dict()
            else:
                params['shop_url'] = self.shop_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedicineShopCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'business_status' in d:
            o.business_status = d['business_status']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'marketing_activity' in d:
            o.marketing_activity = d['marketing_activity']
        if 'medical_org_no' in d:
            o.medical_org_no = d['medical_org_no']
        if 'out_store_id' in d:
            o.out_store_id = d['out_store_id']
        if 'poiid' in d:
            o.poiid = d['poiid']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_logo' in d:
            o.shop_logo = d['shop_logo']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_tags' in d:
            o.shop_tags = d['shop_tags']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'shop_url' in d:
            o.shop_url = d['shop_url']
        return o


