#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GeographyInfo import GeographyInfo
from alipay.aop.api.domain.GeographyInfo import GeographyInfo
from alipay.aop.api.domain.HosInfoInfo import HosInfoInfo
from alipay.aop.api.domain.GeographyInfo import GeographyInfo
from alipay.aop.api.domain.HosInfoInfo import HosInfoInfo


class ExtractItemScoreInfo(object):

    def __init__(self):
        self._city_info_list = None
        self._district_info_list = None
        self._hos_info_list = None
        self._province_info_list = None
        self._univ_department_info_list = None

    @property
    def city_info_list(self):
        return self._city_info_list

    @city_info_list.setter
    def city_info_list(self, value):
        if isinstance(value, list):
            self._city_info_list = list()
            for i in value:
                if isinstance(i, GeographyInfo):
                    self._city_info_list.append(i)
                else:
                    self._city_info_list.append(GeographyInfo.from_alipay_dict(i))
    @property
    def district_info_list(self):
        return self._district_info_list

    @district_info_list.setter
    def district_info_list(self, value):
        if isinstance(value, list):
            self._district_info_list = list()
            for i in value:
                if isinstance(i, GeographyInfo):
                    self._district_info_list.append(i)
                else:
                    self._district_info_list.append(GeographyInfo.from_alipay_dict(i))
    @property
    def hos_info_list(self):
        return self._hos_info_list

    @hos_info_list.setter
    def hos_info_list(self, value):
        if isinstance(value, list):
            self._hos_info_list = list()
            for i in value:
                if isinstance(i, HosInfoInfo):
                    self._hos_info_list.append(i)
                else:
                    self._hos_info_list.append(HosInfoInfo.from_alipay_dict(i))
    @property
    def province_info_list(self):
        return self._province_info_list

    @province_info_list.setter
    def province_info_list(self, value):
        if isinstance(value, list):
            self._province_info_list = list()
            for i in value:
                if isinstance(i, GeographyInfo):
                    self._province_info_list.append(i)
                else:
                    self._province_info_list.append(GeographyInfo.from_alipay_dict(i))
    @property
    def univ_department_info_list(self):
        return self._univ_department_info_list

    @univ_department_info_list.setter
    def univ_department_info_list(self, value):
        if isinstance(value, list):
            self._univ_department_info_list = list()
            for i in value:
                if isinstance(i, HosInfoInfo):
                    self._univ_department_info_list.append(i)
                else:
                    self._univ_department_info_list.append(HosInfoInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.city_info_list:
            if isinstance(self.city_info_list, list):
                for i in range(0, len(self.city_info_list)):
                    element = self.city_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_info_list[i] = element.to_alipay_dict()
            if hasattr(self.city_info_list, 'to_alipay_dict'):
                params['city_info_list'] = self.city_info_list.to_alipay_dict()
            else:
                params['city_info_list'] = self.city_info_list
        if self.district_info_list:
            if isinstance(self.district_info_list, list):
                for i in range(0, len(self.district_info_list)):
                    element = self.district_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.district_info_list[i] = element.to_alipay_dict()
            if hasattr(self.district_info_list, 'to_alipay_dict'):
                params['district_info_list'] = self.district_info_list.to_alipay_dict()
            else:
                params['district_info_list'] = self.district_info_list
        if self.hos_info_list:
            if isinstance(self.hos_info_list, list):
                for i in range(0, len(self.hos_info_list)):
                    element = self.hos_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hos_info_list[i] = element.to_alipay_dict()
            if hasattr(self.hos_info_list, 'to_alipay_dict'):
                params['hos_info_list'] = self.hos_info_list.to_alipay_dict()
            else:
                params['hos_info_list'] = self.hos_info_list
        if self.province_info_list:
            if isinstance(self.province_info_list, list):
                for i in range(0, len(self.province_info_list)):
                    element = self.province_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.province_info_list[i] = element.to_alipay_dict()
            if hasattr(self.province_info_list, 'to_alipay_dict'):
                params['province_info_list'] = self.province_info_list.to_alipay_dict()
            else:
                params['province_info_list'] = self.province_info_list
        if self.univ_department_info_list:
            if isinstance(self.univ_department_info_list, list):
                for i in range(0, len(self.univ_department_info_list)):
                    element = self.univ_department_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.univ_department_info_list[i] = element.to_alipay_dict()
            if hasattr(self.univ_department_info_list, 'to_alipay_dict'):
                params['univ_department_info_list'] = self.univ_department_info_list.to_alipay_dict()
            else:
                params['univ_department_info_list'] = self.univ_department_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtractItemScoreInfo()
        if 'city_info_list' in d:
            o.city_info_list = d['city_info_list']
        if 'district_info_list' in d:
            o.district_info_list = d['district_info_list']
        if 'hos_info_list' in d:
            o.hos_info_list = d['hos_info_list']
        if 'province_info_list' in d:
            o.province_info_list = d['province_info_list']
        if 'univ_department_info_list' in d:
            o.univ_department_info_list = d['univ_department_info_list']
        return o


