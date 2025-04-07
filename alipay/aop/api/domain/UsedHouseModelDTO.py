#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UsedHouseModelDTO(object):

    def __init__(self):
        self._bath_room = None
        self._bed_room = None
        self._building_category = None
        self._community_id = None
        self._constructed_area = None
        self._construction_year = None
        self._contact_person = None
        self._contact_person_phone = None
        self._contact_persons_photo = None
        self._current_condition_house = None
        self._doorplate_number = None
        self._elevator = None
        self._elevator_to_unit_ratio = None
        self._external_id = None
        self._floor_level = None
        self._floor_range = None
        self._house_age = None
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
        self._power_of_attorney = None
        self._property_code = None
        self._property_description = None
        self._property_features = None
        self._property_right_year = None
        self._property_rights = None
        self._property_title = None
        self._renovation = None
        self._source_company = None
        self._status = None
        self._the_only_housing = None
        self._total_floors = None
        self._total_price = None
        self._unit_price = None
        self._verification_code = None
        self._viewing_time = None

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
    def house_age(self):
        return self._house_age

    @house_age.setter
    def house_age(self, value):
        self._house_age = value
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
    def power_of_attorney(self):
        return self._power_of_attorney

    @power_of_attorney.setter
    def power_of_attorney(self, value):
        self._power_of_attorney = value
    @property
    def property_code(self):
        return self._property_code

    @property_code.setter
    def property_code(self, value):
        self._property_code = value
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
    def property_right_year(self):
        return self._property_right_year

    @property_right_year.setter
    def property_right_year(self, value):
        self._property_right_year = value
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
    def the_only_housing(self):
        return self._the_only_housing

    @the_only_housing.setter
    def the_only_housing(self, value):
        self._the_only_housing = value
    @property
    def total_floors(self):
        return self._total_floors

    @total_floors.setter
    def total_floors(self, value):
        self._total_floors = value
    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value
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
        if self.bath_room:
            if hasattr(self.bath_room, 'to_alipay_dict'):
                params['bath_room'] = self.bath_room.to_alipay_dict()
            else:
                params['bath_room'] = self.bath_room
        if self.bed_room:
            if hasattr(self.bed_room, 'to_alipay_dict'):
                params['bed_room'] = self.bed_room.to_alipay_dict()
            else:
                params['bed_room'] = self.bed_room
        if self.building_category:
            if hasattr(self.building_category, 'to_alipay_dict'):
                params['building_category'] = self.building_category.to_alipay_dict()
            else:
                params['building_category'] = self.building_category
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
        if self.doorplate_number:
            if hasattr(self.doorplate_number, 'to_alipay_dict'):
                params['doorplate_number'] = self.doorplate_number.to_alipay_dict()
            else:
                params['doorplate_number'] = self.doorplate_number
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
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
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
        if self.house_age:
            if hasattr(self.house_age, 'to_alipay_dict'):
                params['house_age'] = self.house_age.to_alipay_dict()
            else:
                params['house_age'] = self.house_age
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
        if self.house_program_id:
            if hasattr(self.house_program_id, 'to_alipay_dict'):
                params['house_program_id'] = self.house_program_id.to_alipay_dict()
            else:
                params['house_program_id'] = self.house_program_id
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
        if self.kitchen:
            if hasattr(self.kitchen, 'to_alipay_dict'):
                params['kitchen'] = self.kitchen.to_alipay_dict()
            else:
                params['kitchen'] = self.kitchen
        if self.listing_date:
            if hasattr(self.listing_date, 'to_alipay_dict'):
                params['listing_date'] = self.listing_date.to_alipay_dict()
            else:
                params['listing_date'] = self.listing_date
        if self.living_room:
            if hasattr(self.living_room, 'to_alipay_dict'):
                params['living_room'] = self.living_room.to_alipay_dict()
            else:
                params['living_room'] = self.living_room
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
        if self.power_of_attorney:
            if hasattr(self.power_of_attorney, 'to_alipay_dict'):
                params['power_of_attorney'] = self.power_of_attorney.to_alipay_dict()
            else:
                params['power_of_attorney'] = self.power_of_attorney
        if self.property_code:
            if hasattr(self.property_code, 'to_alipay_dict'):
                params['property_code'] = self.property_code.to_alipay_dict()
            else:
                params['property_code'] = self.property_code
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
        if self.property_right_year:
            if hasattr(self.property_right_year, 'to_alipay_dict'):
                params['property_right_year'] = self.property_right_year.to_alipay_dict()
            else:
                params['property_right_year'] = self.property_right_year
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
        if self.source_company:
            if hasattr(self.source_company, 'to_alipay_dict'):
                params['source_company'] = self.source_company.to_alipay_dict()
            else:
                params['source_company'] = self.source_company
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.the_only_housing:
            if hasattr(self.the_only_housing, 'to_alipay_dict'):
                params['the_only_housing'] = self.the_only_housing.to_alipay_dict()
            else:
                params['the_only_housing'] = self.the_only_housing
        if self.total_floors:
            if hasattr(self.total_floors, 'to_alipay_dict'):
                params['total_floors'] = self.total_floors.to_alipay_dict()
            else:
                params['total_floors'] = self.total_floors
        if self.total_price:
            if hasattr(self.total_price, 'to_alipay_dict'):
                params['total_price'] = self.total_price.to_alipay_dict()
            else:
                params['total_price'] = self.total_price
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
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
        o = UsedHouseModelDTO()
        if 'bath_room' in d:
            o.bath_room = d['bath_room']
        if 'bed_room' in d:
            o.bed_room = d['bed_room']
        if 'building_category' in d:
            o.building_category = d['building_category']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'constructed_area' in d:
            o.constructed_area = d['constructed_area']
        if 'construction_year' in d:
            o.construction_year = d['construction_year']
        if 'contact_person' in d:
            o.contact_person = d['contact_person']
        if 'contact_person_phone' in d:
            o.contact_person_phone = d['contact_person_phone']
        if 'contact_persons_photo' in d:
            o.contact_persons_photo = d['contact_persons_photo']
        if 'current_condition_house' in d:
            o.current_condition_house = d['current_condition_house']
        if 'doorplate_number' in d:
            o.doorplate_number = d['doorplate_number']
        if 'elevator' in d:
            o.elevator = d['elevator']
        if 'elevator_to_unit_ratio' in d:
            o.elevator_to_unit_ratio = d['elevator_to_unit_ratio']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'floor_level' in d:
            o.floor_level = d['floor_level']
        if 'floor_range' in d:
            o.floor_range = d['floor_range']
        if 'house_age' in d:
            o.house_age = d['house_age']
        if 'house_label' in d:
            o.house_label = d['house_label']
        if 'house_pic' in d:
            o.house_pic = d['house_pic']
        if 'house_program_id' in d:
            o.house_program_id = d['house_program_id']
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
        if 'kitchen' in d:
            o.kitchen = d['kitchen']
        if 'listing_date' in d:
            o.listing_date = d['listing_date']
        if 'living_room' in d:
            o.living_room = d['living_room']
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
        if 'power_of_attorney' in d:
            o.power_of_attorney = d['power_of_attorney']
        if 'property_code' in d:
            o.property_code = d['property_code']
        if 'property_description' in d:
            o.property_description = d['property_description']
        if 'property_features' in d:
            o.property_features = d['property_features']
        if 'property_right_year' in d:
            o.property_right_year = d['property_right_year']
        if 'property_rights' in d:
            o.property_rights = d['property_rights']
        if 'property_title' in d:
            o.property_title = d['property_title']
        if 'renovation' in d:
            o.renovation = d['renovation']
        if 'source_company' in d:
            o.source_company = d['source_company']
        if 'status' in d:
            o.status = d['status']
        if 'the_only_housing' in d:
            o.the_only_housing = d['the_only_housing']
        if 'total_floors' in d:
            o.total_floors = d['total_floors']
        if 'total_price' in d:
            o.total_price = d['total_price']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        if 'verification_code' in d:
            o.verification_code = d['verification_code']
        if 'viewing_time' in d:
            o.viewing_time = d['viewing_time']
        return o


