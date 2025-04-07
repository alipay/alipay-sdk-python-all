#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingHouseRentalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingHouseRentalQueryResponse, self).__init__()
        self._accommodation = None
        self._bath_room = None
        self._bed_room = None
        self._building_category = None
        self._check_in_time = None
        self._community_id = None
        self._constructed_area = None
        self._construction_year = None
        self._contact_person = None
        self._contact_person_phone = None
        self._contact_persons_photo = None
        self._current_condition_house = None
        self._deposit = None
        self._doorplate_number = None
        self._elevator = None
        self._elevator_to_unit_ratio = None
        self._external_id = None
        self._floor_level = None
        self._floor_range = None
        self._has_private_bathroom = None
        self._house_label = None
        self._house_pic = None
        self._house_program_id = None
        self._house_structure = None
        self._house_video = None
        self._house_vr_url = None
        self._housing_id = None
        self._housing_type = None
        self._internal_area = None
        self._kitchen = None
        self._listing_date = None
        self._living_room = None
        self._orientation = None
        self._other = None
        self._owner_id = None
        self._owner_name = None
        self._parking_space = None
        self._payment_method = None
        self._power_of_attorney = None
        self._property_description = None
        self._property_features = None
        self._property_rights = None
        self._property_title = None
        self._renovation = None
        self._rent = None
        self._rent_unit = None
        self._rental_requirements = None
        self._rented_room = None
        self._renting_type = None
        self._source_company = None
        self._status = None
        self._total_floors = None
        self._verification_code = None
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
    def bath_room(self):
        return self._bath_room

    @bath_room.setter
    def bath_room(self, value):
        self._bath_room = value
    @property
    def bed_room(self):
        return self._bed_room

    @bed_room.setter
    def bed_room(self, value):
        self._bed_room = value
    @property
    def building_category(self):
        return self._building_category

    @building_category.setter
    def building_category(self, value):
        self._building_category = value
    @property
    def check_in_time(self):
        return self._check_in_time

    @check_in_time.setter
    def check_in_time(self, value):
        self._check_in_time = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def constructed_area(self):
        return self._constructed_area

    @constructed_area.setter
    def constructed_area(self, value):
        self._constructed_area = value
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
    def contact_persons_photo(self):
        return self._contact_persons_photo

    @contact_persons_photo.setter
    def contact_persons_photo(self, value):
        self._contact_persons_photo = value
    @property
    def current_condition_house(self):
        return self._current_condition_house

    @current_condition_house.setter
    def current_condition_house(self, value):
        self._current_condition_house = value
    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, value):
        self._deposit = value
    @property
    def doorplate_number(self):
        return self._doorplate_number

    @doorplate_number.setter
    def doorplate_number(self, value):
        self._doorplate_number = value
    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, value):
        self._elevator = value
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
    def floor_level(self):
        return self._floor_level

    @floor_level.setter
    def floor_level(self, value):
        self._floor_level = value
    @property
    def floor_range(self):
        return self._floor_range

    @floor_range.setter
    def floor_range(self, value):
        self._floor_range = value
    @property
    def has_private_bathroom(self):
        return self._has_private_bathroom

    @has_private_bathroom.setter
    def has_private_bathroom(self, value):
        self._has_private_bathroom = value
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
    def house_pic(self):
        return self._house_pic

    @house_pic.setter
    def house_pic(self, value):
        if isinstance(value, list):
            self._house_pic = list()
            for i in value:
                self._house_pic.append(i)
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
    def house_video(self):
        return self._house_video

    @house_video.setter
    def house_video(self, value):
        if isinstance(value, list):
            self._house_video = list()
            for i in value:
                self._house_video.append(i)
    @property
    def house_vr_url(self):
        return self._house_vr_url

    @house_vr_url.setter
    def house_vr_url(self, value):
        self._house_vr_url = value
    @property
    def housing_id(self):
        return self._housing_id

    @housing_id.setter
    def housing_id(self, value):
        self._housing_id = value
    @property
    def housing_type(self):
        return self._housing_type

    @housing_type.setter
    def housing_type(self, value):
        self._housing_type = value
    @property
    def internal_area(self):
        return self._internal_area

    @internal_area.setter
    def internal_area(self, value):
        self._internal_area = value
    @property
    def kitchen(self):
        return self._kitchen

    @kitchen.setter
    def kitchen(self, value):
        self._kitchen = value
    @property
    def listing_date(self):
        return self._listing_date

    @listing_date.setter
    def listing_date(self, value):
        self._listing_date = value
    @property
    def living_room(self):
        return self._living_room

    @living_room.setter
    def living_room(self, value):
        self._living_room = value
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
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def parking_space(self):
        return self._parking_space

    @parking_space.setter
    def parking_space(self, value):
        self._parking_space = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def power_of_attorney(self):
        return self._power_of_attorney

    @power_of_attorney.setter
    def power_of_attorney(self, value):
        self._power_of_attorney = value
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
    def property_rights(self):
        return self._property_rights

    @property_rights.setter
    def property_rights(self, value):
        self._property_rights = value
    @property
    def property_title(self):
        return self._property_title

    @property_title.setter
    def property_title(self, value):
        self._property_title = value
    @property
    def renovation(self):
        return self._renovation

    @renovation.setter
    def renovation(self, value):
        self._renovation = value
    @property
    def rent(self):
        return self._rent

    @rent.setter
    def rent(self, value):
        self._rent = value
    @property
    def rent_unit(self):
        return self._rent_unit

    @rent_unit.setter
    def rent_unit(self, value):
        self._rent_unit = value
    @property
    def rental_requirements(self):
        return self._rental_requirements

    @rental_requirements.setter
    def rental_requirements(self, value):
        if isinstance(value, list):
            self._rental_requirements = list()
            for i in value:
                self._rental_requirements.append(i)
    @property
    def rented_room(self):
        return self._rented_room

    @rented_room.setter
    def rented_room(self, value):
        self._rented_room = value
    @property
    def renting_type(self):
        return self._renting_type

    @renting_type.setter
    def renting_type(self, value):
        self._renting_type = value
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
    def total_floors(self):
        return self._total_floors

    @total_floors.setter
    def total_floors(self, value):
        self._total_floors = value
    @property
    def verification_code(self):
        return self._verification_code

    @verification_code.setter
    def verification_code(self, value):
        self._verification_code = value
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
        response = super(AlipayCommerceHousingHouseRentalQueryResponse, self).parse_response_content(response_content)
        if 'accommodation' in response:
            self.accommodation = response['accommodation']
        if 'bath_room' in response:
            self.bath_room = response['bath_room']
        if 'bed_room' in response:
            self.bed_room = response['bed_room']
        if 'building_category' in response:
            self.building_category = response['building_category']
        if 'check_in_time' in response:
            self.check_in_time = response['check_in_time']
        if 'community_id' in response:
            self.community_id = response['community_id']
        if 'constructed_area' in response:
            self.constructed_area = response['constructed_area']
        if 'construction_year' in response:
            self.construction_year = response['construction_year']
        if 'contact_person' in response:
            self.contact_person = response['contact_person']
        if 'contact_person_phone' in response:
            self.contact_person_phone = response['contact_person_phone']
        if 'contact_persons_photo' in response:
            self.contact_persons_photo = response['contact_persons_photo']
        if 'current_condition_house' in response:
            self.current_condition_house = response['current_condition_house']
        if 'deposit' in response:
            self.deposit = response['deposit']
        if 'doorplate_number' in response:
            self.doorplate_number = response['doorplate_number']
        if 'elevator' in response:
            self.elevator = response['elevator']
        if 'elevator_to_unit_ratio' in response:
            self.elevator_to_unit_ratio = response['elevator_to_unit_ratio']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'floor_level' in response:
            self.floor_level = response['floor_level']
        if 'floor_range' in response:
            self.floor_range = response['floor_range']
        if 'has_private_bathroom' in response:
            self.has_private_bathroom = response['has_private_bathroom']
        if 'house_label' in response:
            self.house_label = response['house_label']
        if 'house_pic' in response:
            self.house_pic = response['house_pic']
        if 'house_program_id' in response:
            self.house_program_id = response['house_program_id']
        if 'house_structure' in response:
            self.house_structure = response['house_structure']
        if 'house_video' in response:
            self.house_video = response['house_video']
        if 'house_vr_url' in response:
            self.house_vr_url = response['house_vr_url']
        if 'housing_id' in response:
            self.housing_id = response['housing_id']
        if 'housing_type' in response:
            self.housing_type = response['housing_type']
        if 'internal_area' in response:
            self.internal_area = response['internal_area']
        if 'kitchen' in response:
            self.kitchen = response['kitchen']
        if 'listing_date' in response:
            self.listing_date = response['listing_date']
        if 'living_room' in response:
            self.living_room = response['living_room']
        if 'orientation' in response:
            self.orientation = response['orientation']
        if 'other' in response:
            self.other = response['other']
        if 'owner_id' in response:
            self.owner_id = response['owner_id']
        if 'owner_name' in response:
            self.owner_name = response['owner_name']
        if 'parking_space' in response:
            self.parking_space = response['parking_space']
        if 'payment_method' in response:
            self.payment_method = response['payment_method']
        if 'power_of_attorney' in response:
            self.power_of_attorney = response['power_of_attorney']
        if 'property_description' in response:
            self.property_description = response['property_description']
        if 'property_features' in response:
            self.property_features = response['property_features']
        if 'property_rights' in response:
            self.property_rights = response['property_rights']
        if 'property_title' in response:
            self.property_title = response['property_title']
        if 'renovation' in response:
            self.renovation = response['renovation']
        if 'rent' in response:
            self.rent = response['rent']
        if 'rent_unit' in response:
            self.rent_unit = response['rent_unit']
        if 'rental_requirements' in response:
            self.rental_requirements = response['rental_requirements']
        if 'rented_room' in response:
            self.rented_room = response['rented_room']
        if 'renting_type' in response:
            self.renting_type = response['renting_type']
        if 'source_company' in response:
            self.source_company = response['source_company']
        if 'status' in response:
            self.status = response['status']
        if 'total_floors' in response:
            self.total_floors = response['total_floors']
        if 'verification_code' in response:
            self.verification_code = response['verification_code']
        if 'viewing_time' in response:
            self.viewing_time = response['viewing_time']
