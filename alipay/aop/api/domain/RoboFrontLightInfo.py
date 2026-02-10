#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboFrontLightInfo(object):

    def __init__(self):
        self._current_type = None
        self._gif_in = None
        self._gif_out = None
        self._light_ability = None
        self._light_version = None
        self._remain_modify_num = None

    @property
    def current_type(self):
        return self._current_type

    @current_type.setter
    def current_type(self, value):
        self._current_type = value
    @property
    def gif_in(self):
        return self._gif_in

    @gif_in.setter
    def gif_in(self, value):
        self._gif_in = value
    @property
    def gif_out(self):
        return self._gif_out

    @gif_out.setter
    def gif_out(self, value):
        self._gif_out = value
    @property
    def light_ability(self):
        return self._light_ability

    @light_ability.setter
    def light_ability(self, value):
        self._light_ability = value
    @property
    def light_version(self):
        return self._light_version

    @light_version.setter
    def light_version(self, value):
        self._light_version = value
    @property
    def remain_modify_num(self):
        return self._remain_modify_num

    @remain_modify_num.setter
    def remain_modify_num(self, value):
        self._remain_modify_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_type:
            if hasattr(self.current_type, 'to_alipay_dict'):
                params['current_type'] = self.current_type.to_alipay_dict()
            else:
                params['current_type'] = self.current_type
        if self.gif_in:
            if hasattr(self.gif_in, 'to_alipay_dict'):
                params['gif_in'] = self.gif_in.to_alipay_dict()
            else:
                params['gif_in'] = self.gif_in
        if self.gif_out:
            if hasattr(self.gif_out, 'to_alipay_dict'):
                params['gif_out'] = self.gif_out.to_alipay_dict()
            else:
                params['gif_out'] = self.gif_out
        if self.light_ability:
            if hasattr(self.light_ability, 'to_alipay_dict'):
                params['light_ability'] = self.light_ability.to_alipay_dict()
            else:
                params['light_ability'] = self.light_ability
        if self.light_version:
            if hasattr(self.light_version, 'to_alipay_dict'):
                params['light_version'] = self.light_version.to_alipay_dict()
            else:
                params['light_version'] = self.light_version
        if self.remain_modify_num:
            if hasattr(self.remain_modify_num, 'to_alipay_dict'):
                params['remain_modify_num'] = self.remain_modify_num.to_alipay_dict()
            else:
                params['remain_modify_num'] = self.remain_modify_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboFrontLightInfo()
        if 'current_type' in d:
            o.current_type = d['current_type']
        if 'gif_in' in d:
            o.gif_in = d['gif_in']
        if 'gif_out' in d:
            o.gif_out = d['gif_out']
        if 'light_ability' in d:
            o.light_ability = d['light_ability']
        if 'light_version' in d:
            o.light_version = d['light_version']
        if 'remain_modify_num' in d:
            o.remain_modify_num = d['remain_modify_num']
        return o


