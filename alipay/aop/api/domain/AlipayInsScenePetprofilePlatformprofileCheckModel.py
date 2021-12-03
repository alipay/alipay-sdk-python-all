#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsScenePetprofilePlatformprofileCheckModel(object):

    def __init__(self):
        self._file_id = None
        self._pet_photo_type = None
        self._pet_type = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def pet_photo_type(self):
        return self._pet_photo_type

    @pet_photo_type.setter
    def pet_photo_type(self, value):
        self._pet_photo_type = value
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        self._pet_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.pet_photo_type:
            if hasattr(self.pet_photo_type, 'to_alipay_dict'):
                params['pet_photo_type'] = self.pet_photo_type.to_alipay_dict()
            else:
                params['pet_photo_type'] = self.pet_photo_type
        if self.pet_type:
            if hasattr(self.pet_type, 'to_alipay_dict'):
                params['pet_type'] = self.pet_type.to_alipay_dict()
            else:
                params['pet_type'] = self.pet_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsScenePetprofilePlatformprofileCheckModel()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'pet_photo_type' in d:
            o.pet_photo_type = d['pet_photo_type']
        if 'pet_type' in d:
            o.pet_type = d['pet_type']
        return o


