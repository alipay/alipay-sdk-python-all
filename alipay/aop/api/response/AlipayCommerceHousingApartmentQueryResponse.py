#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingApartmentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingApartmentQueryResponse, self).__init__()
        self._accommodation = None
        self._apartment_address = None
        self._apartment_facilities = None
        self._apartment_id = None
        self._apartment_img = None
        self._apartment_name = None
        self._apartment_services = None
        self._apartment_video = None
        self._apartment_vr = None
        self._bed_room = None
        self._business_district = None
        self._city_code = None
        self._contact_person = None
        self._contact_person_phone = None
        self._contact_persons_photo = None
        self._district_code = None
        self._elevator_to_unit_ratio = None
        self._external_id = None
        self._floor_end = None
        self._floor_start = None
        self._house_label = None
        self._house_program_id = None
        self._house_structure = None
        self._housing_type = None
        self._intentional_application = None
        self._orientation = None
        self._other = None
        self._property_description = None
        self._property_features = None
        self._property_title = None
        self._province_code = None
        self._qualification_requirements = None
        self._rent_end = None
        self._rent_start = None
        self._rent_unit = None
        self._source_company = None
        self._status = None
        self._usable_area_end = None
        self._usable_area_start = None
        self._viewing_time = None

    @property
    def accommodation(self):
        return self._accommodation

    @accommodation.setter
    def accommodation(self, value):
        if isinstance(value, list):
            self._accommodation = list()
            for i in value:
                self._accommodation.append(i)
    @property
    def apartment_address(self):
        return self._apartment_address

    @apartment_address.setter
    def apartment_address(self, value):
        self._apartment_address = value
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
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, value):
        self._apartment_id = value
    @property
    def apartment_img(self):
        return self._apartment_img

    @apartment_img.setter
    def apartment_img(self, value):
        if isinstance(value, list):
            self._apartment_img = list()
            for i in value:
                self._apartment_img.append(i)
    @property
    def apartment_name(self):
        return self._apartment_name

    @apartment_name.setter
    def apartment_name(self, value):
        self._apartment_name = value
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
    def apartment_video(self):
        return self._apartment_video

    @apartment_video.setter
    def apartment_video(self, value):
        if isinstance(value, list):
            self._apartment_video = list()
            for i in value:
                self._apartment_video.append(i)
    @property
    def apartment_vr(self):
        return self._apartment_vr

    @apartment_vr.setter
    def apartment_vr(self, value):
        self._apartment_vr = value
    @property
    def bed_room(self):
        return self._bed_room

    @bed_room.setter
    def bed_room(self, value):
        self._bed_room = value
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
    def contact_persons_photo(self):
        return self._contact_persons_photo

    @contact_persons_photo.setter
    def contact_persons_photo(self, value):
        self._contact_persons_photo = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def elevator_to_unit_ratio(self):
        return self._elevator_to_unit_ratio

    @elevator_to_unit_ratio.setter
    def elevator_to_unit_ratio(self, value):
        self._elevator_to_unit_ratio = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def floor_end(self):
        return self._floor_end

    @floor_end.setter
    def floor_end(self, value):
        self._floor_end = value
    @property
    def floor_start(self):
        return self._floor_start

    @floor_start.setter
    def floor_start(self, value):
        self._floor_start = value
    @property
    def house_label(self):
        return self._house_label

    @house_label.setter
    def house_label(self, value):
        if isinstance(value, list):
            self._house_label = list()
            for i in value:
                self._house_label.append(i)
    @property
    def house_program_id(self):
        return self._house_program_id

    @house_program_id.setter
    def house_program_id(self, value):
        self._house_program_id = value
    @property
    def house_structure(self):
        return self._house_structure

    @house_structure.setter
    def house_structure(self, value):
        self._house_structure = value
    @property
    def housing_type(self):
        return self._housing_type

    @housing_type.setter
    def housing_type(self, value):
        self._housing_type = value
    @property
    def intentional_application(self):
        return self._intentional_application

    @intentional_application.setter
    def intentional_application(self, value):
        self._intentional_application = value
    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        self._orientation = value
    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, value):
        self._other = value
    @property
    def property_description(self):
        return self._property_description

    @property_description.setter
    def property_description(self, value):
        self._property_description = value
    @property
    def property_features(self):
        return self._property_features

    @property_features.setter
    def property_features(self, value):
        if isinstance(value, list):
            self._property_features = list()
            for i in value:
                self._property_features.append(i)
    @property
    def property_title(self):
        return self._property_title

    @property_title.setter
    def property_title(self, value):
        self._property_title = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def qualification_requirements(self):
        return self._qualification_requirements

    @qualification_requirements.setter
    def qualification_requirements(self, value):
        self._qualification_requirements = value
    @property
    def rent_end(self):
        return self._rent_end

    @rent_end.setter
    def rent_end(self, value):
        self._rent_end = value
    @property
    def rent_start(self):
        return self._rent_start

    @rent_start.setter
    def rent_start(self, value):
        self._rent_start = value
    @property
    def rent_unit(self):
        return self._rent_unit

    @rent_unit.setter
    def rent_unit(self, value):
        self._rent_unit = value
    @property
    def source_company(self):
        return self._source_company

    @source_company.setter
    def source_company(self, value):
        self._source_company = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def usable_area_end(self):
        return self._usable_area_end

    @usable_area_end.setter
    def usable_area_end(self, value):
        self._usable_area_end = value
    @property
    def usable_area_start(self):
        return self._usable_area_start

    @usable_area_start.setter
    def usable_area_start(self, value):
        self._usable_area_start = value
    @property
    def viewing_time(self):
        return self._viewing_time

    @viewing_time.setter
    def viewing_time(self, value):
        if isinstance(value, list):
            self._viewing_time = list()
            for i in value:
                self._viewing_time.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingApartmentQueryResponse, self).parse_response_content(response_content)
        if 'accommodation' in response:
            self.accommodation = response['accommodation']
        if 'apartment_address' in response:
            self.apartment_address = response['apartment_address']
        if 'apartment_facilities' in response:
            self.apartment_facilities = response['apartment_facilities']
        if 'apartment_id' in response:
            self.apartment_id = response['apartment_id']
        if 'apartment_img' in response:
            self.apartment_img = response['apartment_img']
        if 'apartment_name' in response:
            self.apartment_name = response['apartment_name']
        if 'apartment_services' in response:
            self.apartment_services = response['apartment_services']
        if 'apartment_video' in response:
            self.apartment_video = response['apartment_video']
        if 'apartment_vr' in response:
            self.apartment_vr = response['apartment_vr']
        if 'bed_room' in response:
            self.bed_room = response['bed_room']
        if 'business_district' in response:
            self.business_district = response['business_district']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'contact_person' in response:
            self.contact_person = response['contact_person']
        if 'contact_person_phone' in response:
            self.contact_person_phone = response['contact_person_phone']
        if 'contact_persons_photo' in response:
            self.contact_persons_photo = response['contact_persons_photo']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'elevator_to_unit_ratio' in response:
            self.elevator_to_unit_ratio = response['elevator_to_unit_ratio']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'floor_end' in response:
            self.floor_end = response['floor_end']
        if 'floor_start' in response:
            self.floor_start = response['floor_start']
        if 'house_label' in response:
            self.house_label = response['house_label']
        if 'house_program_id' in response:
            self.house_program_id = response['house_program_id']
        if 'house_structure' in response:
            self.house_structure = response['house_structure']
        if 'housing_type' in response:
            self.housing_type = response['housing_type']
        if 'intentional_application' in response:
            self.intentional_application = response['intentional_application']
        if 'orientation' in response:
            self.orientation = response['orientation']
        if 'other' in response:
            self.other = response['other']
        if 'property_description' in response:
            self.property_description = response['property_description']
        if 'property_features' in response:
            self.property_features = response['property_features']
        if 'property_title' in response:
            self.property_title = response['property_title']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'qualification_requirements' in response:
            self.qualification_requirements = response['qualification_requirements']
        if 'rent_end' in response:
            self.rent_end = response['rent_end']
        if 'rent_start' in response:
            self.rent_start = response['rent_start']
        if 'rent_unit' in response:
            self.rent_unit = response['rent_unit']
        if 'source_company' in response:
            self.source_company = response['source_company']
        if 'status' in response:
            self.status = response['status']
        if 'usable_area_end' in response:
            self.usable_area_end = response['usable_area_end']
        if 'usable_area_start' in response:
            self.usable_area_start = response['usable_area_start']
        if 'viewing_time' in response:
            self.viewing_time = response['viewing_time']
