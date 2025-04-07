#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CheckReportData import CheckReportData


class TransferCarData(object):

    def __init__(self):
        self._acid = None
        self._activity_end_date = None
        self._activity_start_date = None
        self._attr_car_source_battery_owner_type = None
        self._audit_full_date = None
        self._auto_type = None
        self._brand_name = None
        self._brand_official_store = None
        self._call_phone = None
        self._car_color = None
        self._car_desc = None
        self._car_keys = None
        self._car_online_date = None
        self._car_source_type = None
        self._car_tags = None
        self._car_year = None
        self._check_report_data = None
        self._city_code = None
        self._displacement = None
        self._drive_distance = None
        self._emission_standard = None
        self._fuel_type = None
        self._full_img_url = None
        self._highlights = None
        self._images_url = None
        self._insurance_full_date = None
        self._isv_update_date = None
        self._license_full_date = None
        self._operation_type = None
        self._out_id = None
        self._price = None
        self._product_date = None
        self._seats = None
        self._series_name = None
        self._title = None
        self._transfer_count = None
        self._transfer_date = None
        self._transmission_type = None
        self._vehicle_display_status = None
        self._vehicle_video_url = None
        self._vin = None

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, value):
        self._acid = value
    @property
    def activity_end_date(self):
        return self._activity_end_date

    @activity_end_date.setter
    def activity_end_date(self, value):
        self._activity_end_date = value
    @property
    def activity_start_date(self):
        return self._activity_start_date

    @activity_start_date.setter
    def activity_start_date(self, value):
        self._activity_start_date = value
    @property
    def attr_car_source_battery_owner_type(self):
        return self._attr_car_source_battery_owner_type

    @attr_car_source_battery_owner_type.setter
    def attr_car_source_battery_owner_type(self, value):
        self._attr_car_source_battery_owner_type = value
    @property
    def audit_full_date(self):
        return self._audit_full_date

    @audit_full_date.setter
    def audit_full_date(self, value):
        self._audit_full_date = value
    @property
    def auto_type(self):
        return self._auto_type

    @auto_type.setter
    def auto_type(self, value):
        self._auto_type = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def brand_official_store(self):
        return self._brand_official_store

    @brand_official_store.setter
    def brand_official_store(self, value):
        self._brand_official_store = value
    @property
    def call_phone(self):
        return self._call_phone

    @call_phone.setter
    def call_phone(self, value):
        self._call_phone = value
    @property
    def car_color(self):
        return self._car_color

    @car_color.setter
    def car_color(self, value):
        self._car_color = value
    @property
    def car_desc(self):
        return self._car_desc

    @car_desc.setter
    def car_desc(self, value):
        self._car_desc = value
    @property
    def car_keys(self):
        return self._car_keys

    @car_keys.setter
    def car_keys(self, value):
        self._car_keys = value
    @property
    def car_online_date(self):
        return self._car_online_date

    @car_online_date.setter
    def car_online_date(self, value):
        self._car_online_date = value
    @property
    def car_source_type(self):
        return self._car_source_type

    @car_source_type.setter
    def car_source_type(self, value):
        self._car_source_type = value
    @property
    def car_tags(self):
        return self._car_tags

    @car_tags.setter
    def car_tags(self, value):
        if isinstance(value, list):
            self._car_tags = list()
            for i in value:
                self._car_tags.append(i)
    @property
    def car_year(self):
        return self._car_year

    @car_year.setter
    def car_year(self, value):
        self._car_year = value
    @property
    def check_report_data(self):
        return self._check_report_data

    @check_report_data.setter
    def check_report_data(self, value):
        if isinstance(value, CheckReportData):
            self._check_report_data = value
        else:
            self._check_report_data = CheckReportData.from_alipay_dict(value)
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value
    @property
    def drive_distance(self):
        return self._drive_distance

    @drive_distance.setter
    def drive_distance(self, value):
        self._drive_distance = value
    @property
    def emission_standard(self):
        return self._emission_standard

    @emission_standard.setter
    def emission_standard(self, value):
        self._emission_standard = value
    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self._fuel_type = value
    @property
    def full_img_url(self):
        return self._full_img_url

    @full_img_url.setter
    def full_img_url(self, value):
        self._full_img_url = value
    @property
    def highlights(self):
        return self._highlights

    @highlights.setter
    def highlights(self, value):
        if isinstance(value, list):
            self._highlights = list()
            for i in value:
                self._highlights.append(i)
    @property
    def images_url(self):
        return self._images_url

    @images_url.setter
    def images_url(self, value):
        if isinstance(value, list):
            self._images_url = list()
            for i in value:
                self._images_url.append(i)
    @property
    def insurance_full_date(self):
        return self._insurance_full_date

    @insurance_full_date.setter
    def insurance_full_date(self, value):
        self._insurance_full_date = value
    @property
    def isv_update_date(self):
        return self._isv_update_date

    @isv_update_date.setter
    def isv_update_date(self, value):
        self._isv_update_date = value
    @property
    def license_full_date(self):
        return self._license_full_date

    @license_full_date.setter
    def license_full_date(self, value):
        self._license_full_date = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def product_date(self):
        return self._product_date

    @product_date.setter
    def product_date(self, value):
        self._product_date = value
    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value
    @property
    def series_name(self):
        return self._series_name

    @series_name.setter
    def series_name(self, value):
        self._series_name = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def transfer_count(self):
        return self._transfer_count

    @transfer_count.setter
    def transfer_count(self, value):
        self._transfer_count = value
    @property
    def transfer_date(self):
        return self._transfer_date

    @transfer_date.setter
    def transfer_date(self, value):
        self._transfer_date = value
    @property
    def transmission_type(self):
        return self._transmission_type

    @transmission_type.setter
    def transmission_type(self, value):
        self._transmission_type = value
    @property
    def vehicle_display_status(self):
        return self._vehicle_display_status

    @vehicle_display_status.setter
    def vehicle_display_status(self, value):
        self._vehicle_display_status = value
    @property
    def vehicle_video_url(self):
        return self._vehicle_video_url

    @vehicle_video_url.setter
    def vehicle_video_url(self, value):
        self._vehicle_video_url = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.acid:
            if hasattr(self.acid, 'to_alipay_dict'):
                params['acid'] = self.acid.to_alipay_dict()
            else:
                params['acid'] = self.acid
        if self.activity_end_date:
            if hasattr(self.activity_end_date, 'to_alipay_dict'):
                params['activity_end_date'] = self.activity_end_date.to_alipay_dict()
            else:
                params['activity_end_date'] = self.activity_end_date
        if self.activity_start_date:
            if hasattr(self.activity_start_date, 'to_alipay_dict'):
                params['activity_start_date'] = self.activity_start_date.to_alipay_dict()
            else:
                params['activity_start_date'] = self.activity_start_date
        if self.attr_car_source_battery_owner_type:
            if hasattr(self.attr_car_source_battery_owner_type, 'to_alipay_dict'):
                params['attr_car_source_battery_owner_type'] = self.attr_car_source_battery_owner_type.to_alipay_dict()
            else:
                params['attr_car_source_battery_owner_type'] = self.attr_car_source_battery_owner_type
        if self.audit_full_date:
            if hasattr(self.audit_full_date, 'to_alipay_dict'):
                params['audit_full_date'] = self.audit_full_date.to_alipay_dict()
            else:
                params['audit_full_date'] = self.audit_full_date
        if self.auto_type:
            if hasattr(self.auto_type, 'to_alipay_dict'):
                params['auto_type'] = self.auto_type.to_alipay_dict()
            else:
                params['auto_type'] = self.auto_type
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.brand_official_store:
            if hasattr(self.brand_official_store, 'to_alipay_dict'):
                params['brand_official_store'] = self.brand_official_store.to_alipay_dict()
            else:
                params['brand_official_store'] = self.brand_official_store
        if self.call_phone:
            if hasattr(self.call_phone, 'to_alipay_dict'):
                params['call_phone'] = self.call_phone.to_alipay_dict()
            else:
                params['call_phone'] = self.call_phone
        if self.car_color:
            if hasattr(self.car_color, 'to_alipay_dict'):
                params['car_color'] = self.car_color.to_alipay_dict()
            else:
                params['car_color'] = self.car_color
        if self.car_desc:
            if hasattr(self.car_desc, 'to_alipay_dict'):
                params['car_desc'] = self.car_desc.to_alipay_dict()
            else:
                params['car_desc'] = self.car_desc
        if self.car_keys:
            if hasattr(self.car_keys, 'to_alipay_dict'):
                params['car_keys'] = self.car_keys.to_alipay_dict()
            else:
                params['car_keys'] = self.car_keys
        if self.car_online_date:
            if hasattr(self.car_online_date, 'to_alipay_dict'):
                params['car_online_date'] = self.car_online_date.to_alipay_dict()
            else:
                params['car_online_date'] = self.car_online_date
        if self.car_source_type:
            if hasattr(self.car_source_type, 'to_alipay_dict'):
                params['car_source_type'] = self.car_source_type.to_alipay_dict()
            else:
                params['car_source_type'] = self.car_source_type
        if self.car_tags:
            if isinstance(self.car_tags, list):
                for i in range(0, len(self.car_tags)):
                    element = self.car_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.car_tags[i] = element.to_alipay_dict()
            if hasattr(self.car_tags, 'to_alipay_dict'):
                params['car_tags'] = self.car_tags.to_alipay_dict()
            else:
                params['car_tags'] = self.car_tags
        if self.car_year:
            if hasattr(self.car_year, 'to_alipay_dict'):
                params['car_year'] = self.car_year.to_alipay_dict()
            else:
                params['car_year'] = self.car_year
        if self.check_report_data:
            if hasattr(self.check_report_data, 'to_alipay_dict'):
                params['check_report_data'] = self.check_report_data.to_alipay_dict()
            else:
                params['check_report_data'] = self.check_report_data
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.displacement:
            if hasattr(self.displacement, 'to_alipay_dict'):
                params['displacement'] = self.displacement.to_alipay_dict()
            else:
                params['displacement'] = self.displacement
        if self.drive_distance:
            if hasattr(self.drive_distance, 'to_alipay_dict'):
                params['drive_distance'] = self.drive_distance.to_alipay_dict()
            else:
                params['drive_distance'] = self.drive_distance
        if self.emission_standard:
            if hasattr(self.emission_standard, 'to_alipay_dict'):
                params['emission_standard'] = self.emission_standard.to_alipay_dict()
            else:
                params['emission_standard'] = self.emission_standard
        if self.fuel_type:
            if hasattr(self.fuel_type, 'to_alipay_dict'):
                params['fuel_type'] = self.fuel_type.to_alipay_dict()
            else:
                params['fuel_type'] = self.fuel_type
        if self.full_img_url:
            if hasattr(self.full_img_url, 'to_alipay_dict'):
                params['full_img_url'] = self.full_img_url.to_alipay_dict()
            else:
                params['full_img_url'] = self.full_img_url
        if self.highlights:
            if isinstance(self.highlights, list):
                for i in range(0, len(self.highlights)):
                    element = self.highlights[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.highlights[i] = element.to_alipay_dict()
            if hasattr(self.highlights, 'to_alipay_dict'):
                params['highlights'] = self.highlights.to_alipay_dict()
            else:
                params['highlights'] = self.highlights
        if self.images_url:
            if isinstance(self.images_url, list):
                for i in range(0, len(self.images_url)):
                    element = self.images_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images_url[i] = element.to_alipay_dict()
            if hasattr(self.images_url, 'to_alipay_dict'):
                params['images_url'] = self.images_url.to_alipay_dict()
            else:
                params['images_url'] = self.images_url
        if self.insurance_full_date:
            if hasattr(self.insurance_full_date, 'to_alipay_dict'):
                params['insurance_full_date'] = self.insurance_full_date.to_alipay_dict()
            else:
                params['insurance_full_date'] = self.insurance_full_date
        if self.isv_update_date:
            if hasattr(self.isv_update_date, 'to_alipay_dict'):
                params['isv_update_date'] = self.isv_update_date.to_alipay_dict()
            else:
                params['isv_update_date'] = self.isv_update_date
        if self.license_full_date:
            if hasattr(self.license_full_date, 'to_alipay_dict'):
                params['license_full_date'] = self.license_full_date.to_alipay_dict()
            else:
                params['license_full_date'] = self.license_full_date
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.product_date:
            if hasattr(self.product_date, 'to_alipay_dict'):
                params['product_date'] = self.product_date.to_alipay_dict()
            else:
                params['product_date'] = self.product_date
        if self.seats:
            if hasattr(self.seats, 'to_alipay_dict'):
                params['seats'] = self.seats.to_alipay_dict()
            else:
                params['seats'] = self.seats
        if self.series_name:
            if hasattr(self.series_name, 'to_alipay_dict'):
                params['series_name'] = self.series_name.to_alipay_dict()
            else:
                params['series_name'] = self.series_name
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.transfer_count:
            if hasattr(self.transfer_count, 'to_alipay_dict'):
                params['transfer_count'] = self.transfer_count.to_alipay_dict()
            else:
                params['transfer_count'] = self.transfer_count
        if self.transfer_date:
            if hasattr(self.transfer_date, 'to_alipay_dict'):
                params['transfer_date'] = self.transfer_date.to_alipay_dict()
            else:
                params['transfer_date'] = self.transfer_date
        if self.transmission_type:
            if hasattr(self.transmission_type, 'to_alipay_dict'):
                params['transmission_type'] = self.transmission_type.to_alipay_dict()
            else:
                params['transmission_type'] = self.transmission_type
        if self.vehicle_display_status:
            if hasattr(self.vehicle_display_status, 'to_alipay_dict'):
                params['vehicle_display_status'] = self.vehicle_display_status.to_alipay_dict()
            else:
                params['vehicle_display_status'] = self.vehicle_display_status
        if self.vehicle_video_url:
            if hasattr(self.vehicle_video_url, 'to_alipay_dict'):
                params['vehicle_video_url'] = self.vehicle_video_url.to_alipay_dict()
            else:
                params['vehicle_video_url'] = self.vehicle_video_url
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferCarData()
        if 'acid' in d:
            o.acid = d['acid']
        if 'activity_end_date' in d:
            o.activity_end_date = d['activity_end_date']
        if 'activity_start_date' in d:
            o.activity_start_date = d['activity_start_date']
        if 'attr_car_source_battery_owner_type' in d:
            o.attr_car_source_battery_owner_type = d['attr_car_source_battery_owner_type']
        if 'audit_full_date' in d:
            o.audit_full_date = d['audit_full_date']
        if 'auto_type' in d:
            o.auto_type = d['auto_type']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'brand_official_store' in d:
            o.brand_official_store = d['brand_official_store']
        if 'call_phone' in d:
            o.call_phone = d['call_phone']
        if 'car_color' in d:
            o.car_color = d['car_color']
        if 'car_desc' in d:
            o.car_desc = d['car_desc']
        if 'car_keys' in d:
            o.car_keys = d['car_keys']
        if 'car_online_date' in d:
            o.car_online_date = d['car_online_date']
        if 'car_source_type' in d:
            o.car_source_type = d['car_source_type']
        if 'car_tags' in d:
            o.car_tags = d['car_tags']
        if 'car_year' in d:
            o.car_year = d['car_year']
        if 'check_report_data' in d:
            o.check_report_data = d['check_report_data']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'displacement' in d:
            o.displacement = d['displacement']
        if 'drive_distance' in d:
            o.drive_distance = d['drive_distance']
        if 'emission_standard' in d:
            o.emission_standard = d['emission_standard']
        if 'fuel_type' in d:
            o.fuel_type = d['fuel_type']
        if 'full_img_url' in d:
            o.full_img_url = d['full_img_url']
        if 'highlights' in d:
            o.highlights = d['highlights']
        if 'images_url' in d:
            o.images_url = d['images_url']
        if 'insurance_full_date' in d:
            o.insurance_full_date = d['insurance_full_date']
        if 'isv_update_date' in d:
            o.isv_update_date = d['isv_update_date']
        if 'license_full_date' in d:
            o.license_full_date = d['license_full_date']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'price' in d:
            o.price = d['price']
        if 'product_date' in d:
            o.product_date = d['product_date']
        if 'seats' in d:
            o.seats = d['seats']
        if 'series_name' in d:
            o.series_name = d['series_name']
        if 'title' in d:
            o.title = d['title']
        if 'transfer_count' in d:
            o.transfer_count = d['transfer_count']
        if 'transfer_date' in d:
            o.transfer_date = d['transfer_date']
        if 'transmission_type' in d:
            o.transmission_type = d['transmission_type']
        if 'vehicle_display_status' in d:
            o.vehicle_display_status = d['vehicle_display_status']
        if 'vehicle_video_url' in d:
            o.vehicle_video_url = d['vehicle_video_url']
        if 'vin' in d:
            o.vin = d['vin']
        return o


