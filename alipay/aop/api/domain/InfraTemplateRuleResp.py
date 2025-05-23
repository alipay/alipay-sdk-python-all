#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InfraTemplateRuleResp(object):

    def __init__(self):
        self._check_rule = None
        self._desc = None
        self._height = None
        self._max_size = None
        self._min_bitrate = None
        self._min_play_time = None
        self._min_size = None
        self._width = None

    @property
    def check_rule(self):
        return self._check_rule

    @check_rule.setter
    def check_rule(self, value):
        self._check_rule = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        self._max_size = value
    @property
    def min_bitrate(self):
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, value):
        self._min_bitrate = value
    @property
    def min_play_time(self):
        return self._min_play_time

    @min_play_time.setter
    def min_play_time(self, value):
        self._min_play_time = value
    @property
    def min_size(self):
        return self._min_size

    @min_size.setter
    def min_size(self, value):
        self._min_size = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_rule:
            if hasattr(self.check_rule, 'to_alipay_dict'):
                params['check_rule'] = self.check_rule.to_alipay_dict()
            else:
                params['check_rule'] = self.check_rule
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.max_size:
            if hasattr(self.max_size, 'to_alipay_dict'):
                params['max_size'] = self.max_size.to_alipay_dict()
            else:
                params['max_size'] = self.max_size
        if self.min_bitrate:
            if hasattr(self.min_bitrate, 'to_alipay_dict'):
                params['min_bitrate'] = self.min_bitrate.to_alipay_dict()
            else:
                params['min_bitrate'] = self.min_bitrate
        if self.min_play_time:
            if hasattr(self.min_play_time, 'to_alipay_dict'):
                params['min_play_time'] = self.min_play_time.to_alipay_dict()
            else:
                params['min_play_time'] = self.min_play_time
        if self.min_size:
            if hasattr(self.min_size, 'to_alipay_dict'):
                params['min_size'] = self.min_size.to_alipay_dict()
            else:
                params['min_size'] = self.min_size
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InfraTemplateRuleResp()
        if 'check_rule' in d:
            o.check_rule = d['check_rule']
        if 'desc' in d:
            o.desc = d['desc']
        if 'height' in d:
            o.height = d['height']
        if 'max_size' in d:
            o.max_size = d['max_size']
        if 'min_bitrate' in d:
            o.min_bitrate = d['min_bitrate']
        if 'min_play_time' in d:
            o.min_play_time = d['min_play_time']
        if 'min_size' in d:
            o.min_size = d['min_size']
        if 'width' in d:
            o.width = d['width']
        return o


