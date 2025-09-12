#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHotelLockerDeviceSyncModel(object):

    def __init__(self):
        self._alipay_org_id = None
        self._building_id = None
        self._building_name = None
        self._building_no = None
        self._device_id = None
        self._device_isv_code = None
        self._device_name = None
        self._device_p_code = None
        self._device_sn = None
        self._device_type = None
        self._effective = None
        self._floor = None
        self._isv_org_id = None
        self._open_type = None
        self._operators_code = None
        self._org_group_code = None
        self._room_name = None
        self._room_no = None
        self._team_name = None

    @property
    def alipay_org_id(self):
        return self._alipay_org_id

    @alipay_org_id.setter
    def alipay_org_id(self, value):
        self._alipay_org_id = value
    @property
    def building_id(self):
        return self._building_id

    @building_id.setter
    def building_id(self, value):
        self._building_id = value
    @property
    def building_name(self):
        return self._building_name

    @building_name.setter
    def building_name(self, value):
        self._building_name = value
    @property
    def building_no(self):
        return self._building_no

    @building_no.setter
    def building_no(self, value):
        self._building_no = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_isv_code(self):
        return self._device_isv_code

    @device_isv_code.setter
    def device_isv_code(self, value):
        self._device_isv_code = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_p_code(self):
        return self._device_p_code

    @device_p_code.setter
    def device_p_code(self, value):
        self._device_p_code = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def effective(self):
        return self._effective

    @effective.setter
    def effective(self, value):
        self._effective = value
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value
    @property
    def isv_org_id(self):
        return self._isv_org_id

    @isv_org_id.setter
    def isv_org_id(self, value):
        self._isv_org_id = value
    @property
    def open_type(self):
        return self._open_type

    @open_type.setter
    def open_type(self, value):
        self._open_type = value
    @property
    def operators_code(self):
        return self._operators_code

    @operators_code.setter
    def operators_code(self, value):
        self._operators_code = value
    @property
    def org_group_code(self):
        return self._org_group_code

    @org_group_code.setter
    def org_group_code(self, value):
        self._org_group_code = value
    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, value):
        self._room_name = value
    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, value):
        self._room_no = value
    @property
    def team_name(self):
        return self._team_name

    @team_name.setter
    def team_name(self, value):
        self._team_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_org_id:
            if hasattr(self.alipay_org_id, 'to_alipay_dict'):
                params['alipay_org_id'] = self.alipay_org_id.to_alipay_dict()
            else:
                params['alipay_org_id'] = self.alipay_org_id
        if self.building_id:
            if hasattr(self.building_id, 'to_alipay_dict'):
                params['building_id'] = self.building_id.to_alipay_dict()
            else:
                params['building_id'] = self.building_id
        if self.building_name:
            if hasattr(self.building_name, 'to_alipay_dict'):
                params['building_name'] = self.building_name.to_alipay_dict()
            else:
                params['building_name'] = self.building_name
        if self.building_no:
            if hasattr(self.building_no, 'to_alipay_dict'):
                params['building_no'] = self.building_no.to_alipay_dict()
            else:
                params['building_no'] = self.building_no
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_isv_code:
            if hasattr(self.device_isv_code, 'to_alipay_dict'):
                params['device_isv_code'] = self.device_isv_code.to_alipay_dict()
            else:
                params['device_isv_code'] = self.device_isv_code
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.device_p_code:
            if hasattr(self.device_p_code, 'to_alipay_dict'):
                params['device_p_code'] = self.device_p_code.to_alipay_dict()
            else:
                params['device_p_code'] = self.device_p_code
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.effective:
            if hasattr(self.effective, 'to_alipay_dict'):
                params['effective'] = self.effective.to_alipay_dict()
            else:
                params['effective'] = self.effective
        if self.floor:
            if hasattr(self.floor, 'to_alipay_dict'):
                params['floor'] = self.floor.to_alipay_dict()
            else:
                params['floor'] = self.floor
        if self.isv_org_id:
            if hasattr(self.isv_org_id, 'to_alipay_dict'):
                params['isv_org_id'] = self.isv_org_id.to_alipay_dict()
            else:
                params['isv_org_id'] = self.isv_org_id
        if self.open_type:
            if hasattr(self.open_type, 'to_alipay_dict'):
                params['open_type'] = self.open_type.to_alipay_dict()
            else:
                params['open_type'] = self.open_type
        if self.operators_code:
            if hasattr(self.operators_code, 'to_alipay_dict'):
                params['operators_code'] = self.operators_code.to_alipay_dict()
            else:
                params['operators_code'] = self.operators_code
        if self.org_group_code:
            if hasattr(self.org_group_code, 'to_alipay_dict'):
                params['org_group_code'] = self.org_group_code.to_alipay_dict()
            else:
                params['org_group_code'] = self.org_group_code
        if self.room_name:
            if hasattr(self.room_name, 'to_alipay_dict'):
                params['room_name'] = self.room_name.to_alipay_dict()
            else:
                params['room_name'] = self.room_name
        if self.room_no:
            if hasattr(self.room_no, 'to_alipay_dict'):
                params['room_no'] = self.room_no.to_alipay_dict()
            else:
                params['room_no'] = self.room_no
        if self.team_name:
            if hasattr(self.team_name, 'to_alipay_dict'):
                params['team_name'] = self.team_name.to_alipay_dict()
            else:
                params['team_name'] = self.team_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelLockerDeviceSyncModel()
        if 'alipay_org_id' in d:
            o.alipay_org_id = d['alipay_org_id']
        if 'building_id' in d:
            o.building_id = d['building_id']
        if 'building_name' in d:
            o.building_name = d['building_name']
        if 'building_no' in d:
            o.building_no = d['building_no']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_isv_code' in d:
            o.device_isv_code = d['device_isv_code']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'device_p_code' in d:
            o.device_p_code = d['device_p_code']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'effective' in d:
            o.effective = d['effective']
        if 'floor' in d:
            o.floor = d['floor']
        if 'isv_org_id' in d:
            o.isv_org_id = d['isv_org_id']
        if 'open_type' in d:
            o.open_type = d['open_type']
        if 'operators_code' in d:
            o.operators_code = d['operators_code']
        if 'org_group_code' in d:
            o.org_group_code = d['org_group_code']
        if 'room_name' in d:
            o.room_name = d['room_name']
        if 'room_no' in d:
            o.room_no = d['room_no']
        if 'team_name' in d:
            o.team_name = d['team_name']
        return o


