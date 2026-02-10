#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoboAirConditionerInfo import RoboAirConditionerInfo
from alipay.aop.api.domain.RoboCarWindowInfo import RoboCarWindowInfo
from alipay.aop.api.domain.RoboFrontLightInfo import RoboFrontLightInfo
from alipay.aop.api.domain.RoboSeatHeatingInfo import RoboSeatHeatingInfo
from alipay.aop.api.domain.RoboWelcomeLightInfo import RoboWelcomeLightInfo
from alipay.aop.api.domain.RoboWhistleInfo import RoboWhistleInfo


class RoboCarControlInfo(object):

    def __init__(self):
        self._air_conditioner = None
        self._car_window = None
        self._front_light = None
        self._seat_heating = None
        self._welcome_light = None
        self._whistle = None

    @property
    def air_conditioner(self):
        return self._air_conditioner

    @air_conditioner.setter
    def air_conditioner(self, value):
        if isinstance(value, RoboAirConditionerInfo):
            self._air_conditioner = value
        else:
            self._air_conditioner = RoboAirConditionerInfo.from_alipay_dict(value)
    @property
    def car_window(self):
        return self._car_window

    @car_window.setter
    def car_window(self, value):
        if isinstance(value, RoboCarWindowInfo):
            self._car_window = value
        else:
            self._car_window = RoboCarWindowInfo.from_alipay_dict(value)
    @property
    def front_light(self):
        return self._front_light

    @front_light.setter
    def front_light(self, value):
        if isinstance(value, RoboFrontLightInfo):
            self._front_light = value
        else:
            self._front_light = RoboFrontLightInfo.from_alipay_dict(value)
    @property
    def seat_heating(self):
        return self._seat_heating

    @seat_heating.setter
    def seat_heating(self, value):
        if isinstance(value, RoboSeatHeatingInfo):
            self._seat_heating = value
        else:
            self._seat_heating = RoboSeatHeatingInfo.from_alipay_dict(value)
    @property
    def welcome_light(self):
        return self._welcome_light

    @welcome_light.setter
    def welcome_light(self, value):
        if isinstance(value, RoboWelcomeLightInfo):
            self._welcome_light = value
        else:
            self._welcome_light = RoboWelcomeLightInfo.from_alipay_dict(value)
    @property
    def whistle(self):
        return self._whistle

    @whistle.setter
    def whistle(self, value):
        if isinstance(value, RoboWhistleInfo):
            self._whistle = value
        else:
            self._whistle = RoboWhistleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.air_conditioner:
            if hasattr(self.air_conditioner, 'to_alipay_dict'):
                params['air_conditioner'] = self.air_conditioner.to_alipay_dict()
            else:
                params['air_conditioner'] = self.air_conditioner
        if self.car_window:
            if hasattr(self.car_window, 'to_alipay_dict'):
                params['car_window'] = self.car_window.to_alipay_dict()
            else:
                params['car_window'] = self.car_window
        if self.front_light:
            if hasattr(self.front_light, 'to_alipay_dict'):
                params['front_light'] = self.front_light.to_alipay_dict()
            else:
                params['front_light'] = self.front_light
        if self.seat_heating:
            if hasattr(self.seat_heating, 'to_alipay_dict'):
                params['seat_heating'] = self.seat_heating.to_alipay_dict()
            else:
                params['seat_heating'] = self.seat_heating
        if self.welcome_light:
            if hasattr(self.welcome_light, 'to_alipay_dict'):
                params['welcome_light'] = self.welcome_light.to_alipay_dict()
            else:
                params['welcome_light'] = self.welcome_light
        if self.whistle:
            if hasattr(self.whistle, 'to_alipay_dict'):
                params['whistle'] = self.whistle.to_alipay_dict()
            else:
                params['whistle'] = self.whistle
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboCarControlInfo()
        if 'air_conditioner' in d:
            o.air_conditioner = d['air_conditioner']
        if 'car_window' in d:
            o.car_window = d['car_window']
        if 'front_light' in d:
            o.front_light = d['front_light']
        if 'seat_heating' in d:
            o.seat_heating = d['seat_heating']
        if 'welcome_light' in d:
            o.welcome_light = d['welcome_light']
        if 'whistle' in d:
            o.whistle = d['whistle']
        return o


