#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentOrderExtendInfoVO(object):

    def __init__(self):
        self._promised_send_time = None
        self._rent_dispatch_id = None
        self._scene_id = None
        self._union_rent_tag = None

    @property
    def promised_send_time(self):
        return self._promised_send_time

    @promised_send_time.setter
    def promised_send_time(self, value):
        self._promised_send_time = value
    @property
    def rent_dispatch_id(self):
        return self._rent_dispatch_id

    @rent_dispatch_id.setter
    def rent_dispatch_id(self, value):
        self._rent_dispatch_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def union_rent_tag(self):
        return self._union_rent_tag

    @union_rent_tag.setter
    def union_rent_tag(self, value):
        self._union_rent_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.promised_send_time:
            if hasattr(self.promised_send_time, 'to_alipay_dict'):
                params['promised_send_time'] = self.promised_send_time.to_alipay_dict()
            else:
                params['promised_send_time'] = self.promised_send_time
        if self.rent_dispatch_id:
            if hasattr(self.rent_dispatch_id, 'to_alipay_dict'):
                params['rent_dispatch_id'] = self.rent_dispatch_id.to_alipay_dict()
            else:
                params['rent_dispatch_id'] = self.rent_dispatch_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.union_rent_tag:
            if hasattr(self.union_rent_tag, 'to_alipay_dict'):
                params['union_rent_tag'] = self.union_rent_tag.to_alipay_dict()
            else:
                params['union_rent_tag'] = self.union_rent_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderExtendInfoVO()
        if 'promised_send_time' in d:
            o.promised_send_time = d['promised_send_time']
        if 'rent_dispatch_id' in d:
            o.rent_dispatch_id = d['rent_dispatch_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'union_rent_tag' in d:
            o.union_rent_tag = d['union_rent_tag']
        return o


