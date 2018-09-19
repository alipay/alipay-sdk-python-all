#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarDataserviceMaintainvehicleShareModel(object):

    def __init__(self):
        self._vid = None

    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value


    def to_alipay_dict(self):
        params = dict()
        if self.vid:
            if hasattr(self.vid, 'to_alipay_dict'):
                params['vid'] = self.vid.to_alipay_dict()
            else:
                params['vid'] = self.vid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarDataserviceMaintainvehicleShareModel()
        if 'vid' in d:
            o.vid = d['vid']
        return o


