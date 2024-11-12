#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserSegmentationInfo(object):

    def __init__(self):
        self._segmentation_code = None
        self._sub_segmentation_code = None

    @property
    def segmentation_code(self):
        return self._segmentation_code

    @segmentation_code.setter
    def segmentation_code(self, value):
        self._segmentation_code = value
    @property
    def sub_segmentation_code(self):
        return self._sub_segmentation_code

    @sub_segmentation_code.setter
    def sub_segmentation_code(self, value):
        self._sub_segmentation_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.segmentation_code:
            if hasattr(self.segmentation_code, 'to_alipay_dict'):
                params['segmentation_code'] = self.segmentation_code.to_alipay_dict()
            else:
                params['segmentation_code'] = self.segmentation_code
        if self.sub_segmentation_code:
            if hasattr(self.sub_segmentation_code, 'to_alipay_dict'):
                params['sub_segmentation_code'] = self.sub_segmentation_code.to_alipay_dict()
            else:
                params['sub_segmentation_code'] = self.sub_segmentation_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserSegmentationInfo()
        if 'segmentation_code' in d:
            o.segmentation_code = d['segmentation_code']
        if 'sub_segmentation_code' in d:
            o.sub_segmentation_code = d['sub_segmentation_code']
        return o


