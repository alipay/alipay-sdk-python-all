#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HouseOwner import HouseOwner


class House(object):

    def __init__(self):
        self._area_code = None
        self._built_year = None
        self._house_owners = None
        self._house_unit_codes = None
        self._its_floor = None
        self._land_cert_no = None
        self._location = None
        self._mortgaged = None
        self._owner_ship_status = None
        self._structure_area = None
        self._structure_area_unit = None
        self._total_floor = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def built_year(self):
        return self._built_year

    @built_year.setter
    def built_year(self, value):
        self._built_year = value
    @property
    def house_owners(self):
        return self._house_owners

    @house_owners.setter
    def house_owners(self, value):
        if isinstance(value, list):
            self._house_owners = list()
            for i in value:
                if isinstance(i, HouseOwner):
                    self._house_owners.append(i)
                else:
                    self._house_owners.append(HouseOwner.from_alipay_dict(i))
    @property
    def house_unit_codes(self):
        return self._house_unit_codes

    @house_unit_codes.setter
    def house_unit_codes(self, value):
        if isinstance(value, list):
            self._house_unit_codes = list()
            for i in value:
                self._house_unit_codes.append(i)
    @property
    def its_floor(self):
        return self._its_floor

    @its_floor.setter
    def its_floor(self, value):
        self._its_floor = value
    @property
    def land_cert_no(self):
        return self._land_cert_no

    @land_cert_no.setter
    def land_cert_no(self, value):
        self._land_cert_no = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def mortgaged(self):
        return self._mortgaged

    @mortgaged.setter
    def mortgaged(self, value):
        self._mortgaged = value
    @property
    def owner_ship_status(self):
        return self._owner_ship_status

    @owner_ship_status.setter
    def owner_ship_status(self, value):
        self._owner_ship_status = value
    @property
    def structure_area(self):
        return self._structure_area

    @structure_area.setter
    def structure_area(self, value):
        self._structure_area = value
    @property
    def structure_area_unit(self):
        return self._structure_area_unit

    @structure_area_unit.setter
    def structure_area_unit(self, value):
        self._structure_area_unit = value
    @property
    def total_floor(self):
        return self._total_floor

    @total_floor.setter
    def total_floor(self, value):
        self._total_floor = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.built_year:
            if hasattr(self.built_year, 'to_alipay_dict'):
                params['built_year'] = self.built_year.to_alipay_dict()
            else:
                params['built_year'] = self.built_year
        if self.house_owners:
            if isinstance(self.house_owners, list):
                for i in range(0, len(self.house_owners)):
                    element = self.house_owners[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.house_owners[i] = element.to_alipay_dict()
            if hasattr(self.house_owners, 'to_alipay_dict'):
                params['house_owners'] = self.house_owners.to_alipay_dict()
            else:
                params['house_owners'] = self.house_owners
        if self.house_unit_codes:
            if isinstance(self.house_unit_codes, list):
                for i in range(0, len(self.house_unit_codes)):
                    element = self.house_unit_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.house_unit_codes[i] = element.to_alipay_dict()
            if hasattr(self.house_unit_codes, 'to_alipay_dict'):
                params['house_unit_codes'] = self.house_unit_codes.to_alipay_dict()
            else:
                params['house_unit_codes'] = self.house_unit_codes
        if self.its_floor:
            if hasattr(self.its_floor, 'to_alipay_dict'):
                params['its_floor'] = self.its_floor.to_alipay_dict()
            else:
                params['its_floor'] = self.its_floor
        if self.land_cert_no:
            if hasattr(self.land_cert_no, 'to_alipay_dict'):
                params['land_cert_no'] = self.land_cert_no.to_alipay_dict()
            else:
                params['land_cert_no'] = self.land_cert_no
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.mortgaged:
            if hasattr(self.mortgaged, 'to_alipay_dict'):
                params['mortgaged'] = self.mortgaged.to_alipay_dict()
            else:
                params['mortgaged'] = self.mortgaged
        if self.owner_ship_status:
            if hasattr(self.owner_ship_status, 'to_alipay_dict'):
                params['owner_ship_status'] = self.owner_ship_status.to_alipay_dict()
            else:
                params['owner_ship_status'] = self.owner_ship_status
        if self.structure_area:
            if hasattr(self.structure_area, 'to_alipay_dict'):
                params['structure_area'] = self.structure_area.to_alipay_dict()
            else:
                params['structure_area'] = self.structure_area
        if self.structure_area_unit:
            if hasattr(self.structure_area_unit, 'to_alipay_dict'):
                params['structure_area_unit'] = self.structure_area_unit.to_alipay_dict()
            else:
                params['structure_area_unit'] = self.structure_area_unit
        if self.total_floor:
            if hasattr(self.total_floor, 'to_alipay_dict'):
                params['total_floor'] = self.total_floor.to_alipay_dict()
            else:
                params['total_floor'] = self.total_floor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = House()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'built_year' in d:
            o.built_year = d['built_year']
        if 'house_owners' in d:
            o.house_owners = d['house_owners']
        if 'house_unit_codes' in d:
            o.house_unit_codes = d['house_unit_codes']
        if 'its_floor' in d:
            o.its_floor = d['its_floor']
        if 'land_cert_no' in d:
            o.land_cert_no = d['land_cert_no']
        if 'location' in d:
            o.location = d['location']
        if 'mortgaged' in d:
            o.mortgaged = d['mortgaged']
        if 'owner_ship_status' in d:
            o.owner_ship_status = d['owner_ship_status']
        if 'structure_area' in d:
            o.structure_area = d['structure_area']
        if 'structure_area_unit' in d:
            o.structure_area_unit = d['structure_area_unit']
        if 'total_floor' in d:
            o.total_floor = d['total_floor']
        return o


