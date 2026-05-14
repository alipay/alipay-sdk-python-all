#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CareInfo(object):

    def __init__(self):
        self._bed_card_photo_url_list = None
        self._city_name = None
        self._department = None
        self._district_name = None
        self._external_caregiver = None
        self._hospital_address = None
        self._hospital_name = None
        self._inpatient_date = None
        self._province_name = None
        self._service_days = None
        self._service_start_time = None

    @property
    def bed_card_photo_url_list(self):
        return self._bed_card_photo_url_list

    @bed_card_photo_url_list.setter
    def bed_card_photo_url_list(self, value):
        if isinstance(value, list):
            self._bed_card_photo_url_list = list()
            for i in value:
                self._bed_card_photo_url_list.append(i)
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def external_caregiver(self):
        return self._external_caregiver

    @external_caregiver.setter
    def external_caregiver(self, value):
        self._external_caregiver = value
    @property
    def hospital_address(self):
        return self._hospital_address

    @hospital_address.setter
    def hospital_address(self, value):
        self._hospital_address = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def inpatient_date(self):
        return self._inpatient_date

    @inpatient_date.setter
    def inpatient_date(self, value):
        self._inpatient_date = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def service_days(self):
        return self._service_days

    @service_days.setter
    def service_days(self, value):
        self._service_days = value
    @property
    def service_start_time(self):
        return self._service_start_time

    @service_start_time.setter
    def service_start_time(self, value):
        self._service_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bed_card_photo_url_list:
            if isinstance(self.bed_card_photo_url_list, list):
                for i in range(0, len(self.bed_card_photo_url_list)):
                    element = self.bed_card_photo_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bed_card_photo_url_list[i] = element.to_alipay_dict()
            if hasattr(self.bed_card_photo_url_list, 'to_alipay_dict'):
                params['bed_card_photo_url_list'] = self.bed_card_photo_url_list.to_alipay_dict()
            else:
                params['bed_card_photo_url_list'] = self.bed_card_photo_url_list
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.external_caregiver:
            if hasattr(self.external_caregiver, 'to_alipay_dict'):
                params['external_caregiver'] = self.external_caregiver.to_alipay_dict()
            else:
                params['external_caregiver'] = self.external_caregiver
        if self.hospital_address:
            if hasattr(self.hospital_address, 'to_alipay_dict'):
                params['hospital_address'] = self.hospital_address.to_alipay_dict()
            else:
                params['hospital_address'] = self.hospital_address
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.inpatient_date:
            if hasattr(self.inpatient_date, 'to_alipay_dict'):
                params['inpatient_date'] = self.inpatient_date.to_alipay_dict()
            else:
                params['inpatient_date'] = self.inpatient_date
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.service_days:
            if hasattr(self.service_days, 'to_alipay_dict'):
                params['service_days'] = self.service_days.to_alipay_dict()
            else:
                params['service_days'] = self.service_days
        if self.service_start_time:
            if hasattr(self.service_start_time, 'to_alipay_dict'):
                params['service_start_time'] = self.service_start_time.to_alipay_dict()
            else:
                params['service_start_time'] = self.service_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CareInfo()
        if 'bed_card_photo_url_list' in d:
            o.bed_card_photo_url_list = d['bed_card_photo_url_list']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'department' in d:
            o.department = d['department']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'external_caregiver' in d:
            o.external_caregiver = d['external_caregiver']
        if 'hospital_address' in d:
            o.hospital_address = d['hospital_address']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'inpatient_date' in d:
            o.inpatient_date = d['inpatient_date']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'service_days' in d:
            o.service_days = d['service_days']
        if 'service_start_time' in d:
            o.service_start_time = d['service_start_time']
        return o


