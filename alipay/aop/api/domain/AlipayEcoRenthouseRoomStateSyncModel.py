#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseRoomStateSyncModel(object):

    def __init__(self):
        self._flats_tag = None
        self._rent_status = None
        self._room_code = None
        self._room_status = None

    @property
    def flats_tag(self):
        return self._flats_tag

    @flats_tag.setter
    def flats_tag(self, value):
        self._flats_tag = value
    @property
    def rent_status(self):
        return self._rent_status

    @rent_status.setter
    def rent_status(self, value):
        self._rent_status = value
    @property
    def room_code(self):
        return self._room_code

    @room_code.setter
    def room_code(self, value):
        self._room_code = value
    @property
    def room_status(self):
        return self._room_status

    @room_status.setter
    def room_status(self, value):
        self._room_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.flats_tag:
            if hasattr(self.flats_tag, 'to_alipay_dict'):
                params['flats_tag'] = self.flats_tag.to_alipay_dict()
            else:
                params['flats_tag'] = self.flats_tag
        if self.rent_status:
            if hasattr(self.rent_status, 'to_alipay_dict'):
                params['rent_status'] = self.rent_status.to_alipay_dict()
            else:
                params['rent_status'] = self.rent_status
        if self.room_code:
            if hasattr(self.room_code, 'to_alipay_dict'):
                params['room_code'] = self.room_code.to_alipay_dict()
            else:
                params['room_code'] = self.room_code
        if self.room_status:
            if hasattr(self.room_status, 'to_alipay_dict'):
                params['room_status'] = self.room_status.to_alipay_dict()
            else:
                params['room_status'] = self.room_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseRoomStateSyncModel()
        if 'flats_tag' in d:
            o.flats_tag = d['flats_tag']
        if 'rent_status' in d:
            o.rent_status = d['rent_status']
        if 'room_code' in d:
            o.room_code = d['room_code']
        if 'room_status' in d:
            o.room_status = d['room_status']
        return o


