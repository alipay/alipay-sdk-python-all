#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCplifeRoominfoDeleteModel(object):

    def __init__(self):
        self._batch_id = None
        self._community_id = None
        self._out_room_id_set = None

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
    def out_room_id_set(self):
        return self._out_room_id_set

    @out_room_id_set.setter
    def out_room_id_set(self, value):
        if isinstance(value, list):
            self._out_room_id_set = list()
            for i in value:
                self._out_room_id_set.append(i)


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
        if self.out_room_id_set:
            if isinstance(self.out_room_id_set, list):
                for i in range(0, len(self.out_room_id_set)):
                    element = self.out_room_id_set[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_room_id_set[i] = element.to_alipay_dict()
            if hasattr(self.out_room_id_set, 'to_alipay_dict'):
                params['out_room_id_set'] = self.out_room_id_set.to_alipay_dict()
            else:
                params['out_room_id_set'] = self.out_room_id_set
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeRoominfoDeleteModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'out_room_id_set' in d:
            o.out_room_id_set = d['out_room_id_set']
        return o


