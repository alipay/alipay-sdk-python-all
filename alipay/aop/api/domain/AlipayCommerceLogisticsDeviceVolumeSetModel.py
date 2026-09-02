#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsDeviceVolumeSetModel(object):

    def __init__(self):
        self._sn_id = None
        self._volume = None

    @property
    def sn_id(self):
        return self._sn_id

    @sn_id.setter
    def sn_id(self, value):
        self._sn_id = value
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value


    def to_alipay_dict(self):
        params = dict()
        if self.sn_id:
            if hasattr(self.sn_id, 'to_alipay_dict'):
                params['sn_id'] = self.sn_id.to_alipay_dict()
            else:
                params['sn_id'] = self.sn_id
        if self.volume:
            if hasattr(self.volume, 'to_alipay_dict'):
                params['volume'] = self.volume.to_alipay_dict()
            else:
                params['volume'] = self.volume
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsDeviceVolumeSetModel()
        if 'sn_id' in d:
            o.sn_id = d['sn_id']
        if 'volume' in d:
            o.volume = d['volume']
        return o


