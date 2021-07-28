#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo
from alipay.aop.api.domain.HotelRoomInfo import HotelRoomInfo


class AlipayBusinessOrderCheckinOrderinfoSyncModel(object):

    def __init__(self):
        self._appid = None
        self._check_in_date = None
        self._check_in_time = None
        self._check_out_date = None
        self._check_out_time = None
        self._ext_info = None
        self._guest_name = None
        self._has_breakfast = None
        self._hotel_name = None
        self._member_level = None
        self._order_create_time = None
        self._order_id = None
        self._order_source = None
        self._order_status = None
        self._order_update_time = None
        self._outer_hotel_id = None
        self._outer_order_id = None
        self._remind_link = None
        self._room_info = None
        self._telephone = None
        self._uid = None

    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def check_in_date(self):
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self._check_in_date = value
    @property
    def check_in_time(self):
        return self._check_in_time

    @check_in_time.setter
    def check_in_time(self, value):
        self._check_in_time = value
    @property
    def check_out_date(self):
        return self._check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        self._check_out_date = value
    @property
    def check_out_time(self):
        return self._check_out_time

    @check_out_time.setter
    def check_out_time(self, value):
        self._check_out_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ScenicExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ScenicExtInfo.from_alipay_dict(i))
    @property
    def guest_name(self):
        return self._guest_name

    @guest_name.setter
    def guest_name(self, value):
        self._guest_name = value
    @property
    def has_breakfast(self):
        return self._has_breakfast

    @has_breakfast.setter
    def has_breakfast(self, value):
        self._has_breakfast = value
    @property
    def hotel_name(self):
        return self._hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self._hotel_name = value
    @property
    def member_level(self):
        return self._member_level

    @member_level.setter
    def member_level(self, value):
        self._member_level = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_update_time(self):
        return self._order_update_time

    @order_update_time.setter
    def order_update_time(self, value):
        self._order_update_time = value
    @property
    def outer_hotel_id(self):
        return self._outer_hotel_id

    @outer_hotel_id.setter
    def outer_hotel_id(self, value):
        self._outer_hotel_id = value
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def remind_link(self):
        return self._remind_link

    @remind_link.setter
    def remind_link(self, value):
        self._remind_link = value
    @property
    def room_info(self):
        return self._room_info

    @room_info.setter
    def room_info(self, value):
        if isinstance(value, list):
            self._room_info = list()
            for i in value:
                if isinstance(i, HotelRoomInfo):
                    self._room_info.append(i)
                else:
                    self._room_info.append(HotelRoomInfo.from_alipay_dict(i))
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.check_in_date:
            if hasattr(self.check_in_date, 'to_alipay_dict'):
                params['check_in_date'] = self.check_in_date.to_alipay_dict()
            else:
                params['check_in_date'] = self.check_in_date
        if self.check_in_time:
            if hasattr(self.check_in_time, 'to_alipay_dict'):
                params['check_in_time'] = self.check_in_time.to_alipay_dict()
            else:
                params['check_in_time'] = self.check_in_time
        if self.check_out_date:
            if hasattr(self.check_out_date, 'to_alipay_dict'):
                params['check_out_date'] = self.check_out_date.to_alipay_dict()
            else:
                params['check_out_date'] = self.check_out_date
        if self.check_out_time:
            if hasattr(self.check_out_time, 'to_alipay_dict'):
                params['check_out_time'] = self.check_out_time.to_alipay_dict()
            else:
                params['check_out_time'] = self.check_out_time
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.guest_name:
            if hasattr(self.guest_name, 'to_alipay_dict'):
                params['guest_name'] = self.guest_name.to_alipay_dict()
            else:
                params['guest_name'] = self.guest_name
        if self.has_breakfast:
            if hasattr(self.has_breakfast, 'to_alipay_dict'):
                params['has_breakfast'] = self.has_breakfast.to_alipay_dict()
            else:
                params['has_breakfast'] = self.has_breakfast
        if self.hotel_name:
            if hasattr(self.hotel_name, 'to_alipay_dict'):
                params['hotel_name'] = self.hotel_name.to_alipay_dict()
            else:
                params['hotel_name'] = self.hotel_name
        if self.member_level:
            if hasattr(self.member_level, 'to_alipay_dict'):
                params['member_level'] = self.member_level.to_alipay_dict()
            else:
                params['member_level'] = self.member_level
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_update_time:
            if hasattr(self.order_update_time, 'to_alipay_dict'):
                params['order_update_time'] = self.order_update_time.to_alipay_dict()
            else:
                params['order_update_time'] = self.order_update_time
        if self.outer_hotel_id:
            if hasattr(self.outer_hotel_id, 'to_alipay_dict'):
                params['outer_hotel_id'] = self.outer_hotel_id.to_alipay_dict()
            else:
                params['outer_hotel_id'] = self.outer_hotel_id
        if self.outer_order_id:
            if hasattr(self.outer_order_id, 'to_alipay_dict'):
                params['outer_order_id'] = self.outer_order_id.to_alipay_dict()
            else:
                params['outer_order_id'] = self.outer_order_id
        if self.remind_link:
            if hasattr(self.remind_link, 'to_alipay_dict'):
                params['remind_link'] = self.remind_link.to_alipay_dict()
            else:
                params['remind_link'] = self.remind_link
        if self.room_info:
            if isinstance(self.room_info, list):
                for i in range(0, len(self.room_info)):
                    element = self.room_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.room_info[i] = element.to_alipay_dict()
            if hasattr(self.room_info, 'to_alipay_dict'):
                params['room_info'] = self.room_info.to_alipay_dict()
            else:
                params['room_info'] = self.room_info
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessOrderCheckinOrderinfoSyncModel()
        if 'appid' in d:
            o.appid = d['appid']
        if 'check_in_date' in d:
            o.check_in_date = d['check_in_date']
        if 'check_in_time' in d:
            o.check_in_time = d['check_in_time']
        if 'check_out_date' in d:
            o.check_out_date = d['check_out_date']
        if 'check_out_time' in d:
            o.check_out_time = d['check_out_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'guest_name' in d:
            o.guest_name = d['guest_name']
        if 'has_breakfast' in d:
            o.has_breakfast = d['has_breakfast']
        if 'hotel_name' in d:
            o.hotel_name = d['hotel_name']
        if 'member_level' in d:
            o.member_level = d['member_level']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_update_time' in d:
            o.order_update_time = d['order_update_time']
        if 'outer_hotel_id' in d:
            o.outer_hotel_id = d['outer_hotel_id']
        if 'outer_order_id' in d:
            o.outer_order_id = d['outer_order_id']
        if 'remind_link' in d:
            o.remind_link = d['remind_link']
        if 'room_info' in d:
            o.room_info = d['room_info']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'uid' in d:
            o.uid = d['uid']
        return o


