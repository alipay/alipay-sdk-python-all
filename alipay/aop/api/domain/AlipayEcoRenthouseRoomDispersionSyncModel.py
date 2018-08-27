#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcoRenthouseOtherAmount import EcoRenthouseOtherAmount
from alipay.aop.api.domain.EcoDisRenthousepayTypeList import EcoDisRenthousepayTypeList


class AlipayEcoRenthouseRoomDispersionSyncModel(object):

    def __init__(self):
        self._ali_short_num = None
        self._bedroom_count = None
        self._checkin_time = None
        self._comm_req_id = None
        self._commission = None
        self._commission_type = None
        self._community_code = None
        self._fee_remark = None
        self._flat_area = None
        self._flat_building = None
        self._flat_configs = None
        self._flat_unit = None
        self._floor_count = None
        self._foregift_amount = None
        self._free_begin_date = None
        self._free_end_date = None
        self._images = None
        self._intro = None
        self._max_lease_time = None
        self._min_rent_days = None
        self._other_amount = None
        self._owners_name = None
        self._owners_tel = None
        self._parlor_count = None
        self._pay_type = None
        self._pay_type_list = None
        self._rent_status = None
        self._rent_type = None
        self._room_amount = None
        self._room_area = None
        self._room_code = None
        self._room_configs = None
        self._room_face = None
        self._room_name = None
        self._room_num = None
        self._room_status = None
        self._room_store_no = None
        self._toilet_count = None
        self._total_floor_count = None

    @property
    def ali_short_num(self):
        return self._ali_short_num

    @ali_short_num.setter
    def ali_short_num(self, value):
        self._ali_short_num = value
    @property
    def bedroom_count(self):
        return self._bedroom_count

    @bedroom_count.setter
    def bedroom_count(self, value):
        self._bedroom_count = value
    @property
    def checkin_time(self):
        return self._checkin_time

    @checkin_time.setter
    def checkin_time(self, value):
        self._checkin_time = value
    @property
    def comm_req_id(self):
        return self._comm_req_id

    @comm_req_id.setter
    def comm_req_id(self, value):
        self._comm_req_id = value
    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value):
        self._commission = value
    @property
    def commission_type(self):
        return self._commission_type

    @commission_type.setter
    def commission_type(self, value):
        self._commission_type = value
    @property
    def community_code(self):
        return self._community_code

    @community_code.setter
    def community_code(self, value):
        self._community_code = value
    @property
    def fee_remark(self):
        return self._fee_remark

    @fee_remark.setter
    def fee_remark(self, value):
        self._fee_remark = value
    @property
    def flat_area(self):
        return self._flat_area

    @flat_area.setter
    def flat_area(self, value):
        self._flat_area = value
    @property
    def flat_building(self):
        return self._flat_building

    @flat_building.setter
    def flat_building(self, value):
        self._flat_building = value
    @property
    def flat_configs(self):
        return self._flat_configs

    @flat_configs.setter
    def flat_configs(self, value):
        if isinstance(value, list):
            self._flat_configs = list()
            for i in value:
                self._flat_configs.append(i)
    @property
    def flat_unit(self):
        return self._flat_unit

    @flat_unit.setter
    def flat_unit(self, value):
        self._flat_unit = value
    @property
    def floor_count(self):
        return self._floor_count

    @floor_count.setter
    def floor_count(self, value):
        self._floor_count = value
    @property
    def foregift_amount(self):
        return self._foregift_amount

    @foregift_amount.setter
    def foregift_amount(self, value):
        self._foregift_amount = value
    @property
    def free_begin_date(self):
        return self._free_begin_date

    @free_begin_date.setter
    def free_begin_date(self, value):
        self._free_begin_date = value
    @property
    def free_end_date(self):
        return self._free_end_date

    @free_end_date.setter
    def free_end_date(self, value):
        self._free_end_date = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
    @property
    def intro(self):
        return self._intro

    @intro.setter
    def intro(self, value):
        self._intro = value
    @property
    def max_lease_time(self):
        return self._max_lease_time

    @max_lease_time.setter
    def max_lease_time(self, value):
        self._max_lease_time = value
    @property
    def min_rent_days(self):
        return self._min_rent_days

    @min_rent_days.setter
    def min_rent_days(self, value):
        self._min_rent_days = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        if isinstance(value, list):
            self._other_amount = list()
            for i in value:
                if isinstance(i, EcoRenthouseOtherAmount):
                    self._other_amount.append(i)
                else:
                    self._other_amount.append(EcoRenthouseOtherAmount.from_alipay_dict(i))
    @property
    def owners_name(self):
        return self._owners_name

    @owners_name.setter
    def owners_name(self, value):
        self._owners_name = value
    @property
    def owners_tel(self):
        return self._owners_tel

    @owners_tel.setter
    def owners_tel(self, value):
        self._owners_tel = value
    @property
    def parlor_count(self):
        return self._parlor_count

    @parlor_count.setter
    def parlor_count(self, value):
        self._parlor_count = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def pay_type_list(self):
        return self._pay_type_list

    @pay_type_list.setter
    def pay_type_list(self, value):
        if isinstance(value, list):
            self._pay_type_list = list()
            for i in value:
                if isinstance(i, EcoDisRenthousepayTypeList):
                    self._pay_type_list.append(i)
                else:
                    self._pay_type_list.append(EcoDisRenthousepayTypeList.from_alipay_dict(i))
    @property
    def rent_status(self):
        return self._rent_status

    @rent_status.setter
    def rent_status(self, value):
        self._rent_status = value
    @property
    def rent_type(self):
        return self._rent_type

    @rent_type.setter
    def rent_type(self, value):
        self._rent_type = value
    @property
    def room_amount(self):
        return self._room_amount

    @room_amount.setter
    def room_amount(self, value):
        self._room_amount = value
    @property
    def room_area(self):
        return self._room_area

    @room_area.setter
    def room_area(self, value):
        self._room_area = value
    @property
    def room_code(self):
        return self._room_code

    @room_code.setter
    def room_code(self, value):
        self._room_code = value
    @property
    def room_configs(self):
        return self._room_configs

    @room_configs.setter
    def room_configs(self, value):
        if isinstance(value, list):
            self._room_configs = list()
            for i in value:
                self._room_configs.append(i)
    @property
    def room_face(self):
        return self._room_face

    @room_face.setter
    def room_face(self, value):
        self._room_face = value
    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, value):
        self._room_name = value
    @property
    def room_num(self):
        return self._room_num

    @room_num.setter
    def room_num(self, value):
        self._room_num = value
    @property
    def room_status(self):
        return self._room_status

    @room_status.setter
    def room_status(self, value):
        self._room_status = value
    @property
    def room_store_no(self):
        return self._room_store_no

    @room_store_no.setter
    def room_store_no(self, value):
        self._room_store_no = value
    @property
    def toilet_count(self):
        return self._toilet_count

    @toilet_count.setter
    def toilet_count(self, value):
        self._toilet_count = value
    @property
    def total_floor_count(self):
        return self._total_floor_count

    @total_floor_count.setter
    def total_floor_count(self, value):
        self._total_floor_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.ali_short_num:
            if hasattr(self.ali_short_num, 'to_alipay_dict'):
                params['ali_short_num'] = self.ali_short_num.to_alipay_dict()
            else:
                params['ali_short_num'] = self.ali_short_num
        if self.bedroom_count:
            if hasattr(self.bedroom_count, 'to_alipay_dict'):
                params['bedroom_count'] = self.bedroom_count.to_alipay_dict()
            else:
                params['bedroom_count'] = self.bedroom_count
        if self.checkin_time:
            if hasattr(self.checkin_time, 'to_alipay_dict'):
                params['checkin_time'] = self.checkin_time.to_alipay_dict()
            else:
                params['checkin_time'] = self.checkin_time
        if self.comm_req_id:
            if hasattr(self.comm_req_id, 'to_alipay_dict'):
                params['comm_req_id'] = self.comm_req_id.to_alipay_dict()
            else:
                params['comm_req_id'] = self.comm_req_id
        if self.commission:
            if hasattr(self.commission, 'to_alipay_dict'):
                params['commission'] = self.commission.to_alipay_dict()
            else:
                params['commission'] = self.commission
        if self.commission_type:
            if hasattr(self.commission_type, 'to_alipay_dict'):
                params['commission_type'] = self.commission_type.to_alipay_dict()
            else:
                params['commission_type'] = self.commission_type
        if self.community_code:
            if hasattr(self.community_code, 'to_alipay_dict'):
                params['community_code'] = self.community_code.to_alipay_dict()
            else:
                params['community_code'] = self.community_code
        if self.fee_remark:
            if hasattr(self.fee_remark, 'to_alipay_dict'):
                params['fee_remark'] = self.fee_remark.to_alipay_dict()
            else:
                params['fee_remark'] = self.fee_remark
        if self.flat_area:
            if hasattr(self.flat_area, 'to_alipay_dict'):
                params['flat_area'] = self.flat_area.to_alipay_dict()
            else:
                params['flat_area'] = self.flat_area
        if self.flat_building:
            if hasattr(self.flat_building, 'to_alipay_dict'):
                params['flat_building'] = self.flat_building.to_alipay_dict()
            else:
                params['flat_building'] = self.flat_building
        if self.flat_configs:
            if isinstance(self.flat_configs, list):
                for i in range(0, len(self.flat_configs)):
                    element = self.flat_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.flat_configs[i] = element.to_alipay_dict()
            if hasattr(self.flat_configs, 'to_alipay_dict'):
                params['flat_configs'] = self.flat_configs.to_alipay_dict()
            else:
                params['flat_configs'] = self.flat_configs
        if self.flat_unit:
            if hasattr(self.flat_unit, 'to_alipay_dict'):
                params['flat_unit'] = self.flat_unit.to_alipay_dict()
            else:
                params['flat_unit'] = self.flat_unit
        if self.floor_count:
            if hasattr(self.floor_count, 'to_alipay_dict'):
                params['floor_count'] = self.floor_count.to_alipay_dict()
            else:
                params['floor_count'] = self.floor_count
        if self.foregift_amount:
            if hasattr(self.foregift_amount, 'to_alipay_dict'):
                params['foregift_amount'] = self.foregift_amount.to_alipay_dict()
            else:
                params['foregift_amount'] = self.foregift_amount
        if self.free_begin_date:
            if hasattr(self.free_begin_date, 'to_alipay_dict'):
                params['free_begin_date'] = self.free_begin_date.to_alipay_dict()
            else:
                params['free_begin_date'] = self.free_begin_date
        if self.free_end_date:
            if hasattr(self.free_end_date, 'to_alipay_dict'):
                params['free_end_date'] = self.free_end_date.to_alipay_dict()
            else:
                params['free_end_date'] = self.free_end_date
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.intro:
            if hasattr(self.intro, 'to_alipay_dict'):
                params['intro'] = self.intro.to_alipay_dict()
            else:
                params['intro'] = self.intro
        if self.max_lease_time:
            if hasattr(self.max_lease_time, 'to_alipay_dict'):
                params['max_lease_time'] = self.max_lease_time.to_alipay_dict()
            else:
                params['max_lease_time'] = self.max_lease_time
        if self.min_rent_days:
            if hasattr(self.min_rent_days, 'to_alipay_dict'):
                params['min_rent_days'] = self.min_rent_days.to_alipay_dict()
            else:
                params['min_rent_days'] = self.min_rent_days
        if self.other_amount:
            if isinstance(self.other_amount, list):
                for i in range(0, len(self.other_amount)):
                    element = self.other_amount[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_amount[i] = element.to_alipay_dict()
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.owners_name:
            if hasattr(self.owners_name, 'to_alipay_dict'):
                params['owners_name'] = self.owners_name.to_alipay_dict()
            else:
                params['owners_name'] = self.owners_name
        if self.owners_tel:
            if hasattr(self.owners_tel, 'to_alipay_dict'):
                params['owners_tel'] = self.owners_tel.to_alipay_dict()
            else:
                params['owners_tel'] = self.owners_tel
        if self.parlor_count:
            if hasattr(self.parlor_count, 'to_alipay_dict'):
                params['parlor_count'] = self.parlor_count.to_alipay_dict()
            else:
                params['parlor_count'] = self.parlor_count
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.pay_type_list:
            if isinstance(self.pay_type_list, list):
                for i in range(0, len(self.pay_type_list)):
                    element = self.pay_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_type_list[i] = element.to_alipay_dict()
            if hasattr(self.pay_type_list, 'to_alipay_dict'):
                params['pay_type_list'] = self.pay_type_list.to_alipay_dict()
            else:
                params['pay_type_list'] = self.pay_type_list
        if self.rent_status:
            if hasattr(self.rent_status, 'to_alipay_dict'):
                params['rent_status'] = self.rent_status.to_alipay_dict()
            else:
                params['rent_status'] = self.rent_status
        if self.rent_type:
            if hasattr(self.rent_type, 'to_alipay_dict'):
                params['rent_type'] = self.rent_type.to_alipay_dict()
            else:
                params['rent_type'] = self.rent_type
        if self.room_amount:
            if hasattr(self.room_amount, 'to_alipay_dict'):
                params['room_amount'] = self.room_amount.to_alipay_dict()
            else:
                params['room_amount'] = self.room_amount
        if self.room_area:
            if hasattr(self.room_area, 'to_alipay_dict'):
                params['room_area'] = self.room_area.to_alipay_dict()
            else:
                params['room_area'] = self.room_area
        if self.room_code:
            if hasattr(self.room_code, 'to_alipay_dict'):
                params['room_code'] = self.room_code.to_alipay_dict()
            else:
                params['room_code'] = self.room_code
        if self.room_configs:
            if isinstance(self.room_configs, list):
                for i in range(0, len(self.room_configs)):
                    element = self.room_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.room_configs[i] = element.to_alipay_dict()
            if hasattr(self.room_configs, 'to_alipay_dict'):
                params['room_configs'] = self.room_configs.to_alipay_dict()
            else:
                params['room_configs'] = self.room_configs
        if self.room_face:
            if hasattr(self.room_face, 'to_alipay_dict'):
                params['room_face'] = self.room_face.to_alipay_dict()
            else:
                params['room_face'] = self.room_face
        if self.room_name:
            if hasattr(self.room_name, 'to_alipay_dict'):
                params['room_name'] = self.room_name.to_alipay_dict()
            else:
                params['room_name'] = self.room_name
        if self.room_num:
            if hasattr(self.room_num, 'to_alipay_dict'):
                params['room_num'] = self.room_num.to_alipay_dict()
            else:
                params['room_num'] = self.room_num
        if self.room_status:
            if hasattr(self.room_status, 'to_alipay_dict'):
                params['room_status'] = self.room_status.to_alipay_dict()
            else:
                params['room_status'] = self.room_status
        if self.room_store_no:
            if hasattr(self.room_store_no, 'to_alipay_dict'):
                params['room_store_no'] = self.room_store_no.to_alipay_dict()
            else:
                params['room_store_no'] = self.room_store_no
        if self.toilet_count:
            if hasattr(self.toilet_count, 'to_alipay_dict'):
                params['toilet_count'] = self.toilet_count.to_alipay_dict()
            else:
                params['toilet_count'] = self.toilet_count
        if self.total_floor_count:
            if hasattr(self.total_floor_count, 'to_alipay_dict'):
                params['total_floor_count'] = self.total_floor_count.to_alipay_dict()
            else:
                params['total_floor_count'] = self.total_floor_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseRoomDispersionSyncModel()
        if 'ali_short_num' in d:
            o.ali_short_num = d['ali_short_num']
        if 'bedroom_count' in d:
            o.bedroom_count = d['bedroom_count']
        if 'checkin_time' in d:
            o.checkin_time = d['checkin_time']
        if 'comm_req_id' in d:
            o.comm_req_id = d['comm_req_id']
        if 'commission' in d:
            o.commission = d['commission']
        if 'commission_type' in d:
            o.commission_type = d['commission_type']
        if 'community_code' in d:
            o.community_code = d['community_code']
        if 'fee_remark' in d:
            o.fee_remark = d['fee_remark']
        if 'flat_area' in d:
            o.flat_area = d['flat_area']
        if 'flat_building' in d:
            o.flat_building = d['flat_building']
        if 'flat_configs' in d:
            o.flat_configs = d['flat_configs']
        if 'flat_unit' in d:
            o.flat_unit = d['flat_unit']
        if 'floor_count' in d:
            o.floor_count = d['floor_count']
        if 'foregift_amount' in d:
            o.foregift_amount = d['foregift_amount']
        if 'free_begin_date' in d:
            o.free_begin_date = d['free_begin_date']
        if 'free_end_date' in d:
            o.free_end_date = d['free_end_date']
        if 'images' in d:
            o.images = d['images']
        if 'intro' in d:
            o.intro = d['intro']
        if 'max_lease_time' in d:
            o.max_lease_time = d['max_lease_time']
        if 'min_rent_days' in d:
            o.min_rent_days = d['min_rent_days']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'owners_name' in d:
            o.owners_name = d['owners_name']
        if 'owners_tel' in d:
            o.owners_tel = d['owners_tel']
        if 'parlor_count' in d:
            o.parlor_count = d['parlor_count']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'pay_type_list' in d:
            o.pay_type_list = d['pay_type_list']
        if 'rent_status' in d:
            o.rent_status = d['rent_status']
        if 'rent_type' in d:
            o.rent_type = d['rent_type']
        if 'room_amount' in d:
            o.room_amount = d['room_amount']
        if 'room_area' in d:
            o.room_area = d['room_area']
        if 'room_code' in d:
            o.room_code = d['room_code']
        if 'room_configs' in d:
            o.room_configs = d['room_configs']
        if 'room_face' in d:
            o.room_face = d['room_face']
        if 'room_name' in d:
            o.room_name = d['room_name']
        if 'room_num' in d:
            o.room_num = d['room_num']
        if 'room_status' in d:
            o.room_status = d['room_status']
        if 'room_store_no' in d:
            o.room_store_no = d['room_store_no']
        if 'toilet_count' in d:
            o.toilet_count = d['toilet_count']
        if 'total_floor_count' in d:
            o.total_floor_count = d['total_floor_count']
        return o


