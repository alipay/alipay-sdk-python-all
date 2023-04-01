#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemDeliveryInfoSyncRequest(object):

    def __init__(self):
        self._camp_type = None
        self._position_id = None

    @property
    def camp_type(self):
        return self._camp_type

    @camp_type.setter
    def camp_type(self, value):
        self._camp_type = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_type:
            if hasattr(self.camp_type, 'to_alipay_dict'):
                params['camp_type'] = self.camp_type.to_alipay_dict()
            else:
                params['camp_type'] = self.camp_type
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDeliveryInfoSyncRequest()
        if 'camp_type' in d:
            o.camp_type = d['camp_type']
        if 'position_id' in d:
            o.position_id = d['position_id']
        return o


