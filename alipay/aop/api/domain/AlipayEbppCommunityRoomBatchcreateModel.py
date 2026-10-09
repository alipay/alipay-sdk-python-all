#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoomBatchCreateItem import RoomBatchCreateItem


class AlipayEbppCommunityRoomBatchcreateModel(object):

    def __init__(self):
        self._community_short_name = None
        self._parent_value = None
        self._rooms = None

    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def parent_value(self):
        return self._parent_value

    @parent_value.setter
    def parent_value(self, value):
        self._parent_value = value
    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        if isinstance(value, list):
            self._rooms = list()
            for i in value:
                if isinstance(i, RoomBatchCreateItem):
                    self._rooms.append(i)
                else:
                    self._rooms.append(RoomBatchCreateItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.parent_value:
            if hasattr(self.parent_value, 'to_alipay_dict'):
                params['parent_value'] = self.parent_value.to_alipay_dict()
            else:
                params['parent_value'] = self.parent_value
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityRoomBatchcreateModel()
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'parent_value' in d:
            o.parent_value = d['parent_value']
        if 'rooms' in d:
            o.rooms = d['rooms']
        return o


