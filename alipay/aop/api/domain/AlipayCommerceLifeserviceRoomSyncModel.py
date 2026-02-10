#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LifeServiceAttr import LifeServiceAttr


class AlipayCommerceLifeserviceRoomSyncModel(object):

    def __init__(self):
        self._out_room_id = None
        self._room_attrs = None
        self._room_category = None
        self._room_id = None
        self._room_name = None
        self._room_pics = None
        self._shop_id = None
        self._status = None

    @property
    def out_room_id(self):
        return self._out_room_id

    @out_room_id.setter
    def out_room_id(self, value):
        self._out_room_id = value
    @property
    def room_attrs(self):
        return self._room_attrs

    @room_attrs.setter
    def room_attrs(self, value):
        if isinstance(value, list):
            self._room_attrs = list()
            for i in value:
                if isinstance(i, LifeServiceAttr):
                    self._room_attrs.append(i)
                else:
                    self._room_attrs.append(LifeServiceAttr.from_alipay_dict(i))
    @property
    def room_category(self):
        return self._room_category

    @room_category.setter
    def room_category(self, value):
        self._room_category = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, value):
        self._room_name = value
    @property
    def room_pics(self):
        return self._room_pics

    @room_pics.setter
    def room_pics(self, value):
        if isinstance(value, list):
            self._room_pics = list()
            for i in value:
                self._room_pics.append(i)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_room_id:
            if hasattr(self.out_room_id, 'to_alipay_dict'):
                params['out_room_id'] = self.out_room_id.to_alipay_dict()
            else:
                params['out_room_id'] = self.out_room_id
        if self.room_attrs:
            if isinstance(self.room_attrs, list):
                for i in range(0, len(self.room_attrs)):
                    element = self.room_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.room_attrs[i] = element.to_alipay_dict()
            if hasattr(self.room_attrs, 'to_alipay_dict'):
                params['room_attrs'] = self.room_attrs.to_alipay_dict()
            else:
                params['room_attrs'] = self.room_attrs
        if self.room_category:
            if hasattr(self.room_category, 'to_alipay_dict'):
                params['room_category'] = self.room_category.to_alipay_dict()
            else:
                params['room_category'] = self.room_category
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        if self.room_name:
            if hasattr(self.room_name, 'to_alipay_dict'):
                params['room_name'] = self.room_name.to_alipay_dict()
            else:
                params['room_name'] = self.room_name
        if self.room_pics:
            if isinstance(self.room_pics, list):
                for i in range(0, len(self.room_pics)):
                    element = self.room_pics[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.room_pics[i] = element.to_alipay_dict()
            if hasattr(self.room_pics, 'to_alipay_dict'):
                params['room_pics'] = self.room_pics.to_alipay_dict()
            else:
                params['room_pics'] = self.room_pics
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceRoomSyncModel()
        if 'out_room_id' in d:
            o.out_room_id = d['out_room_id']
        if 'room_attrs' in d:
            o.room_attrs = d['room_attrs']
        if 'room_category' in d:
            o.room_category = d['room_category']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'room_name' in d:
            o.room_name = d['room_name']
        if 'room_pics' in d:
            o.room_pics = d['room_pics']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        return o


