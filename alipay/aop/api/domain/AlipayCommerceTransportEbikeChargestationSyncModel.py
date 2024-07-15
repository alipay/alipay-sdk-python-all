#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEbikeChargestationSyncModel(object):

    def __init__(self):
        self._address = None
        self._available_plug_count = None
        self._brand_code = None
        self._brand_name = None
        self._city_code = None
        self._city_name = None
        self._data_source = None
        self._detail_link_url = None
        self._device_field_type = None
        self._device_lbs = None
        self._device_name = None
        self._device_no = None
        self._device_status = None
        self._device_type_code = None
        self._fee_desc = None
        self._field_image_list = None
        self._field_service_desc = None
        self._maximum_power = None
        self._pay_type = None
        self._plug_sum = None
        self._province = None
        self._station_name = None
        self._station_no = None
        self._sync_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def available_plug_count(self):
        return self._available_plug_count

    @available_plug_count.setter
    def available_plug_count(self, value):
        self._available_plug_count = value
    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def detail_link_url(self):
        return self._detail_link_url

    @detail_link_url.setter
    def detail_link_url(self, value):
        self._detail_link_url = value
    @property
    def device_field_type(self):
        return self._device_field_type

    @device_field_type.setter
    def device_field_type(self, value):
        self._device_field_type = value
    @property
    def device_lbs(self):
        return self._device_lbs

    @device_lbs.setter
    def device_lbs(self, value):
        self._device_lbs = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def device_type_code(self):
        return self._device_type_code

    @device_type_code.setter
    def device_type_code(self, value):
        self._device_type_code = value
    @property
    def fee_desc(self):
        return self._fee_desc

    @fee_desc.setter
    def fee_desc(self, value):
        self._fee_desc = value
    @property
    def field_image_list(self):
        return self._field_image_list

    @field_image_list.setter
    def field_image_list(self, value):
        if isinstance(value, list):
            self._field_image_list = list()
            for i in value:
                self._field_image_list.append(i)
    @property
    def field_service_desc(self):
        return self._field_service_desc

    @field_service_desc.setter
    def field_service_desc(self, value):
        if isinstance(value, list):
            self._field_service_desc = list()
            for i in value:
                self._field_service_desc.append(i)
    @property
    def maximum_power(self):
        return self._maximum_power

    @maximum_power.setter
    def maximum_power(self, value):
        self._maximum_power = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def plug_sum(self):
        return self._plug_sum

    @plug_sum.setter
    def plug_sum(self, value):
        self._plug_sum = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def station_no(self):
        return self._station_no

    @station_no.setter
    def station_no(self, value):
        self._station_no = value
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.available_plug_count:
            if hasattr(self.available_plug_count, 'to_alipay_dict'):
                params['available_plug_count'] = self.available_plug_count.to_alipay_dict()
            else:
                params['available_plug_count'] = self.available_plug_count
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.detail_link_url:
            if hasattr(self.detail_link_url, 'to_alipay_dict'):
                params['detail_link_url'] = self.detail_link_url.to_alipay_dict()
            else:
                params['detail_link_url'] = self.detail_link_url
        if self.device_field_type:
            if hasattr(self.device_field_type, 'to_alipay_dict'):
                params['device_field_type'] = self.device_field_type.to_alipay_dict()
            else:
                params['device_field_type'] = self.device_field_type
        if self.device_lbs:
            if hasattr(self.device_lbs, 'to_alipay_dict'):
                params['device_lbs'] = self.device_lbs.to_alipay_dict()
            else:
                params['device_lbs'] = self.device_lbs
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.device_status:
            if hasattr(self.device_status, 'to_alipay_dict'):
                params['device_status'] = self.device_status.to_alipay_dict()
            else:
                params['device_status'] = self.device_status
        if self.device_type_code:
            if hasattr(self.device_type_code, 'to_alipay_dict'):
                params['device_type_code'] = self.device_type_code.to_alipay_dict()
            else:
                params['device_type_code'] = self.device_type_code
        if self.fee_desc:
            if hasattr(self.fee_desc, 'to_alipay_dict'):
                params['fee_desc'] = self.fee_desc.to_alipay_dict()
            else:
                params['fee_desc'] = self.fee_desc
        if self.field_image_list:
            if isinstance(self.field_image_list, list):
                for i in range(0, len(self.field_image_list)):
                    element = self.field_image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.field_image_list[i] = element.to_alipay_dict()
            if hasattr(self.field_image_list, 'to_alipay_dict'):
                params['field_image_list'] = self.field_image_list.to_alipay_dict()
            else:
                params['field_image_list'] = self.field_image_list
        if self.field_service_desc:
            if isinstance(self.field_service_desc, list):
                for i in range(0, len(self.field_service_desc)):
                    element = self.field_service_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.field_service_desc[i] = element.to_alipay_dict()
            if hasattr(self.field_service_desc, 'to_alipay_dict'):
                params['field_service_desc'] = self.field_service_desc.to_alipay_dict()
            else:
                params['field_service_desc'] = self.field_service_desc
        if self.maximum_power:
            if hasattr(self.maximum_power, 'to_alipay_dict'):
                params['maximum_power'] = self.maximum_power.to_alipay_dict()
            else:
                params['maximum_power'] = self.maximum_power
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.plug_sum:
            if hasattr(self.plug_sum, 'to_alipay_dict'):
                params['plug_sum'] = self.plug_sum.to_alipay_dict()
            else:
                params['plug_sum'] = self.plug_sum
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        if self.station_no:
            if hasattr(self.station_no, 'to_alipay_dict'):
                params['station_no'] = self.station_no.to_alipay_dict()
            else:
                params['station_no'] = self.station_no
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEbikeChargestationSyncModel()
        if 'address' in d:
            o.address = d['address']
        if 'available_plug_count' in d:
            o.available_plug_count = d['available_plug_count']
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'detail_link_url' in d:
            o.detail_link_url = d['detail_link_url']
        if 'device_field_type' in d:
            o.device_field_type = d['device_field_type']
        if 'device_lbs' in d:
            o.device_lbs = d['device_lbs']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'device_status' in d:
            o.device_status = d['device_status']
        if 'device_type_code' in d:
            o.device_type_code = d['device_type_code']
        if 'fee_desc' in d:
            o.fee_desc = d['fee_desc']
        if 'field_image_list' in d:
            o.field_image_list = d['field_image_list']
        if 'field_service_desc' in d:
            o.field_service_desc = d['field_service_desc']
        if 'maximum_power' in d:
            o.maximum_power = d['maximum_power']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'plug_sum' in d:
            o.plug_sum = d['plug_sum']
        if 'province' in d:
            o.province = d['province']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'station_no' in d:
            o.station_no = d['station_no']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


