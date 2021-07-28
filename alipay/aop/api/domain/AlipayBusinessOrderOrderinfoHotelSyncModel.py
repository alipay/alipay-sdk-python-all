#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Passenger import Passenger
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo
from alipay.aop.api.domain.Room import Room


class AlipayBusinessOrderOrderinfoHotelSyncModel(object):

    def __init__(self):
        self._amount = None
        self._appid = None
        self._booker = None
        self._cancel_rule_description = None
        self._cancel_rule_name = None
        self._check_in_date = None
        self._check_in_time = None
        self._check_out_date = None
        self._check_out_time = None
        self._discount_amount = None
        self._ext_info = None
        self._membership_card_template_id = None
        self._membership_grade = None
        self._order_create_time = None
        self._order_id = None
        self._order_link = None
        self._order_source = None
        self._order_status = None
        self._order_update_time = None
        self._outer_hotel_id = None
        self._outer_order_id = None
        self._pid = None
        self._plan_check_in_date = None
        self._rooms = None
        self._trade_id = None
        self._uid = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def booker(self):
        return self._booker

    @booker.setter
    def booker(self, value):
        if isinstance(value, Passenger):
            self._booker = value
        else:
            self._booker = Passenger.from_alipay_dict(value)
    @property
    def cancel_rule_description(self):
        return self._cancel_rule_description

    @cancel_rule_description.setter
    def cancel_rule_description(self, value):
        self._cancel_rule_description = value
    @property
    def cancel_rule_name(self):
        return self._cancel_rule_name

    @cancel_rule_name.setter
    def cancel_rule_name(self, value):
        self._cancel_rule_name = value
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
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
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
    def membership_card_template_id(self):
        return self._membership_card_template_id

    @membership_card_template_id.setter
    def membership_card_template_id(self, value):
        self._membership_card_template_id = value
    @property
    def membership_grade(self):
        return self._membership_grade

    @membership_grade.setter
    def membership_grade(self, value):
        self._membership_grade = value
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
    def order_link(self):
        return self._order_link

    @order_link.setter
    def order_link(self, value):
        self._order_link = value
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
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def plan_check_in_date(self):
        return self._plan_check_in_date

    @plan_check_in_date.setter
    def plan_check_in_date(self, value):
        self._plan_check_in_date = value
    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        if isinstance(value, list):
            self._rooms = list()
            for i in value:
                if isinstance(i, Room):
                    self._rooms.append(i)
                else:
                    self._rooms.append(Room.from_alipay_dict(i))
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.booker:
            if hasattr(self.booker, 'to_alipay_dict'):
                params['booker'] = self.booker.to_alipay_dict()
            else:
                params['booker'] = self.booker
        if self.cancel_rule_description:
            if hasattr(self.cancel_rule_description, 'to_alipay_dict'):
                params['cancel_rule_description'] = self.cancel_rule_description.to_alipay_dict()
            else:
                params['cancel_rule_description'] = self.cancel_rule_description
        if self.cancel_rule_name:
            if hasattr(self.cancel_rule_name, 'to_alipay_dict'):
                params['cancel_rule_name'] = self.cancel_rule_name.to_alipay_dict()
            else:
                params['cancel_rule_name'] = self.cancel_rule_name
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
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
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
        if self.membership_card_template_id:
            if hasattr(self.membership_card_template_id, 'to_alipay_dict'):
                params['membership_card_template_id'] = self.membership_card_template_id.to_alipay_dict()
            else:
                params['membership_card_template_id'] = self.membership_card_template_id
        if self.membership_grade:
            if hasattr(self.membership_grade, 'to_alipay_dict'):
                params['membership_grade'] = self.membership_grade.to_alipay_dict()
            else:
                params['membership_grade'] = self.membership_grade
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
        if self.order_link:
            if hasattr(self.order_link, 'to_alipay_dict'):
                params['order_link'] = self.order_link.to_alipay_dict()
            else:
                params['order_link'] = self.order_link
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
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.plan_check_in_date:
            if hasattr(self.plan_check_in_date, 'to_alipay_dict'):
                params['plan_check_in_date'] = self.plan_check_in_date.to_alipay_dict()
            else:
                params['plan_check_in_date'] = self.plan_check_in_date
        if self.rooms:
            if isinstance(self.rooms, list):
                for i in range(0, len(self.rooms)):
                    element = self.rooms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rooms[i] = element.to_alipay_dict()
            if hasattr(self.rooms, 'to_alipay_dict'):
                params['rooms'] = self.rooms.to_alipay_dict()
            else:
                params['rooms'] = self.rooms
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
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
        o = AlipayBusinessOrderOrderinfoHotelSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'appid' in d:
            o.appid = d['appid']
        if 'booker' in d:
            o.booker = d['booker']
        if 'cancel_rule_description' in d:
            o.cancel_rule_description = d['cancel_rule_description']
        if 'cancel_rule_name' in d:
            o.cancel_rule_name = d['cancel_rule_name']
        if 'check_in_date' in d:
            o.check_in_date = d['check_in_date']
        if 'check_in_time' in d:
            o.check_in_time = d['check_in_time']
        if 'check_out_date' in d:
            o.check_out_date = d['check_out_date']
        if 'check_out_time' in d:
            o.check_out_time = d['check_out_time']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'membership_card_template_id' in d:
            o.membership_card_template_id = d['membership_card_template_id']
        if 'membership_grade' in d:
            o.membership_grade = d['membership_grade']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_link' in d:
            o.order_link = d['order_link']
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
        if 'pid' in d:
            o.pid = d['pid']
        if 'plan_check_in_date' in d:
            o.plan_check_in_date = d['plan_check_in_date']
        if 'rooms' in d:
            o.rooms = d['rooms']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'uid' in d:
            o.uid = d['uid']
        return o


