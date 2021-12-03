#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PetPhoto import PetPhoto


class AlipayInsScenePetprofilePlatformprofileMatchModel(object):

    def __init__(self):
        self._pet_type = None
        self._photos = None

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        self._pet_type = value
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
        if self.pet_type:
            if hasattr(self.pet_type, 'to_alipay_dict'):
                params['pet_type'] = self.pet_type.to_alipay_dict()
            else:
                params['pet_type'] = self.pet_type
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
        o = AlipayInsScenePetprofilePlatformprofileMatchModel()
        if 'pet_type' in d:
            o.pet_type = d['pet_type']
        if 'photos' in d:
            o.photos = d['photos']
        return o


