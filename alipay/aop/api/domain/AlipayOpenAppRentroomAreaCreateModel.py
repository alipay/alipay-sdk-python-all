#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentRoomApartmentInfo import RentRoomApartmentInfo
from alipay.aop.api.domain.RentRoomCommunityInfo import RentRoomCommunityInfo


class AlipayOpenAppRentroomAreaCreateModel(object):

    def __init__(self):
        self._apartment_info = None
        self._area_type = None
        self._community_info = None
        self._out_area_id = None

    @property
    def apartment_info(self):
        return self._apartment_info

    @apartment_info.setter
    def apartment_info(self, value):
        if isinstance(value, RentRoomApartmentInfo):
            self._apartment_info = value
        else:
            self._apartment_info = RentRoomApartmentInfo.from_alipay_dict(value)
    @property
    def area_type(self):
        return self._area_type

    @area_type.setter
    def area_type(self, value):
        self._area_type = value
    @property
    def community_info(self):
        return self._community_info

    @community_info.setter
    def community_info(self, value):
        if isinstance(value, RentRoomCommunityInfo):
            self._community_info = value
        else:
            self._community_info = RentRoomCommunityInfo.from_alipay_dict(value)
    @property
    def out_area_id(self):
        return self._out_area_id

    @out_area_id.setter
    def out_area_id(self, value):
        self._out_area_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apartment_info:
            if hasattr(self.apartment_info, 'to_alipay_dict'):
                params['apartment_info'] = self.apartment_info.to_alipay_dict()
            else:
                params['apartment_info'] = self.apartment_info
        if self.area_type:
            if hasattr(self.area_type, 'to_alipay_dict'):
                params['area_type'] = self.area_type.to_alipay_dict()
            else:
                params['area_type'] = self.area_type
        if self.community_info:
            if hasattr(self.community_info, 'to_alipay_dict'):
                params['community_info'] = self.community_info.to_alipay_dict()
            else:
                params['community_info'] = self.community_info
        if self.out_area_id:
            if hasattr(self.out_area_id, 'to_alipay_dict'):
                params['out_area_id'] = self.out_area_id.to_alipay_dict()
            else:
                params['out_area_id'] = self.out_area_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppRentroomAreaCreateModel()
        if 'apartment_info' in d:
            o.apartment_info = d['apartment_info']
        if 'area_type' in d:
            o.area_type = d['area_type']
        if 'community_info' in d:
            o.community_info = d['community_info']
        if 'out_area_id' in d:
            o.out_area_id = d['out_area_id']
        return o


