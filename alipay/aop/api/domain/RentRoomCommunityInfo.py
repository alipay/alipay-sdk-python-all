#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AreaAddressInfo import AreaAddressInfo
from alipay.aop.api.domain.CommunityBasicInfo import CommunityBasicInfo
from alipay.aop.api.domain.CommunityPicInfo import CommunityPicInfo


class RentRoomCommunityInfo(object):

    def __init__(self):
        self._area_address_info = None
        self._community_basic_info = None
        self._community_equipment_info = None
        self._community_introduce = None
        self._community_name = None
        self._community_pic_info = None

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
    def community_basic_info(self):
        return self._community_basic_info

    @community_basic_info.setter
    def community_basic_info(self, value):
        if isinstance(value, CommunityBasicInfo):
            self._community_basic_info = value
        else:
            self._community_basic_info = CommunityBasicInfo.from_alipay_dict(value)
    @property
    def community_equipment_info(self):
        return self._community_equipment_info

    @community_equipment_info.setter
    def community_equipment_info(self, value):
        if isinstance(value, list):
            self._community_equipment_info = list()
            for i in value:
                self._community_equipment_info.append(i)
    @property
    def community_introduce(self):
        return self._community_introduce

    @community_introduce.setter
    def community_introduce(self, value):
        self._community_introduce = value
    @property
    def community_name(self):
        return self._community_name

    @community_name.setter
    def community_name(self, value):
        self._community_name = value
    @property
    def community_pic_info(self):
        return self._community_pic_info

    @community_pic_info.setter
    def community_pic_info(self, value):
        if isinstance(value, CommunityPicInfo):
            self._community_pic_info = value
        else:
            self._community_pic_info = CommunityPicInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.area_address_info:
            if hasattr(self.area_address_info, 'to_alipay_dict'):
                params['area_address_info'] = self.area_address_info.to_alipay_dict()
            else:
                params['area_address_info'] = self.area_address_info
        if self.community_basic_info:
            if hasattr(self.community_basic_info, 'to_alipay_dict'):
                params['community_basic_info'] = self.community_basic_info.to_alipay_dict()
            else:
                params['community_basic_info'] = self.community_basic_info
        if self.community_equipment_info:
            if isinstance(self.community_equipment_info, list):
                for i in range(0, len(self.community_equipment_info)):
                    element = self.community_equipment_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.community_equipment_info[i] = element.to_alipay_dict()
            if hasattr(self.community_equipment_info, 'to_alipay_dict'):
                params['community_equipment_info'] = self.community_equipment_info.to_alipay_dict()
            else:
                params['community_equipment_info'] = self.community_equipment_info
        if self.community_introduce:
            if hasattr(self.community_introduce, 'to_alipay_dict'):
                params['community_introduce'] = self.community_introduce.to_alipay_dict()
            else:
                params['community_introduce'] = self.community_introduce
        if self.community_name:
            if hasattr(self.community_name, 'to_alipay_dict'):
                params['community_name'] = self.community_name.to_alipay_dict()
            else:
                params['community_name'] = self.community_name
        if self.community_pic_info:
            if hasattr(self.community_pic_info, 'to_alipay_dict'):
                params['community_pic_info'] = self.community_pic_info.to_alipay_dict()
            else:
                params['community_pic_info'] = self.community_pic_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRoomCommunityInfo()
        if 'area_address_info' in d:
            o.area_address_info = d['area_address_info']
        if 'community_basic_info' in d:
            o.community_basic_info = d['community_basic_info']
        if 'community_equipment_info' in d:
            o.community_equipment_info = d['community_equipment_info']
        if 'community_introduce' in d:
            o.community_introduce = d['community_introduce']
        if 'community_name' in d:
            o.community_name = d['community_name']
        if 'community_pic_info' in d:
            o.community_pic_info = d['community_pic_info']
        return o


