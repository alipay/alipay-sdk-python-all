#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemContactVo(object):

    def __init__(self):
        self._consultation_mode = None
        self._location = None
        self._processing_time = None

    @property
    def consultation_mode(self):
        return self._consultation_mode

    @consultation_mode.setter
    def consultation_mode(self, value):
        self._consultation_mode = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def processing_time(self):
        return self._processing_time

    @processing_time.setter
    def processing_time(self, value):
        self._processing_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.consultation_mode:
            if hasattr(self.consultation_mode, 'to_alipay_dict'):
                params['consultation_mode'] = self.consultation_mode.to_alipay_dict()
            else:
                params['consultation_mode'] = self.consultation_mode
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.processing_time:
            if hasattr(self.processing_time, 'to_alipay_dict'):
                params['processing_time'] = self.processing_time.to_alipay_dict()
            else:
                params['processing_time'] = self.processing_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemContactVo()
        if 'consultation_mode' in d:
            o.consultation_mode = d['consultation_mode']
        if 'location' in d:
            o.location = d['location']
        if 'processing_time' in d:
            o.processing_time = d['processing_time']
        return o


