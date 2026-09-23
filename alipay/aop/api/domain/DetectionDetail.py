#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DetectionDetail(object):

    def __init__(self):
        self._cheating_status = None
        self._detection_status = None
        self._gesture_type = None

    @property
    def cheating_status(self):
        return self._cheating_status

    @cheating_status.setter
    def cheating_status(self, value):
        self._cheating_status = value
    @property
    def detection_status(self):
        return self._detection_status

    @detection_status.setter
    def detection_status(self, value):
        self._detection_status = value
    @property
    def gesture_type(self):
        return self._gesture_type

    @gesture_type.setter
    def gesture_type(self, value):
        self._gesture_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cheating_status:
            if hasattr(self.cheating_status, 'to_alipay_dict'):
                params['cheating_status'] = self.cheating_status.to_alipay_dict()
            else:
                params['cheating_status'] = self.cheating_status
        if self.detection_status:
            if hasattr(self.detection_status, 'to_alipay_dict'):
                params['detection_status'] = self.detection_status.to_alipay_dict()
            else:
                params['detection_status'] = self.detection_status
        if self.gesture_type:
            if hasattr(self.gesture_type, 'to_alipay_dict'):
                params['gesture_type'] = self.gesture_type.to_alipay_dict()
            else:
                params['gesture_type'] = self.gesture_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DetectionDetail()
        if 'cheating_status' in d:
            o.cheating_status = d['cheating_status']
        if 'detection_status' in d:
            o.detection_status = d['detection_status']
        if 'gesture_type' in d:
            o.gesture_type = d['gesture_type']
        return o


