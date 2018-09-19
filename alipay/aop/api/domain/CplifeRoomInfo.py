#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CplifeRoomInfo(object):

    def __init__(self):
        self._address = None
        self._building = None
        self._group = None
        self._out_room_id = None
        self._room = None
        self._unit = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def building(self):
        return self._building

    @building.setter
    def building(self, value):
        self._building = value
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
    @property
    def out_room_id(self):
        return self._out_room_id

    @out_room_id.setter
    def out_room_id(self, value):
        self._out_room_id = value
    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value):
        self._room = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.building:
            if hasattr(self.building, 'to_alipay_dict'):
                params['building'] = self.building.to_alipay_dict()
            else:
                params['building'] = self.building
        if self.group:
            if hasattr(self.group, 'to_alipay_dict'):
                params['group'] = self.group.to_alipay_dict()
            else:
                params['group'] = self.group
        if self.out_room_id:
            if hasattr(self.out_room_id, 'to_alipay_dict'):
                params['out_room_id'] = self.out_room_id.to_alipay_dict()
            else:
                params['out_room_id'] = self.out_room_id
        if self.room:
            if hasattr(self.room, 'to_alipay_dict'):
                params['room'] = self.room.to_alipay_dict()
            else:
                params['room'] = self.room
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CplifeRoomInfo()
        if 'address' in d:
            o.address = d['address']
        if 'building' in d:
            o.building = d['building']
        if 'group' in d:
            o.group = d['group']
        if 'out_room_id' in d:
            o.out_room_id = d['out_room_id']
        if 'room' in d:
            o.room = d['room']
        if 'unit' in d:
            o.unit = d['unit']
        return o


