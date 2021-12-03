#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PetPhoto import PetPhoto


class AlipayInsScenePetprofilePlatformprofileCreateModel(object):

    def __init__(self):
        self._birthday = None
        self._gender = None
        self._nick = None
        self._out_biz_no = None
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayInsScenePetprofilePlatformprofileCreateModel()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'gender' in d:
            o.gender = d['gender']
        if 'nick' in d:
            o.nick = d['nick']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'photos' in d:
            o.photos = d['photos']
        if 'sterilization' in d:
            o.sterilization = d['sterilization']
        if 'type' in d:
            o.type = d['type']
        return o


