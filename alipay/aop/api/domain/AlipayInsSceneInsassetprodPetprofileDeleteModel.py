#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsassetprodPetprofileDeleteModel(object):

    def __init__(self):
        self._channel = None
        self._pet_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.pet_id:
            if hasattr(self.pet_id, 'to_alipay_dict'):
                params['pet_id'] = self.pet_id.to_alipay_dict()
            else:
                params['pet_id'] = self.pet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInsassetprodPetprofileDeleteModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'pet_id' in d:
            o.pet_id = d['pet_id']
        return o


