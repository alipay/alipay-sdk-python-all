#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PetPhoto import PetPhoto


class AlipayInsScenePetprofilePlatformprofileIdentifyModel(object):

    def __init__(self):
        self._pet_id = None
        self._photos = None

    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value
    @property
    def photos(self):
        return self._photos

    @photos.setter
    def photos(self, value):
        if isinstance(value, list):
            self._photos = list()
            for i in value:
                if isinstance(i, PetPhoto):
                    self._photos.append(i)
                else:
                    self._photos.append(PetPhoto.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.pet_id:
            if hasattr(self.pet_id, 'to_alipay_dict'):
                params['pet_id'] = self.pet_id.to_alipay_dict()
            else:
                params['pet_id'] = self.pet_id
        if self.photos:
            if isinstance(self.photos, list):
                for i in range(0, len(self.photos)):
                    element = self.photos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.photos[i] = element.to_alipay_dict()
            if hasattr(self.photos, 'to_alipay_dict'):
                params['photos'] = self.photos.to_alipay_dict()
            else:
                params['photos'] = self.photos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsScenePetprofilePlatformprofileIdentifyModel()
        if 'pet_id' in d:
            o.pet_id = d['pet_id']
        if 'photos' in d:
            o.photos = d['photos']
        return o


