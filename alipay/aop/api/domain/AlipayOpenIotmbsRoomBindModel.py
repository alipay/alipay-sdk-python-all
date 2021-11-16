#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsRoomBindModel(object):

    def __init__(self):
        self._dev_id = None
        self._device_type = None
        self._hotel_id = None
        self._hotel_name = None
        self._project_id = None
        self._room_no = None
        self._sn = None

    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def hotel_id(self):
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, value):
        self._hotel_id = value
    @property
    def hotel_name(self):
        return self._hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self._hotel_name = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, value):
        self._room_no = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.hotel_id:
            if hasattr(self.hotel_id, 'to_alipay_dict'):
                params['hotel_id'] = self.hotel_id.to_alipay_dict()
            else:
                params['hotel_id'] = self.hotel_id
        if self.hotel_name:
            if hasattr(self.hotel_name, 'to_alipay_dict'):
                params['hotel_name'] = self.hotel_name.to_alipay_dict()
            else:
                params['hotel_name'] = self.hotel_name
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.room_no:
            if hasattr(self.room_no, 'to_alipay_dict'):
                params['room_no'] = self.room_no.to_alipay_dict()
            else:
                params['room_no'] = self.room_no
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsRoomBindModel()
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'hotel_id' in d:
            o.hotel_id = d['hotel_id']
        if 'hotel_name' in d:
            o.hotel_name = d['hotel_name']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'room_no' in d:
            o.room_no = d['room_no']
        if 'sn' in d:
            o.sn = d['sn']
        return o


