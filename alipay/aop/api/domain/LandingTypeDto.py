#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LandingActDto import LandingActDto


class LandingTypeDto(object):

    def __init__(self):
        self._landing_act = None
        self._landing_id = None
        self._landing_name = None
        self._landing_type = None
        self._landing_url = None

    @property
    def landing_act(self):
        return self._landing_act

    @landing_act.setter
    def landing_act(self, value):
        if isinstance(value, list):
            self._landing_act = list()
            for i in value:
                if isinstance(i, LandingActDto):
                    self._landing_act.append(i)
                else:
                    self._landing_act.append(LandingActDto.from_alipay_dict(i))
    @property
    def landing_id(self):
        return self._landing_id

    @landing_id.setter
    def landing_id(self, value):
        self._landing_id = value
    @property
    def landing_name(self):
        return self._landing_name

    @landing_name.setter
    def landing_name(self, value):
        self._landing_name = value
    @property
    def landing_type(self):
        return self._landing_type

    @landing_type.setter
    def landing_type(self, value):
        self._landing_type = value
    @property
    def landing_url(self):
        return self._landing_url

    @landing_url.setter
    def landing_url(self, value):
        self._landing_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.landing_act:
            if isinstance(self.landing_act, list):
                for i in range(0, len(self.landing_act)):
                    element = self.landing_act[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.landing_act[i] = element.to_alipay_dict()
            if hasattr(self.landing_act, 'to_alipay_dict'):
                params['landing_act'] = self.landing_act.to_alipay_dict()
            else:
                params['landing_act'] = self.landing_act
        if self.landing_id:
            if hasattr(self.landing_id, 'to_alipay_dict'):
                params['landing_id'] = self.landing_id.to_alipay_dict()
            else:
                params['landing_id'] = self.landing_id
        if self.landing_name:
            if hasattr(self.landing_name, 'to_alipay_dict'):
                params['landing_name'] = self.landing_name.to_alipay_dict()
            else:
                params['landing_name'] = self.landing_name
        if self.landing_type:
            if hasattr(self.landing_type, 'to_alipay_dict'):
                params['landing_type'] = self.landing_type.to_alipay_dict()
            else:
                params['landing_type'] = self.landing_type
        if self.landing_url:
            if hasattr(self.landing_url, 'to_alipay_dict'):
                params['landing_url'] = self.landing_url.to_alipay_dict()
            else:
                params['landing_url'] = self.landing_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LandingTypeDto()
        if 'landing_act' in d:
            o.landing_act = d['landing_act']
        if 'landing_id' in d:
            o.landing_id = d['landing_id']
        if 'landing_name' in d:
            o.landing_name = d['landing_name']
        if 'landing_type' in d:
            o.landing_type = d['landing_type']
        if 'landing_url' in d:
            o.landing_url = d['landing_url']
        return o


