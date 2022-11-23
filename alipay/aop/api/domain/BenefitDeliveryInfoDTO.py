#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitDeliveryInfoDTO(object):

    def __init__(self):
        self._available_areas = None
        self._available_shops = None
        self._deliver_scene = None
        self._deliver_type = None

    @property
    def available_areas(self):
        return self._available_areas

    @available_areas.setter
    def available_areas(self, value):
        if isinstance(value, list):
            self._available_areas = list()
            for i in value:
                self._available_areas.append(i)
    @property
    def available_shops(self):
        return self._available_shops

    @available_shops.setter
    def available_shops(self, value):
        if isinstance(value, list):
            self._available_shops = list()
            for i in value:
                self._available_shops.append(i)
    @property
    def deliver_scene(self):
        return self._deliver_scene

    @deliver_scene.setter
    def deliver_scene(self, value):
        if isinstance(value, list):
            self._deliver_scene = list()
            for i in value:
                self._deliver_scene.append(i)
    @property
    def deliver_type(self):
        return self._deliver_type

    @deliver_type.setter
    def deliver_type(self, value):
        self._deliver_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_areas:
            if isinstance(self.available_areas, list):
                for i in range(0, len(self.available_areas)):
                    element = self.available_areas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_areas[i] = element.to_alipay_dict()
            if hasattr(self.available_areas, 'to_alipay_dict'):
                params['available_areas'] = self.available_areas.to_alipay_dict()
            else:
                params['available_areas'] = self.available_areas
        if self.available_shops:
            if isinstance(self.available_shops, list):
                for i in range(0, len(self.available_shops)):
                    element = self.available_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_shops[i] = element.to_alipay_dict()
            if hasattr(self.available_shops, 'to_alipay_dict'):
                params['available_shops'] = self.available_shops.to_alipay_dict()
            else:
                params['available_shops'] = self.available_shops
        if self.deliver_scene:
            if isinstance(self.deliver_scene, list):
                for i in range(0, len(self.deliver_scene)):
                    element = self.deliver_scene[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deliver_scene[i] = element.to_alipay_dict()
            if hasattr(self.deliver_scene, 'to_alipay_dict'):
                params['deliver_scene'] = self.deliver_scene.to_alipay_dict()
            else:
                params['deliver_scene'] = self.deliver_scene
        if self.deliver_type:
            if hasattr(self.deliver_type, 'to_alipay_dict'):
                params['deliver_type'] = self.deliver_type.to_alipay_dict()
            else:
                params['deliver_type'] = self.deliver_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitDeliveryInfoDTO()
        if 'available_areas' in d:
            o.available_areas = d['available_areas']
        if 'available_shops' in d:
            o.available_shops = d['available_shops']
        if 'deliver_scene' in d:
            o.deliver_scene = d['deliver_scene']
        if 'deliver_type' in d:
            o.deliver_type = d['deliver_type']
        return o


