#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePropertyVideocallRoomCreateModel(object):

    def __init__(self):
        self._device_id = None
        self._out_community_id = None
        self._owner_id = None
        self._type_list = None
        self._visitor_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def type_list(self):
        return self._type_list

    @type_list.setter
    def type_list(self, value):
        if isinstance(value, list):
            self._type_list = list()
            for i in value:
                self._type_list.append(i)
    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.out_community_id:
            if hasattr(self.out_community_id, 'to_alipay_dict'):
                params['out_community_id'] = self.out_community_id.to_alipay_dict()
            else:
                params['out_community_id'] = self.out_community_id
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.type_list:
            if isinstance(self.type_list, list):
                for i in range(0, len(self.type_list)):
                    element = self.type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.type_list[i] = element.to_alipay_dict()
            if hasattr(self.type_list, 'to_alipay_dict'):
                params['type_list'] = self.type_list.to_alipay_dict()
            else:
                params['type_list'] = self.type_list
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePropertyVideocallRoomCreateModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'type_list' in d:
            o.type_list = d['type_list']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        return o


