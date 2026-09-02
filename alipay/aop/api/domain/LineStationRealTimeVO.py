#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DirectionVO import DirectionVO


class LineStationRealTimeVO(object):

    def __init__(self):
        self._color = None
        self._directions = None
        self._icon = None
        self._name = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def directions(self):
        return self._directions

    @directions.setter
    def directions(self, value):
        if isinstance(value, list):
            self._directions = list()
            for i in value:
                if isinstance(i, DirectionVO):
                    self._directions.append(i)
                else:
                    self._directions.append(DirectionVO.from_alipay_dict(i))
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.directions:
            if isinstance(self.directions, list):
                for i in range(0, len(self.directions)):
                    element = self.directions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.directions[i] = element.to_alipay_dict()
            if hasattr(self.directions, 'to_alipay_dict'):
                params['directions'] = self.directions.to_alipay_dict()
            else:
                params['directions'] = self.directions
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LineStationRealTimeVO()
        if 'color' in d:
            o.color = d['color']
        if 'directions' in d:
            o.directions = d['directions']
        if 'icon' in d:
            o.icon = d['icon']
        if 'name' in d:
            o.name = d['name']
        return o


