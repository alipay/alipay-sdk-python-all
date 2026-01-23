#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VerifyConfigCommonPageConfig(object):

    def __init__(self):
        self._back_ground_image = None
        self._float_diaphaneity = None

    @property
    def back_ground_image(self):
        return self._back_ground_image

    @back_ground_image.setter
    def back_ground_image(self, value):
        self._back_ground_image = value
    @property
    def float_diaphaneity(self):
        return self._float_diaphaneity

    @float_diaphaneity.setter
    def float_diaphaneity(self, value):
        self._float_diaphaneity = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_ground_image:
            if hasattr(self.back_ground_image, 'to_alipay_dict'):
                params['back_ground_image'] = self.back_ground_image.to_alipay_dict()
            else:
                params['back_ground_image'] = self.back_ground_image
        if self.float_diaphaneity:
            if hasattr(self.float_diaphaneity, 'to_alipay_dict'):
                params['float_diaphaneity'] = self.float_diaphaneity.to_alipay_dict()
            else:
                params['float_diaphaneity'] = self.float_diaphaneity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VerifyConfigCommonPageConfig()
        if 'back_ground_image' in d:
            o.back_ground_image = d['back_ground_image']
        if 'float_diaphaneity' in d:
            o.float_diaphaneity = d['float_diaphaneity']
        return o


