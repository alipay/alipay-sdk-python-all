#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingHouseRentalModifyModel(object):

    def __init__(self):
        self._accommodation = None
        self._building_category = None
        self._check_in_time = None
        self._community_id = None
        self._constructed_area = None
        self._contact_person = None
        self._contact_person_phone = None
        self._contact_persons_photo = None
        self._current_condition_house = None
        self._deposit = None
        self._elevator = None
        self._elevator_to_unit_ratio = None
        self._floor_level = None
        self._floor_range = None
        self._has_private_bathroom = None
        self._house_label = None
        self._house_pic = None
        self._house_structure = None
        self._house_video = None
        self._house_vr_url = None
        self._housing_id = None
        self._housing_type = None
        self._internal_area = None
        self._listing_date = None
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
    def listing_date(self):
        return self._listing_date

    @listing_date.setter
    def listing_date(self, value):
        self._listing_date = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.accommodation:
            if isinstance(self.accommodation, list):
                for i in range(0, len(self.accommodation)):
                    element = self.accommodation[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.accommodation[i] = element.to_alipay_dict()
            if hasattr(self.accommodation, 'to_alipay_dict'):
                params['accommodation'] = self.accommodation.to_alipay_dict()
            else:
                params['accommodation'] = self.accommodation
        if self.building_category:
            if hasattr(self.building_category, 'to_alipay_dict'):
                params['building_category'] = self.building_category.to_alipay_dict()
            else:
                params['building_category'] = self.building_category
        if self.check_in_time:
            if hasattr(self.check_in_time, 'to_alipay_dict'):
                params['check_in_time'] = self.check_in_time.to_alipay_dict()
            else:
                params['check_in_time'] = self.check_in_time
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.constructed_area:
            if hasattr(self.constructed_area, 'to_alipay_dict'):
                params['constructed_area'] = self.constructed_area.to_alipay_dict()
            else:
                params['constructed_area'] = self.constructed_area
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
        if self.contact_persons_photo:
            if hasattr(self.contact_persons_photo, 'to_alipay_dict'):
                params['contact_persons_photo'] = self.contact_persons_photo.to_alipay_dict()
            else:
                params['contact_persons_photo'] = self.contact_persons_photo
        if self.current_condition_house:
            if hasattr(self.current_condition_house, 'to_alipay_dict'):
                params['current_condition_house'] = self.current_condition_house.to_alipay_dict()
            else:
                params['current_condition_house'] = self.current_condition_house
        if self.deposit:
            if hasattr(self.deposit, 'to_alipay_dict'):
                params['deposit'] = self.deposit.to_alipay_dict()
            else:
                params['deposit'] = self.deposit
        if self.elevator:
            if hasattr(self.elevator, 'to_alipay_dict'):
                params['elevator'] = self.elevator.to_alipay_dict()
            else:
                params['elevator'] = self.elevator
        if self.elevator_to_unit_ratio:
            if hasattr(self.elevator_to_unit_ratio, 'to_alipay_dict'):
                params['elevator_to_unit_ratio'] = self.elevator_to_unit_ratio.to_alipay_dict()
            else:
                params['elevator_to_unit_ratio'] = self.elevator_to_unit_ratio
        if self.floor_level:
            if hasattr(self.floor_level, 'to_alipay_dict'):
                params['floor_level'] = self.floor_level.to_alipay_dict()
            else:
                params['floor_level'] = self.floor_level
        if self.floor_range:
            if hasattr(self.floor_range, 'to_alipay_dict'):
                params['floor_range'] = self.floor_range.to_alipay_dict()
            else:
                params['floor_range'] = self.floor_range
        if self.has_private_bathroom:
            if hasattr(self.has_private_bathroom, 'to_alipay_dict'):
                params['has_private_bathroom'] = self.has_private_bathroom.to_alipay_dict()
            else:
                params['has_private_bathroom'] = self.has_private_bathroom
        if self.house_label:
            if isinstance(self.house_label, list):
                for i in range(0, len(self.house_label)):
                    element = self.house_label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.house_label[i] = element.to_alipay_dict()
            if hasattr(self.house_label, 'to_alipay_dict'):
                params['house_label'] = self.house_label.to_alipay_dict()
            else:
                params['house_label'] = self.house_label
        if self.house_pic:
            if isinstance(self.house_pic, list):
                for i in range(0, len(self.house_pic)):
                    element = self.house_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.house_pic[i] = element.to_alipay_dict()
            if hasattr(self.house_pic, 'to_alipay_dict'):
                params['house_pic'] = self.house_pic.to_alipay_dict()
            else:
                params['house_pic'] = self.house_pic
        if self.house_structure:
            if hasattr(self.house_structure, 'to_alipay_dict'):
                params['house_structure'] = self.house_structure.to_alipay_dict()
            else:
                params['house_structure'] = self.house_structure
        if self.house_video:
            if isinstance(self.house_video, list):
                for i in range(0, len(self.house_video)):
                    element = self.house_video[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.house_video[i] = element.to_alipay_dict()
            if hasattr(self.house_video, 'to_alipay_dict'):
                params['house_video'] = self.house_video.to_alipay_dict()
            else:
                params['house_video'] = self.house_video
        if self.house_vr_url:
            if hasattr(self.house_vr_url, 'to_alipay_dict'):
                params['house_vr_url'] = self.house_vr_url.to_alipay_dict()
            else:
                params['house_vr_url'] = self.house_vr_url
        if self.housing_id:
            if hasattr(self.housing_id, 'to_alipay_dict'):
                params['housing_id'] = self.housing_id.to_alipay_dict()
            else:
                params['housing_id'] = self.housing_id
        if self.housing_type:
            if hasattr(self.housing_type, 'to_alipay_dict'):
                params['housing_type'] = self.housing_type.to_alipay_dict()
            else:
                params['housing_type'] = self.housing_type
        if self.internal_area:
            if hasattr(self.internal_area, 'to_alipay_dict'):
                params['internal_area'] = self.internal_area.to_alipay_dict()
            else:
                params['internal_area'] = self.internal_area
        if self.listing_date:
            if hasattr(self.listing_date, 'to_alipay_dict'):
                params['listing_date'] = self.listing_date.to_alipay_dict()
            else:
                params['listing_date'] = self.listing_date
        if self.orientation:
            if hasattr(self.orientation, 'to_alipay_dict'):
                params['orientation'] = self.orientation.to_alipay_dict()
            else:
                params['orientation'] = self.orientation
        if self.other:
            if hasattr(self.other, 'to_alipay_dict'):
                params['other'] = self.other.to_alipay_dict()
            else:
                params['other'] = self.other
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.parking_space:
            if hasattr(self.parking_space, 'to_alipay_dict'):
                params['parking_space'] = self.parking_space.to_alipay_dict()
            else:
                params['parking_space'] = self.parking_space
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.power_of_attorney:
            if hasattr(self.power_of_attorney, 'to_alipay_dict'):
                params['power_of_attorney'] = self.power_of_attorney.to_alipay_dict()
            else:
                params['power_of_attorney'] = self.power_of_attorney
        if self.property_description:
            if hasattr(self.property_description, 'to_alipay_dict'):
                params['property_description'] = self.property_description.to_alipay_dict()
            else:
                params['property_description'] = self.property_description
        if self.property_features:
            if isinstance(self.property_features, list):
                for i in range(0, len(self.property_features)):
                    element = self.property_features[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_features[i] = element.to_alipay_dict()
            if hasattr(self.property_features, 'to_alipay_dict'):
                params['property_features'] = self.property_features.to_alipay_dict()
            else:
                params['property_features'] = self.property_features
        if self.property_rights:
            if hasattr(self.property_rights, 'to_alipay_dict'):
                params['property_rights'] = self.property_rights.to_alipay_dict()
            else:
                params['property_rights'] = self.property_rights
        if self.property_title:
            if hasattr(self.property_title, 'to_alipay_dict'):
                params['property_title'] = self.property_title.to_alipay_dict()
            else:
                params['property_title'] = self.property_title
        if self.renovation:
            if hasattr(self.renovation, 'to_alipay_dict'):
                params['renovation'] = self.renovation.to_alipay_dict()
            else:
                params['renovation'] = self.renovation
        if self.rent:
            if hasattr(self.rent, 'to_alipay_dict'):
                params['rent'] = self.rent.to_alipay_dict()
            else:
                params['rent'] = self.rent
        if self.rent_unit:
            if hasattr(self.rent_unit, 'to_alipay_dict'):
                params['rent_unit'] = self.rent_unit.to_alipay_dict()
            else:
                params['rent_unit'] = self.rent_unit
        if self.rental_requirements:
            if isinstance(self.rental_requirements, list):
                for i in range(0, len(self.rental_requirements)):
                    element = self.rental_requirements[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rental_requirements[i] = element.to_alipay_dict()
            if hasattr(self.rental_requirements, 'to_alipay_dict'):
                params['rental_requirements'] = self.rental_requirements.to_alipay_dict()
            else:
                params['rental_requirements'] = self.rental_requirements
        if self.rented_room:
            if hasattr(self.rented_room, 'to_alipay_dict'):
                params['rented_room'] = self.rented_room.to_alipay_dict()
            else:
                params['rented_room'] = self.rented_room
        if self.renting_type:
            if hasattr(self.renting_type, 'to_alipay_dict'):
                params['renting_type'] = self.renting_type.to_alipay_dict()
            else:
                params['renting_type'] = self.renting_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_floors:
            if hasattr(self.total_floors, 'to_alipay_dict'):
                params['total_floors'] = self.total_floors.to_alipay_dict()
            else:
                params['total_floors'] = self.total_floors
        if self.verification_code:
            if hasattr(self.verification_code, 'to_alipay_dict'):
                params['verification_code'] = self.verification_code.to_alipay_dict()
            else:
                params['verification_code'] = self.verification_code
        if self.viewing_time:
            if isinstance(self.viewing_time, list):
                for i in range(0, len(self.viewing_time)):
                    element = self.viewing_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.viewing_time[i] = element.to_alipay_dict()
            if hasattr(self.viewing_time, 'to_alipay_dict'):
                params['viewing_time'] = self.viewing_time.to_alipay_dict()
            else:
                params['viewing_time'] = self.viewing_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHousingHouseRentalModifyModel()
        if 'accommodation' in d:
            o.accommodation = d['accommodation']
        if 'building_category' in d:
            o.building_category = d['building_category']
        if 'check_in_time' in d:
            o.check_in_time = d['check_in_time']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'constructed_area' in d:
            o.constructed_area = d['constructed_area']
        if 'contact_person' in d:
            o.contact_person = d['contact_person']
        if 'contact_person_phone' in d:
            o.contact_person_phone = d['contact_person_phone']
        if 'contact_persons_photo' in d:
            o.contact_persons_photo = d['contact_persons_photo']
        if 'current_condition_house' in d:
            o.current_condition_house = d['current_condition_house']
        if 'deposit' in d:
            o.deposit = d['deposit']
        if 'elevator' in d:
            o.elevator = d['elevator']
        if 'elevator_to_unit_ratio' in d:
            o.elevator_to_unit_ratio = d['elevator_to_unit_ratio']
        if 'floor_level' in d:
            o.floor_level = d['floor_level']
        if 'floor_range' in d:
            o.floor_range = d['floor_range']
        if 'has_private_bathroom' in d:
            o.has_private_bathroom = d['has_private_bathroom']
        if 'house_label' in d:
            o.house_label = d['house_label']
        if 'house_pic' in d:
            o.house_pic = d['house_pic']
        if 'house_structure' in d:
            o.house_structure = d['house_structure']
        if 'house_video' in d:
            o.house_video = d['house_video']
        if 'house_vr_url' in d:
            o.house_vr_url = d['house_vr_url']
        if 'housing_id' in d:
            o.housing_id = d['housing_id']
        if 'housing_type' in d:
            o.housing_type = d['housing_type']
        if 'internal_area' in d:
            o.internal_area = d['internal_area']
        if 'listing_date' in d:
            o.listing_date = d['listing_date']
        if 'orientation' in d:
            o.orientation = d['orientation']
        if 'other' in d:
            o.other = d['other']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'parking_space' in d:
            o.parking_space = d['parking_space']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'power_of_attorney' in d:
            o.power_of_attorney = d['power_of_attorney']
        if 'property_description' in d:
            o.property_description = d['property_description']
        if 'property_features' in d:
            o.property_features = d['property_features']
        if 'property_rights' in d:
            o.property_rights = d['property_rights']
        if 'property_title' in d:
            o.property_title = d['property_title']
        if 'renovation' in d:
            o.renovation = d['renovation']
        if 'rent' in d:
            o.rent = d['rent']
        if 'rent_unit' in d:
            o.rent_unit = d['rent_unit']
        if 'rental_requirements' in d:
            o.rental_requirements = d['rental_requirements']
        if 'rented_room' in d:
            o.rented_room = d['rented_room']
        if 'renting_type' in d:
            o.renting_type = d['renting_type']
        if 'status' in d:
            o.status = d['status']
        if 'total_floors' in d:
            o.total_floors = d['total_floors']
        if 'verification_code' in d:
            o.verification_code = d['verification_code']
        if 'viewing_time' in d:
            o.viewing_time = d['viewing_time']
        return o


