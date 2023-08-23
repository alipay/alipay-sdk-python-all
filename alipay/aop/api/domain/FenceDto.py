#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GpsInfo import GpsInfo


class FenceDto(object):

    def __init__(self):
        self._coordinates = None
        self._properties = None

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        if isinstance(value, list):
            self._coordinates = list()
            for i in value:
                if isinstance(i, GpsInfo):
                    self._coordinates.append(i)
                else:
                    self._coordinates.append(GpsInfo.from_alipay_dict(i))
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = value


    def to_alipay_dict(self):
        params = dict()
        if self.coordinates:
            if isinstance(self.coordinates, list):
                for i in range(0, len(self.coordinates)):
                    element = self.coordinates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coordinates[i] = element.to_alipay_dict()
            if hasattr(self.coordinates, 'to_alipay_dict'):
                params['coordinates'] = self.coordinates.to_alipay_dict()
            else:
                params['coordinates'] = self.coordinates
        if self.properties:
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FenceDto()
        if 'coordinates' in d:
            o.coordinates = d['coordinates']
        if 'properties' in d:
            o.properties = d['properties']
        return o


