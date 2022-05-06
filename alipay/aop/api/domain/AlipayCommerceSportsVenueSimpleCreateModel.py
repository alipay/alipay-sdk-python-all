#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsVenueSimpleCreateModel(object):

    def __init__(self):
        self._address = None
        self._admission_requirement = None
        self._announcement = None
        self._area_code = None
        self._bookable = None
        self._city_code = None
        self._desc = None
        self._equipment_rental = None
        self._extra_service_url = None
        self._facility_list = None
        self._join_type = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._opening_hours = None
        self._out_venue_id = None
        self._payee_account = None
        self._payment_method = None
        self._payment_type = None
        self._phone = None
        self._picture_list = None
        self._poi = None
        self._poster = None
        self._product_type_list = None
        self._promotion = None
        self._province_code = None
        self._rec_price = None
        self._sub_venue_pid = None
        self._sub_venue_smid = None
        self._tag_list = None
        self._test_venue = None
        self._traffic = None
        self._training = None
        self._venue_pid = None
        self._venue_type = None
        self._vip = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def admission_requirement(self):
        return self._admission_requirement

    @admission_requirement.setter
    def admission_requirement(self, value):
        self._admission_requirement = value
    @property
    def announcement(self):
        return self._announcement

    @announcement.setter
    def announcement(self, value):
        self._announcement = value
    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def bookable(self):
        return self._bookable

    @bookable.setter
    def bookable(self, value):
        self._bookable = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def equipment_rental(self):
        return self._equipment_rental

    @equipment_rental.setter
    def equipment_rental(self, value):
        self._equipment_rental = value
    @property
    def extra_service_url(self):
        return self._extra_service_url

    @extra_service_url.setter
    def extra_service_url(self, value):
        self._extra_service_url = value
    @property
    def facility_list(self):
        return self._facility_list

    @facility_list.setter
    def facility_list(self, value):
        if isinstance(value, list):
            self._facility_list = list()
            for i in value:
                self._facility_list.append(i)
    @property
    def join_type(self):
        return self._join_type

    @join_type.setter
    def join_type(self, value):
        self._join_type = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value):
        self._opening_hours = value
    @property
    def out_venue_id(self):
        return self._out_venue_id

    @out_venue_id.setter
    def out_venue_id(self, value):
        self._out_venue_id = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if isinstance(value, list):
            self._phone = list()
            for i in value:
                self._phone.append(i)
    @property
    def picture_list(self):
        return self._picture_list

    @picture_list.setter
    def picture_list(self, value):
        if isinstance(value, list):
            self._picture_list = list()
            for i in value:
                self._picture_list.append(i)
    @property
    def poi(self):
        return self._poi

    @poi.setter
    def poi(self, value):
        self._poi = value
    @property
    def poster(self):
        return self._poster

    @poster.setter
    def poster(self, value):
        self._poster = value
    @property
    def product_type_list(self):
        return self._product_type_list

    @product_type_list.setter
    def product_type_list(self, value):
        if isinstance(value, list):
            self._product_type_list = list()
            for i in value:
                self._product_type_list.append(i)
    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        self._promotion = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def rec_price(self):
        return self._rec_price

    @rec_price.setter
    def rec_price(self, value):
        self._rec_price = value
    @property
    def sub_venue_pid(self):
        return self._sub_venue_pid

    @sub_venue_pid.setter
    def sub_venue_pid(self, value):
        self._sub_venue_pid = value
    @property
    def sub_venue_smid(self):
        return self._sub_venue_smid

    @sub_venue_smid.setter
    def sub_venue_smid(self, value):
        self._sub_venue_smid = value
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                self._tag_list.append(i)
    @property
    def test_venue(self):
        return self._test_venue

    @test_venue.setter
    def test_venue(self, value):
        self._test_venue = value
    @property
    def traffic(self):
        return self._traffic

    @traffic.setter
    def traffic(self, value):
        self._traffic = value
    @property
    def training(self):
        return self._training

    @training.setter
    def training(self, value):
        self._training = value
    @property
    def venue_pid(self):
        return self._venue_pid

    @venue_pid.setter
    def venue_pid(self, value):
        self._venue_pid = value
    @property
    def venue_type(self):
        return self._venue_type

    @venue_type.setter
    def venue_type(self, value):
        if isinstance(value, list):
            self._venue_type = list()
            for i in value:
                self._venue_type.append(i)
    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, value):
        self._vip = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.admission_requirement:
            if hasattr(self.admission_requirement, 'to_alipay_dict'):
                params['admission_requirement'] = self.admission_requirement.to_alipay_dict()
            else:
                params['admission_requirement'] = self.admission_requirement
        if self.announcement:
            if hasattr(self.announcement, 'to_alipay_dict'):
                params['announcement'] = self.announcement.to_alipay_dict()
            else:
                params['announcement'] = self.announcement
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.bookable:
            if hasattr(self.bookable, 'to_alipay_dict'):
                params['bookable'] = self.bookable.to_alipay_dict()
            else:
                params['bookable'] = self.bookable
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.equipment_rental:
            if hasattr(self.equipment_rental, 'to_alipay_dict'):
                params['equipment_rental'] = self.equipment_rental.to_alipay_dict()
            else:
                params['equipment_rental'] = self.equipment_rental
        if self.extra_service_url:
            if hasattr(self.extra_service_url, 'to_alipay_dict'):
                params['extra_service_url'] = self.extra_service_url.to_alipay_dict()
            else:
                params['extra_service_url'] = self.extra_service_url
        if self.facility_list:
            if isinstance(self.facility_list, list):
                for i in range(0, len(self.facility_list)):
                    element = self.facility_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.facility_list[i] = element.to_alipay_dict()
            if hasattr(self.facility_list, 'to_alipay_dict'):
                params['facility_list'] = self.facility_list.to_alipay_dict()
            else:
                params['facility_list'] = self.facility_list
        if self.join_type:
            if hasattr(self.join_type, 'to_alipay_dict'):
                params['join_type'] = self.join_type.to_alipay_dict()
            else:
                params['join_type'] = self.join_type
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.opening_hours:
            if hasattr(self.opening_hours, 'to_alipay_dict'):
                params['opening_hours'] = self.opening_hours.to_alipay_dict()
            else:
                params['opening_hours'] = self.opening_hours
        if self.out_venue_id:
            if hasattr(self.out_venue_id, 'to_alipay_dict'):
                params['out_venue_id'] = self.out_venue_id.to_alipay_dict()
            else:
                params['out_venue_id'] = self.out_venue_id
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.phone:
            if isinstance(self.phone, list):
                for i in range(0, len(self.phone)):
                    element = self.phone[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone[i] = element.to_alipay_dict()
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.picture_list:
            if isinstance(self.picture_list, list):
                for i in range(0, len(self.picture_list)):
                    element = self.picture_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.picture_list[i] = element.to_alipay_dict()
            if hasattr(self.picture_list, 'to_alipay_dict'):
                params['picture_list'] = self.picture_list.to_alipay_dict()
            else:
                params['picture_list'] = self.picture_list
        if self.poi:
            if hasattr(self.poi, 'to_alipay_dict'):
                params['poi'] = self.poi.to_alipay_dict()
            else:
                params['poi'] = self.poi
        if self.poster:
            if hasattr(self.poster, 'to_alipay_dict'):
                params['poster'] = self.poster.to_alipay_dict()
            else:
                params['poster'] = self.poster
        if self.product_type_list:
            if isinstance(self.product_type_list, list):
                for i in range(0, len(self.product_type_list)):
                    element = self.product_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_type_list[i] = element.to_alipay_dict()
            if hasattr(self.product_type_list, 'to_alipay_dict'):
                params['product_type_list'] = self.product_type_list.to_alipay_dict()
            else:
                params['product_type_list'] = self.product_type_list
        if self.promotion:
            if hasattr(self.promotion, 'to_alipay_dict'):
                params['promotion'] = self.promotion.to_alipay_dict()
            else:
                params['promotion'] = self.promotion
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.rec_price:
            if hasattr(self.rec_price, 'to_alipay_dict'):
                params['rec_price'] = self.rec_price.to_alipay_dict()
            else:
                params['rec_price'] = self.rec_price
        if self.sub_venue_pid:
            if hasattr(self.sub_venue_pid, 'to_alipay_dict'):
                params['sub_venue_pid'] = self.sub_venue_pid.to_alipay_dict()
            else:
                params['sub_venue_pid'] = self.sub_venue_pid
        if self.sub_venue_smid:
            if hasattr(self.sub_venue_smid, 'to_alipay_dict'):
                params['sub_venue_smid'] = self.sub_venue_smid.to_alipay_dict()
            else:
                params['sub_venue_smid'] = self.sub_venue_smid
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        if self.test_venue:
            if hasattr(self.test_venue, 'to_alipay_dict'):
                params['test_venue'] = self.test_venue.to_alipay_dict()
            else:
                params['test_venue'] = self.test_venue
        if self.traffic:
            if hasattr(self.traffic, 'to_alipay_dict'):
                params['traffic'] = self.traffic.to_alipay_dict()
            else:
                params['traffic'] = self.traffic
        if self.training:
            if hasattr(self.training, 'to_alipay_dict'):
                params['training'] = self.training.to_alipay_dict()
            else:
                params['training'] = self.training
        if self.venue_pid:
            if hasattr(self.venue_pid, 'to_alipay_dict'):
                params['venue_pid'] = self.venue_pid.to_alipay_dict()
            else:
                params['venue_pid'] = self.venue_pid
        if self.venue_type:
            if isinstance(self.venue_type, list):
                for i in range(0, len(self.venue_type)):
                    element = self.venue_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.venue_type[i] = element.to_alipay_dict()
            if hasattr(self.venue_type, 'to_alipay_dict'):
                params['venue_type'] = self.venue_type.to_alipay_dict()
            else:
                params['venue_type'] = self.venue_type
        if self.vip:
            if hasattr(self.vip, 'to_alipay_dict'):
                params['vip'] = self.vip.to_alipay_dict()
            else:
                params['vip'] = self.vip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsVenueSimpleCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'admission_requirement' in d:
            o.admission_requirement = d['admission_requirement']
        if 'announcement' in d:
            o.announcement = d['announcement']
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'bookable' in d:
            o.bookable = d['bookable']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'equipment_rental' in d:
            o.equipment_rental = d['equipment_rental']
        if 'extra_service_url' in d:
            o.extra_service_url = d['extra_service_url']
        if 'facility_list' in d:
            o.facility_list = d['facility_list']
        if 'join_type' in d:
            o.join_type = d['join_type']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'opening_hours' in d:
            o.opening_hours = d['opening_hours']
        if 'out_venue_id' in d:
            o.out_venue_id = d['out_venue_id']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'picture_list' in d:
            o.picture_list = d['picture_list']
        if 'poi' in d:
            o.poi = d['poi']
        if 'poster' in d:
            o.poster = d['poster']
        if 'product_type_list' in d:
            o.product_type_list = d['product_type_list']
        if 'promotion' in d:
            o.promotion = d['promotion']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'rec_price' in d:
            o.rec_price = d['rec_price']
        if 'sub_venue_pid' in d:
            o.sub_venue_pid = d['sub_venue_pid']
        if 'sub_venue_smid' in d:
            o.sub_venue_smid = d['sub_venue_smid']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'test_venue' in d:
            o.test_venue = d['test_venue']
        if 'traffic' in d:
            o.traffic = d['traffic']
        if 'training' in d:
            o.training = d['training']
        if 'venue_pid' in d:
            o.venue_pid = d['venue_pid']
        if 'venue_type' in d:
            o.venue_type = d['venue_type']
        if 'vip' in d:
            o.vip = d['vip']
        return o


