#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingCommunityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingCommunityQueryResponse, self).__init__()
        self._apartment_facilities = None
        self._apartment_services = None
        self._avg_price = None
        self._business_district = None
        self._city_code = None
        self._closed_community = None
        self._community_address = None
        self._community_alias = None
        self._community_id = None
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
    def avg_price(self):
        return self._avg_price

    @avg_price.setter
    def avg_price(self, value):
        self._avg_price = value
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
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingCommunityQueryResponse, self).parse_response_content(response_content)
        if 'apartment_facilities' in response:
            self.apartment_facilities = response['apartment_facilities']
        if 'apartment_services' in response:
            self.apartment_services = response['apartment_services']
        if 'avg_price' in response:
            self.avg_price = response['avg_price']
        if 'business_district' in response:
            self.business_district = response['business_district']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'closed_community' in response:
            self.closed_community = response['closed_community']
        if 'community_address' in response:
            self.community_address = response['community_address']
        if 'community_alias' in response:
            self.community_alias = response['community_alias']
        if 'community_id' in response:
            self.community_id = response['community_id']
        if 'community_img' in response:
            self.community_img = response['community_img']
        if 'community_label' in response:
            self.community_label = response['community_label']
        if 'community_name' in response:
            self.community_name = response['community_name']
        if 'community_reviews' in response:
            self.community_reviews = response['community_reviews']
        if 'community_status' in response:
            self.community_status = response['community_status']
        if 'community_type' in response:
            self.community_type = response['community_type']
        if 'community_video' in response:
            self.community_video = response['community_video']
        if 'construction_year' in response:
            self.construction_year = response['construction_year']
        if 'contact_person' in response:
            self.contact_person = response['contact_person']
        if 'contact_person_phone' in response:
            self.contact_person_phone = response['contact_person_phone']
        if 'development_company' in response:
            self.development_company = response['development_company']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'electricity_type' in response:
            self.electricity_type = response['electricity_type']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'floor_area_ratio' in response:
            self.floor_area_ratio = response['floor_area_ratio']
        if 'gas_fee' in response:
            self.gas_fee = response['gas_fee']
        if 'greenery_ratio' in response:
            self.greenery_ratio = response['greenery_ratio']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'pedestrian_vehicle_separation' in response:
            self.pedestrian_vehicle_separation = response['pedestrian_vehicle_separation']
        if 'property_management_company' in response:
            self.property_management_company = response['property_management_company']
        if 'property_management_fee' in response:
            self.property_management_fee = response['property_management_fee']
        if 'property_right_year' in response:
            self.property_right_year = response['property_right_year']
        if 'property_type' in response:
            self.property_type = response['property_type']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'sum_buildings' in response:
            self.sum_buildings = response['sum_buildings']
        if 'sum_units' in response:
            self.sum_units = response['sum_units']
        if 'supply_company' in response:
            self.supply_company = response['supply_company']
        if 'vehicle_unit_ratio' in response:
            self.vehicle_unit_ratio = response['vehicle_unit_ratio']
        if 'water_type' in response:
            self.water_type = response['water_type']
