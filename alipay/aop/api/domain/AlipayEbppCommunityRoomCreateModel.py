#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityRoomCreateModel(object):

    def __init__(self):
        self._community_short_name = None
        self._out_room_id = None
        self._owner_mobile = None
        self._owner_name = None
        self._room_desc = None
        self._room_value = None

    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def out_room_id(self):
        return self._out_room_id

    @out_room_id.setter
    def out_room_id(self, value):
        self._out_room_id = value
    @property
    def owner_mobile(self):
        return self._owner_mobile

    @owner_mobile.setter
    def owner_mobile(self, value):
        self._owner_mobile = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def room_desc(self):
        return self._room_desc

    @room_desc.setter
    def room_desc(self, value):
        self._room_desc = value
    @property
    def room_value(self):
        return self._room_value

    @room_value.setter
    def room_value(self, value):
        self._room_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.out_room_id:
            if hasattr(self.out_room_id, 'to_alipay_dict'):
                params['out_room_id'] = self.out_room_id.to_alipay_dict()
            else:
                params['out_room_id'] = self.out_room_id
        if self.owner_mobile:
            if hasattr(self.owner_mobile, 'to_alipay_dict'):
                params['owner_mobile'] = self.owner_mobile.to_alipay_dict()
            else:
                params['owner_mobile'] = self.owner_mobile
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.room_desc:
            if hasattr(self.room_desc, 'to_alipay_dict'):
                params['room_desc'] = self.room_desc.to_alipay_dict()
            else:
                params['room_desc'] = self.room_desc
        if self.room_value:
            if hasattr(self.room_value, 'to_alipay_dict'):
                params['room_value'] = self.room_value.to_alipay_dict()
            else:
                params['room_value'] = self.room_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityRoomCreateModel()
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'out_room_id' in d:
            o.out_room_id = d['out_room_id']
        if 'owner_mobile' in d:
            o.owner_mobile = d['owner_mobile']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'room_desc' in d:
            o.room_desc = d['room_desc']
        if 'room_value' in d:
            o.room_value = d['room_value']
        return o


