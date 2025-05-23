#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingNewhouseProjectSaveModel(object):

    def __init__(self):
        self._address = None
        self._alias = None
        self._avg_price = None
        self._business_district = None
        self._city_code = None
        self._contact_person = None
        self._contact_person_phone = None
        self._cover_area = None
        self._development_company = None
        self._district_code = None
        self._estate_project_img = None
        self._estate_project_label = None
        self._estate_project_video = None
        self._external_id = None
        self._floor_area_ratio = None
        self._greenery_ratio = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._presale_certificate = None
        self._property_management_fee = None
        self._property_right_year = None
        self._property_type = None
        self._province_code = None
        self._renovation = None
        self._sale_address = None
        self._sale_status = None
        self._status = None
        self._sum_buildings = None
        self._sum_units = None
        self._supply_company = None
        self._vehicle_unit_ratio = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value
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
    def cover_area(self):
        return self._cover_area

    @cover_area.setter
    def cover_area(self, value):
        self._cover_area = value
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
    def estate_project_img(self):
        return self._estate_project_img

    @estate_project_img.setter
    def estate_project_img(self, value):
        if isinstance(value, list):
            self._estate_project_img = list()
            for i in value:
                self._estate_project_img.append(i)
    @property
    def estate_project_label(self):
        return self._estate_project_label

    @estate_project_label.setter
    def estate_project_label(self, value):
        if isinstance(value, list):
            self._estate_project_label = list()
            for i in value:
                self._estate_project_label.append(i)
    @property
    def estate_project_video(self):
        return self._estate_project_video

    @estate_project_video.setter
    def estate_project_video(self, value):
        if isinstance(value, list):
            self._estate_project_video = list()
            for i in value:
                self._estate_project_video.append(i)
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def presale_certificate(self):
        return self._presale_certificate

    @presale_certificate.setter
    def presale_certificate(self, value):
        if isinstance(value, list):
            self._presale_certificate = list()
            for i in value:
                self._presale_certificate.append(i)
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
    def renovation(self):
        return self._renovation

    @renovation.setter
    def renovation(self, value):
        self._renovation = value
    @property
    def sale_address(self):
        return self._sale_address

    @sale_address.setter
    def sale_address(self, value):
        self._sale_address = value
    @property
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.alias:
            if hasattr(self.alias, 'to_alipay_dict'):
                params['alias'] = self.alias.to_alipay_dict()
            else:
                params['alias'] = self.alias
        if self.avg_price:
            if hasattr(self.avg_price, 'to_alipay_dict'):
                params['avg_price'] = self.avg_price.to_alipay_dict()
            else:
                params['avg_price'] = self.avg_price
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
        if self.cover_area:
            if hasattr(self.cover_area, 'to_alipay_dict'):
                params['cover_area'] = self.cover_area.to_alipay_dict()
            else:
                params['cover_area'] = self.cover_area
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
        if self.estate_project_img:
            if isinstance(self.estate_project_img, list):
                for i in range(0, len(self.estate_project_img)):
                    element = self.estate_project_img[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.estate_project_img[i] = element.to_alipay_dict()
            if hasattr(self.estate_project_img, 'to_alipay_dict'):
                params['estate_project_img'] = self.estate_project_img.to_alipay_dict()
            else:
                params['estate_project_img'] = self.estate_project_img
        if self.estate_project_label:
            if isinstance(self.estate_project_label, list):
                for i in range(0, len(self.estate_project_label)):
                    element = self.estate_project_label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.estate_project_label[i] = element.to_alipay_dict()
            if hasattr(self.estate_project_label, 'to_alipay_dict'):
                params['estate_project_label'] = self.estate_project_label.to_alipay_dict()
            else:
                params['estate_project_label'] = self.estate_project_label
        if self.estate_project_video:
            if isinstance(self.estate_project_video, list):
                for i in range(0, len(self.estate_project_video)):
                    element = self.estate_project_video[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.estate_project_video[i] = element.to_alipay_dict()
            if hasattr(self.estate_project_video, 'to_alipay_dict'):
                params['estate_project_video'] = self.estate_project_video.to_alipay_dict()
            else:
                params['estate_project_video'] = self.estate_project_video
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.presale_certificate:
            if isinstance(self.presale_certificate, list):
                for i in range(0, len(self.presale_certificate)):
                    element = self.presale_certificate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.presale_certificate[i] = element.to_alipay_dict()
            if hasattr(self.presale_certificate, 'to_alipay_dict'):
                params['presale_certificate'] = self.presale_certificate.to_alipay_dict()
            else:
                params['presale_certificate'] = self.presale_certificate
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
        if self.renovation:
            if hasattr(self.renovation, 'to_alipay_dict'):
                params['renovation'] = self.renovation.to_alipay_dict()
            else:
                params['renovation'] = self.renovation
        if self.sale_address:
            if hasattr(self.sale_address, 'to_alipay_dict'):
                params['sale_address'] = self.sale_address.to_alipay_dict()
            else:
                params['sale_address'] = self.sale_address
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHousingNewhouseProjectSaveModel()
        if 'address' in d:
            o.address = d['address']
        if 'alias' in d:
            o.alias = d['alias']
        if 'avg_price' in d:
            o.avg_price = d['avg_price']
        if 'business_district' in d:
            o.business_district = d['business_district']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'contact_person' in d:
            o.contact_person = d['contact_person']
        if 'contact_person_phone' in d:
            o.contact_person_phone = d['contact_person_phone']
        if 'cover_area' in d:
            o.cover_area = d['cover_area']
        if 'development_company' in d:
            o.development_company = d['development_company']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'estate_project_img' in d:
            o.estate_project_img = d['estate_project_img']
        if 'estate_project_label' in d:
            o.estate_project_label = d['estate_project_label']
        if 'estate_project_video' in d:
            o.estate_project_video = d['estate_project_video']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'floor_area_ratio' in d:
            o.floor_area_ratio = d['floor_area_ratio']
        if 'greenery_ratio' in d:
            o.greenery_ratio = d['greenery_ratio']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'presale_certificate' in d:
            o.presale_certificate = d['presale_certificate']
        if 'property_management_fee' in d:
            o.property_management_fee = d['property_management_fee']
        if 'property_right_year' in d:
            o.property_right_year = d['property_right_year']
        if 'property_type' in d:
            o.property_type = d['property_type']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'renovation' in d:
            o.renovation = d['renovation']
        if 'sale_address' in d:
            o.sale_address = d['sale_address']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'status' in d:
            o.status = d['status']
        if 'sum_buildings' in d:
            o.sum_buildings = d['sum_buildings']
        if 'sum_units' in d:
            o.sum_units = d['sum_units']
        if 'supply_company' in d:
            o.supply_company = d['supply_company']
        if 'vehicle_unit_ratio' in d:
            o.vehicle_unit_ratio = d['vehicle_unit_ratio']
        return o


