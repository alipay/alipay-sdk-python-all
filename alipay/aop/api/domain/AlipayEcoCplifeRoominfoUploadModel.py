#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CplifeRoomInfo import CplifeRoomInfo


class AlipayEcoCplifeRoominfoUploadModel(object):

    def __init__(self):
        self._batch_id = None
        self._community_id = None
        self._room_info_set = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def room_info_set(self):
        return self._room_info_set

    @room_info_set.setter
    def room_info_set(self, value):
        if isinstance(value, list):
            self._room_info_set = list()
            for i in value:
                if isinstance(i, CplifeRoomInfo):
                    self._room_info_set.append(i)
                else:
                    self._room_info_set.append(CplifeRoomInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.room_info_set:
            if isinstance(self.room_info_set, list):
                for i in range(0, len(self.room_info_set)):
                    element = self.room_info_set[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.room_info_set[i] = element.to_alipay_dict()
            if hasattr(self.room_info_set, 'to_alipay_dict'):
                params['room_info_set'] = self.room_info_set.to_alipay_dict()
            else:
                params['room_info_set'] = self.room_info_set
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeRoominfoUploadModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'room_info_set' in d:
            o.room_info_set = d['room_info_set']
        return o


