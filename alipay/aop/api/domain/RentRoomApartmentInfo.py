#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApartmentPicInfo import ApartmentPicInfo
from alipay.aop.api.domain.AreaAddressInfo import AreaAddressInfo
from alipay.aop.api.domain.ApartmentContactInfo import ApartmentContactInfo


class RentRoomApartmentInfo(object):

    def __init__(self):
        self._apartment_equipment_info = None
        self._apartment_introduce = None
        self._apartment_name = None
        self._apartment_pic_info = None
        self._area_address_info = None
        self._contact_info_list = None

    @property
    def apartment_equipment_info(self):
        return self._apartment_equipment_info

    @apartment_equipment_info.setter
    def apartment_equipment_info(self, value):
        if isinstance(value, list):
            self._apartment_equipment_info = list()
            for i in value:
                self._apartment_equipment_info.append(i)
    @property
    def apartment_introduce(self):
        return self._apartment_introduce

    @apartment_introduce.setter
    def apartment_introduce(self, value):
        self._apartment_introduce = value
    @property
    def apartment_name(self):
        return self._apartment_name

    @apartment_name.setter
    def apartment_name(self, value):
        self._apartment_name = value
    @property
    def apartment_pic_info(self):
        return self._apartment_pic_info

    @apartment_pic_info.setter
    def apartment_pic_info(self, value):
        if isinstance(value, ApartmentPicInfo):
            self._apartment_pic_info = value
        else:
            self._apartment_pic_info = ApartmentPicInfo.from_alipay_dict(value)
    @property
    def area_address_info(self):
        return self._area_address_info

    @area_address_info.setter
    def area_address_info(self, value):
        if isinstance(value, AreaAddressInfo):
            self._area_address_info = value
        else:
            self._area_address_info = AreaAddressInfo.from_alipay_dict(value)
    @property
    def contact_info_list(self):
        return self._contact_info_list

    @contact_info_list.setter
    def contact_info_list(self, value):
        if isinstance(value, list):
            self._contact_info_list = list()
            for i in value:
                if isinstance(i, ApartmentContactInfo):
                    self._contact_info_list.append(i)
                else:
                    self._contact_info_list.append(ApartmentContactInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apartment_equipment_info:
            if isinstance(self.apartment_equipment_info, list):
                for i in range(0, len(self.apartment_equipment_info)):
                    element = self.apartment_equipment_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apartment_equipment_info[i] = element.to_alipay_dict()
            if hasattr(self.apartment_equipment_info, 'to_alipay_dict'):
                params['apartment_equipment_info'] = self.apartment_equipment_info.to_alipay_dict()
            else:
                params['apartment_equipment_info'] = self.apartment_equipment_info
        if self.apartment_introduce:
            if hasattr(self.apartment_introduce, 'to_alipay_dict'):
                params['apartment_introduce'] = self.apartment_introduce.to_alipay_dict()
            else:
                params['apartment_introduce'] = self.apartment_introduce
        if self.apartment_name:
            if hasattr(self.apartment_name, 'to_alipay_dict'):
                params['apartment_name'] = self.apartment_name.to_alipay_dict()
            else:
                params['apartment_name'] = self.apartment_name
        if self.apartment_pic_info:
            if hasattr(self.apartment_pic_info, 'to_alipay_dict'):
                params['apartment_pic_info'] = self.apartment_pic_info.to_alipay_dict()
            else:
                params['apartment_pic_info'] = self.apartment_pic_info
        if self.area_address_info:
            if hasattr(self.area_address_info, 'to_alipay_dict'):
                params['area_address_info'] = self.area_address_info.to_alipay_dict()
            else:
                params['area_address_info'] = self.area_address_info
        if self.contact_info_list:
            if isinstance(self.contact_info_list, list):
                for i in range(0, len(self.contact_info_list)):
                    element = self.contact_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_info_list[i] = element.to_alipay_dict()
            if hasattr(self.contact_info_list, 'to_alipay_dict'):
                params['contact_info_list'] = self.contact_info_list.to_alipay_dict()
            else:
                params['contact_info_list'] = self.contact_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRoomApartmentInfo()
        if 'apartment_equipment_info' in d:
            o.apartment_equipment_info = d['apartment_equipment_info']
        if 'apartment_introduce' in d:
            o.apartment_introduce = d['apartment_introduce']
        if 'apartment_name' in d:
            o.apartment_name = d['apartment_name']
        if 'apartment_pic_info' in d:
            o.apartment_pic_info = d['apartment_pic_info']
        if 'area_address_info' in d:
            o.area_address_info = d['area_address_info']
        if 'contact_info_list' in d:
            o.contact_info_list = d['contact_info_list']
        return o


