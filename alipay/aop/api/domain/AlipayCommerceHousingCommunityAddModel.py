#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingCommunityAddModel(object):

    def __init__(self):
        self._apartment_facilities = None
        self._apartment_services = None
        self._business_district = None
        self._city_code = None
        self._closed_community = None
        self._community_address = None
        self._community_alias = None
        self._community_img = None
        self._community_label = None
        self._community_name = None
        self._community_reviews = None
        self._community_status = None
        self._community_type = None
        self._community_video = None
        self._construction_year = None
        self._contact_person = None
        self._contact_person_phone = None
        self._development_company = None
        self._district_code = None
        self._electricity_type = None
        self._external_id = None
        self._floor_area_ratio = None
        self._gas_fee = None
        self._greenery_ratio = None
        self._latitude = None
        self._longitude = None
        self._pedestrian_vehicle_separation = None
        self._property_management_company = None
        self._property_management_fee = None
        self._property_right_year = None
        self._property_type = None
        self._province_code = None
        self._sum_buildings = None
        self._sum_units = None
        self._supply_company = None
        self._vehicle_unit_ratio = None
        self._water_type = None

    @property
    def apartment_facilities(self):
        return self._apartment_facilities

    @apartment_facilities.setter
    def apartment_facilities(self, value):
        if isinstance(value, list):
            self._apartment_facilities = list()
            for i in value:
                self._apartment_facilities.append(i)
    @property
    def apartment_services(self):
        return self._apartment_services

    @apartment_services.setter
    def apartment_services(self, value):
        if isinstance(value, list):
            self._apartment_services = list()
            for i in value:
                self._apartment_services.append(i)
    @property
    def business_district(self):
        return self._business_district

    @business_district.setter
    def business_district(self, value):
        self._business_district = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def closed_community(self):
        return self._closed_community

    @closed_community.setter
    def closed_community(self, value):
        self._closed_community = value
    @property
    def community_address(self):
        return self._community_address

    @community_address.setter
    def community_address(self, value):
        self._community_address = value
    @property
    def community_alias(self):
        return self._community_alias

    @community_alias.setter
    def community_alias(self, value):
        self._community_alias = value
    @property
    def community_img(self):
        return self._community_img

    @community_img.setter
    def community_img(self, value):
        if isinstance(value, list):
            self._community_img = list()
            for i in value:
                self._community_img.append(i)
    @property
    def community_label(self):
        return self._community_label

    @community_label.setter
    def community_label(self, value):
        if isinstance(value, list):
            self._community_label = list()
            for i in value:
                self._community_label.append(i)
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def community_reviews(self):
        return self._community_reviews

    @community_reviews.setter
    def community_reviews(self, value):
        self._community_reviews = value
    @property
    def community_status(self):
        return self._community_status

    @community_status.setter
    def community_status(self, value):
        self._community_status = value
    @property
    def community_type(self):
        return self._community_type

    @community_type.setter
    def community_type(self, value):
        self._community_type = value
    @property
    def community_video(self):
        return self._community_video

    @community_video.setter
    def community_video(self, value):
        if isinstance(value, list):
            self._community_video = list()
            for i in value:
                self._community_video.append(i)
    @property
    def construction_year(self):
        return self._construction_year

    @construction_year.setter
    def construction_year(self, value):
        self._construction_year = value
    @property
    def contact_person(self):
        return self._contact_person

    @contact_person.setter
    def contact_person(self, value):
        self._contact_person = value
    @property
    def contact_person_phone(self):
        return self._contact_person_phone

    @contact_person_phone.setter
    def contact_person_phone(self, value):
        self._contact_person_phone = value
    @property
    def development_company(self):
        return self._development_company

    @development_company.setter
    def development_company(self, value):
        self._development_company = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def electricity_type(self):
        return self._electricity_type

    @electricity_type.setter
    def electricity_type(self, value):
        self._electricity_type = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def floor_area_ratio(self):
        return self._floor_area_ratio

    @floor_area_ratio.setter
    def floor_area_ratio(self, value):
        self._floor_area_ratio = value
    @property
    def gas_fee(self):
        return self._gas_fee

    @gas_fee.setter
    def gas_fee(self, value):
        self._gas_fee = value
    @property
    def greenery_ratio(self):
        return self._greenery_ratio

    @greenery_ratio.setter
    def greenery_ratio(self, value):
        self._greenery_ratio = value
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
    def pedestrian_vehicle_separation(self):
        return self._pedestrian_vehicle_separation

    @pedestrian_vehicle_separation.setter
    def pedestrian_vehicle_separation(self, value):
        self._pedestrian_vehicle_separation = value
    @property
    def property_management_company(self):
        return self._property_management_company

    @property_management_company.setter
    def property_management_company(self, value):
        self._property_management_company = value
    @property
    def property_management_fee(self):
        return self._property_management_fee

    @property_management_fee.setter
    def property_management_fee(self, value):
        self._property_management_fee = value
    @property
    def property_right_year(self):
        return self._property_right_year

    @property_right_year.setter
    def property_right_year(self, value):
        self._property_right_year = value
    @property
    def property_type(self):
        return self._property_type

    @property_type.setter
    def property_type(self, value):
        self._property_type = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def sum_buildings(self):
        return self._sum_buildings

    @sum_buildings.setter
    def sum_buildings(self, value):
        self._sum_buildings = value
    @property
    def sum_units(self):
        return self._sum_units

    @sum_units.setter
    def sum_units(self, value):
        self._sum_units = value
    @property
    def supply_company(self):
        return self._supply_company

    @supply_company.setter
    def supply_company(self, value):
        self._supply_company = value
    @property
    def vehicle_unit_ratio(self):
        return self._vehicle_unit_ratio

    @vehicle_unit_ratio.setter
    def vehicle_unit_ratio(self, value):
        self._vehicle_unit_ratio = value
    @property
    def water_type(self):
        return self._water_type

    @water_type.setter
    def water_type(self, value):
        self._water_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apartment_facilities:
            if isinstance(self.apartment_facilities, list):
                for i in range(0, len(self.apartment_facilities)):
                    element = self.apartment_facilities[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apartment_facilities[i] = element.to_alipay_dict()
            if hasattr(self.apartment_facilities, 'to_alipay_dict'):
                params['apartment_facilities'] = self.apartment_facilities.to_alipay_dict()
            else:
                params['apartment_facilities'] = self.apartment_facilities
        if self.apartment_services:
            if isinstance(self.apartment_services, list):
                for i in range(0, len(self.apartment_services)):
                    element = self.apartment_services[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apartment_services[i] = element.to_alipay_dict()
            if hasattr(self.apartment_services, 'to_alipay_dict'):
                params['apartment_services'] = self.apartment_services.to_alipay_dict()
            else:
                params['apartment_services'] = self.apartment_services
        if self.business_district:
            if hasattr(self.business_district, 'to_alipay_dict'):
                params['business_district'] = self.business_district.to_alipay_dict()
            else:
                params['business_district'] = self.business_district
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.closed_community:
            if hasattr(self.closed_community, 'to_alipay_dict'):
                params['closed_community'] = self.closed_community.to_alipay_dict()
            else:
                params['closed_community'] = self.closed_community
        if self.community_address:
            if hasattr(self.community_address, 'to_alipay_dict'):
                params['community_address'] = self.community_address.to_alipay_dict()
            else:
                params['community_address'] = self.community_address
        if self.community_alias:
            if hasattr(self.community_alias, 'to_alipay_dict'):
                params['community_alias'] = self.community_alias.to_alipay_dict()
            else:
                params['community_alias'] = self.community_alias
        if self.community_img:
            if isinstance(self.community_img, list):
                for i in range(0, len(self.community_img)):
                    element = self.community_img[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.community_img[i] = element.to_alipay_dict()
            if hasattr(self.community_img, 'to_alipay_dict'):
                params['community_img'] = self.community_img.to_alipay_dict()
            else:
                params['community_img'] = self.community_img
        if self.community_label:
            if isinstance(self.community_label, list):
                for i in range(0, len(self.community_label)):
                    element = self.community_label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.community_label[i] = element.to_alipay_dict()
            if hasattr(self.community_label, 'to_alipay_dict'):
                params['community_label'] = self.community_label.to_alipay_dict()
            else:
                params['community_label'] = self.community_label
        if self.community_name:
            if hasattr(self.community_name, 'to_alipay_dict'):
                params['community_name'] = self.community_name.to_alipay_dict()
            else:
                params['community_name'] = self.community_name
        if self.community_reviews:
            if hasattr(self.community_reviews, 'to_alipay_dict'):
                params['community_reviews'] = self.community_reviews.to_alipay_dict()
            else:
                params['community_reviews'] = self.community_reviews
        if self.community_status:
            if hasattr(self.community_status, 'to_alipay_dict'):
                params['community_status'] = self.community_status.to_alipay_dict()
            else:
                params['community_status'] = self.community_status
        if self.community_type:
            if hasattr(self.community_type, 'to_alipay_dict'):
                params['community_type'] = self.community_type.to_alipay_dict()
            else:
                params['community_type'] = self.community_type
        if self.community_video:
            if isinstance(self.community_video, list):
                for i in range(0, len(self.community_video)):
                    element = self.community_video[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.community_video[i] = element.to_alipay_dict()
            if hasattr(self.community_video, 'to_alipay_dict'):
                params['community_video'] = self.community_video.to_alipay_dict()
            else:
                params['community_video'] = self.community_video
        if self.construction_year:
            if hasattr(self.construction_year, 'to_alipay_dict'):
                params['construction_year'] = self.construction_year.to_alipay_dict()
            else:
                params['construction_year'] = self.construction_year
        if self.contact_person:
            if hasattr(self.contact_person, 'to_alipay_dict'):
                params['contact_person'] = self.contact_person.to_alipay_dict()
            else:
                params['contact_person'] = self.contact_person
        if self.contact_person_phone:
            if hasattr(self.contact_person_phone, 'to_alipay_dict'):
                params['contact_person_phone'] = self.contact_person_phone.to_alipay_dict()
            else:
                params['contact_person_phone'] = self.contact_person_phone
        if self.development_company:
            if hasattr(self.development_company, 'to_alipay_dict'):
                params['development_company'] = self.development_company.to_alipay_dict()
            else:
                params['development_company'] = self.development_company
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.electricity_type:
            if hasattr(self.electricity_type, 'to_alipay_dict'):
                params['electricity_type'] = self.electricity_type.to_alipay_dict()
            else:
                params['electricity_type'] = self.electricity_type
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.floor_area_ratio:
            if hasattr(self.floor_area_ratio, 'to_alipay_dict'):
                params['floor_area_ratio'] = self.floor_area_ratio.to_alipay_dict()
            else:
                params['floor_area_ratio'] = self.floor_area_ratio
        if self.gas_fee:
            if hasattr(self.gas_fee, 'to_alipay_dict'):
                params['gas_fee'] = self.gas_fee.to_alipay_dict()
            else:
                params['gas_fee'] = self.gas_fee
        if self.greenery_ratio:
            if hasattr(self.greenery_ratio, 'to_alipay_dict'):
                params['greenery_ratio'] = self.greenery_ratio.to_alipay_dict()
            else:
                params['greenery_ratio'] = self.greenery_ratio
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
        if self.pedestrian_vehicle_separation:
            if hasattr(self.pedestrian_vehicle_separation, 'to_alipay_dict'):
                params['pedestrian_vehicle_separation'] = self.pedestrian_vehicle_separation.to_alipay_dict()
            else:
                params['pedestrian_vehicle_separation'] = self.pedestrian_vehicle_separation
        if self.property_management_company:
            if hasattr(self.property_management_company, 'to_alipay_dict'):
                params['property_management_company'] = self.property_management_company.to_alipay_dict()
            else:
                params['property_management_company'] = self.property_management_company
        if self.property_management_fee:
            if hasattr(self.property_management_fee, 'to_alipay_dict'):
                params['property_management_fee'] = self.property_management_fee.to_alipay_dict()
            else:
                params['property_management_fee'] = self.property_management_fee
        if self.property_right_year:
            if hasattr(self.property_right_year, 'to_alipay_dict'):
                params['property_right_year'] = self.property_right_year.to_alipay_dict()
            else:
                params['property_right_year'] = self.property_right_year
        if self.property_type:
            if hasattr(self.property_type, 'to_alipay_dict'):
                params['property_type'] = self.property_type.to_alipay_dict()
            else:
                params['property_type'] = self.property_type
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.sum_buildings:
            if hasattr(self.sum_buildings, 'to_alipay_dict'):
                params['sum_buildings'] = self.sum_buildings.to_alipay_dict()
            else:
                params['sum_buildings'] = self.sum_buildings
        if self.sum_units:
            if hasattr(self.sum_units, 'to_alipay_dict'):
                params['sum_units'] = self.sum_units.to_alipay_dict()
            else:
                params['sum_units'] = self.sum_units
        if self.supply_company:
            if hasattr(self.supply_company, 'to_alipay_dict'):
                params['supply_company'] = self.supply_company.to_alipay_dict()
            else:
                params['supply_company'] = self.supply_company
        if self.vehicle_unit_ratio:
            if hasattr(self.vehicle_unit_ratio, 'to_alipay_dict'):
                params['vehicle_unit_ratio'] = self.vehicle_unit_ratio.to_alipay_dict()
            else:
                params['vehicle_unit_ratio'] = self.vehicle_unit_ratio
        if self.water_type:
            if hasattr(self.water_type, 'to_alipay_dict'):
                params['water_type'] = self.water_type.to_alipay_dict()
            else:
                params['water_type'] = self.water_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHousingCommunityAddModel()
        if 'apartment_facilities' in d:
            o.apartment_facilities = d['apartment_facilities']
        if 'apartment_services' in d:
            o.apartment_services = d['apartment_services']
        if 'business_district' in d:
            o.business_district = d['business_district']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'closed_community' in d:
            o.closed_community = d['closed_community']
        if 'community_address' in d:
            o.community_address = d['community_address']
        if 'community_alias' in d:
            o.community_alias = d['community_alias']
        if 'community_img' in d:
            o.community_img = d['community_img']
        if 'community_label' in d:
            o.community_label = d['community_label']
        if 'community_name' in d:
            o.community_name = d['community_name']
        if 'community_reviews' in d:
            o.community_reviews = d['community_reviews']
        if 'community_status' in d:
            o.community_status = d['community_status']
        if 'community_type' in d:
            o.community_type = d['community_type']
        if 'community_video' in d:
            o.community_video = d['community_video']
        if 'construction_year' in d:
            o.construction_year = d['construction_year']
        if 'contact_person' in d:
            o.contact_person = d['contact_person']
        if 'contact_person_phone' in d:
            o.contact_person_phone = d['contact_person_phone']
        if 'development_company' in d:
            o.development_company = d['development_company']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'electricity_type' in d:
            o.electricity_type = d['electricity_type']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'floor_area_ratio' in d:
            o.floor_area_ratio = d['floor_area_ratio']
        if 'gas_fee' in d:
            o.gas_fee = d['gas_fee']
        if 'greenery_ratio' in d:
            o.greenery_ratio = d['greenery_ratio']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'pedestrian_vehicle_separation' in d:
            o.pedestrian_vehicle_separation = d['pedestrian_vehicle_separation']
        if 'property_management_company' in d:
            o.property_management_company = d['property_management_company']
        if 'property_management_fee' in d:
            o.property_management_fee = d['property_management_fee']
        if 'property_right_year' in d:
            o.property_right_year = d['property_right_year']
        if 'property_type' in d:
            o.property_type = d['property_type']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'sum_buildings' in d:
            o.sum_buildings = d['sum_buildings']
        if 'sum_units' in d:
            o.sum_units = d['sum_units']
        if 'supply_company' in d:
            o.supply_company = d['supply_company']
        if 'vehicle_unit_ratio' in d:
            o.vehicle_unit_ratio = d['vehicle_unit_ratio']
        if 'water_type' in d:
            o.water_type = d['water_type']
        return o


