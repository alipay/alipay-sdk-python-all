#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PetPhoto import PetPhoto


class PlatformPetProfile(object):

    def __init__(self):
        self._birthday = None
        self._gender = None
        self._nick = None
        self._pet_id = None
        self._photos = None
        self._sterilization = None
        self._type = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
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
    @property
    def sterilization(self):
        return self._sterilization

    @sterilization.setter
    def sterilization(self, value):
        self._sterilization = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = self.nick.to_alipay_dict()
            else:
                params['nick'] = self.nick
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
        if self.sterilization:
            if hasattr(self.sterilization, 'to_alipay_dict'):
                params['sterilization'] = self.sterilization.to_alipay_dict()
            else:
                params['sterilization'] = self.sterilization
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlatformPetProfile()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'gender' in d:
            o.gender = d['gender']
        if 'nick' in d:
            o.nick = d['nick']
        if 'pet_id' in d:
            o.pet_id = d['pet_id']
        if 'photos' in d:
            o.photos = d['photos']
        if 'sterilization' in d:
            o.sterilization = d['sterilization']
        if 'type' in d:
            o.type = d['type']
        return o


