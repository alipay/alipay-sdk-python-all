#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingApartmentModifyModel(object):

    def __init__(self):
        self._accommodation = None
        self._apartment_facilities = None
        self._apartment_id = None
        self._apartment_img = None
        self._apartment_services = None
        self._apartment_video = None
        self._apartment_vr = None
        self._bed_room = None
        self._contact_person = None
        self._contact_person_phone = None
        self._contact_persons_photo = None
        self._elevator_to_unit_ratio = None
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
        self._qualification_requirements = None
        self._rent_end = None
        self._rent_start = None
        self._rent_unit = None
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
    def elevator_to_unit_ratio(self):
        return self._elevator_to_unit_ratio

    @elevator_to_unit_ratio.setter
    def elevator_to_unit_ratio(self, value):
        self._elevator_to_unit_ratio = value
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
        if self.apartment_id:
            if hasattr(self.apartment_id, 'to_alipay_dict'):
                params['apartment_id'] = self.apartment_id.to_alipay_dict()
            else:
                params['apartment_id'] = self.apartment_id
        if self.apartment_img:
            if isinstance(self.apartment_img, list):
                for i in range(0, len(self.apartment_img)):
                    element = self.apartment_img[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apartment_img[i] = element.to_alipay_dict()
            if hasattr(self.apartment_img, 'to_alipay_dict'):
                params['apartment_img'] = self.apartment_img.to_alipay_dict()
            else:
                params['apartment_img'] = self.apartment_img
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
        if self.apartment_video:
            if isinstance(self.apartment_video, list):
                for i in range(0, len(self.apartment_video)):
                    element = self.apartment_video[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apartment_video[i] = element.to_alipay_dict()
            if hasattr(self.apartment_video, 'to_alipay_dict'):
                params['apartment_video'] = self.apartment_video.to_alipay_dict()
            else:
                params['apartment_video'] = self.apartment_video
        if self.apartment_vr:
            if hasattr(self.apartment_vr, 'to_alipay_dict'):
                params['apartment_vr'] = self.apartment_vr.to_alipay_dict()
            else:
                params['apartment_vr'] = self.apartment_vr
        if self.bed_room:
            if hasattr(self.bed_room, 'to_alipay_dict'):
                params['bed_room'] = self.bed_room.to_alipay_dict()
            else:
                params['bed_room'] = self.bed_room
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
        if self.elevator_to_unit_ratio:
            if hasattr(self.elevator_to_unit_ratio, 'to_alipay_dict'):
                params['elevator_to_unit_ratio'] = self.elevator_to_unit_ratio.to_alipay_dict()
            else:
                params['elevator_to_unit_ratio'] = self.elevator_to_unit_ratio
        if self.floor_end:
            if hasattr(self.floor_end, 'to_alipay_dict'):
                params['floor_end'] = self.floor_end.to_alipay_dict()
            else:
                params['floor_end'] = self.floor_end
        if self.floor_start:
            if hasattr(self.floor_start, 'to_alipay_dict'):
                params['floor_start'] = self.floor_start.to_alipay_dict()
            else:
                params['floor_start'] = self.floor_start
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
        if self.housing_type:
            if hasattr(self.housing_type, 'to_alipay_dict'):
                params['housing_type'] = self.housing_type.to_alipay_dict()
            else:
                params['housing_type'] = self.housing_type
        if self.intentional_application:
            if hasattr(self.intentional_application, 'to_alipay_dict'):
                params['intentional_application'] = self.intentional_application.to_alipay_dict()
            else:
                params['intentional_application'] = self.intentional_application
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
        if self.property_title:
            if hasattr(self.property_title, 'to_alipay_dict'):
                params['property_title'] = self.property_title.to_alipay_dict()
            else:
                params['property_title'] = self.property_title
        if self.qualification_requirements:
            if hasattr(self.qualification_requirements, 'to_alipay_dict'):
                params['qualification_requirements'] = self.qualification_requirements.to_alipay_dict()
            else:
                params['qualification_requirements'] = self.qualification_requirements
        if self.rent_end:
            if hasattr(self.rent_end, 'to_alipay_dict'):
                params['rent_end'] = self.rent_end.to_alipay_dict()
            else:
                params['rent_end'] = self.rent_end
        if self.rent_start:
            if hasattr(self.rent_start, 'to_alipay_dict'):
                params['rent_start'] = self.rent_start.to_alipay_dict()
            else:
                params['rent_start'] = self.rent_start
        if self.rent_unit:
            if hasattr(self.rent_unit, 'to_alipay_dict'):
                params['rent_unit'] = self.rent_unit.to_alipay_dict()
            else:
                params['rent_unit'] = self.rent_unit
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.usable_area_end:
            if hasattr(self.usable_area_end, 'to_alipay_dict'):
                params['usable_area_end'] = self.usable_area_end.to_alipay_dict()
            else:
                params['usable_area_end'] = self.usable_area_end
        if self.usable_area_start:
            if hasattr(self.usable_area_start, 'to_alipay_dict'):
                params['usable_area_start'] = self.usable_area_start.to_alipay_dict()
            else:
                params['usable_area_start'] = self.usable_area_start
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
        o = AlipayCommerceHousingApartmentModifyModel()
        if 'accommodation' in d:
            o.accommodation = d['accommodation']
        if 'apartment_facilities' in d:
            o.apartment_facilities = d['apartment_facilities']
        if 'apartment_id' in d:
            o.apartment_id = d['apartment_id']
        if 'apartment_img' in d:
            o.apartment_img = d['apartment_img']
        if 'apartment_services' in d:
            o.apartment_services = d['apartment_services']
        if 'apartment_video' in d:
            o.apartment_video = d['apartment_video']
        if 'apartment_vr' in d:
            o.apartment_vr = d['apartment_vr']
        if 'bed_room' in d:
            o.bed_room = d['bed_room']
        if 'contact_person' in d:
            o.contact_person = d['contact_person']
        if 'contact_person_phone' in d:
            o.contact_person_phone = d['contact_person_phone']
        if 'contact_persons_photo' in d:
            o.contact_persons_photo = d['contact_persons_photo']
        if 'elevator_to_unit_ratio' in d:
            o.elevator_to_unit_ratio = d['elevator_to_unit_ratio']
        if 'floor_end' in d:
            o.floor_end = d['floor_end']
        if 'floor_start' in d:
            o.floor_start = d['floor_start']
        if 'house_label' in d:
            o.house_label = d['house_label']
        if 'house_program_id' in d:
            o.house_program_id = d['house_program_id']
        if 'house_structure' in d:
            o.house_structure = d['house_structure']
        if 'housing_type' in d:
            o.housing_type = d['housing_type']
        if 'intentional_application' in d:
            o.intentional_application = d['intentional_application']
        if 'orientation' in d:
            o.orientation = d['orientation']
        if 'other' in d:
            o.other = d['other']
        if 'property_description' in d:
            o.property_description = d['property_description']
        if 'property_features' in d:
            o.property_features = d['property_features']
        if 'property_title' in d:
            o.property_title = d['property_title']
        if 'qualification_requirements' in d:
            o.qualification_requirements = d['qualification_requirements']
        if 'rent_end' in d:
            o.rent_end = d['rent_end']
        if 'rent_start' in d:
            o.rent_start = d['rent_start']
        if 'rent_unit' in d:
            o.rent_unit = d['rent_unit']
        if 'status' in d:
            o.status = d['status']
        if 'usable_area_end' in d:
            o.usable_area_end = d['usable_area_end']
        if 'usable_area_start' in d:
            o.usable_area_start = d['usable_area_start']
        if 'viewing_time' in d:
            o.viewing_time = d['viewing_time']
        return o


