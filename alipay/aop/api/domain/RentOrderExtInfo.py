#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentOrderExtInfo(object):

    def __init__(self):
        self._rent_mode = None

    @property
    def rent_mode(self):
        return self._rent_mode

    @rent_mode.setter
    def rent_mode(self, value):
        self._rent_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.rent_mode:
            if hasattr(self.rent_mode, 'to_alipay_dict'):
                params['rent_mode'] = self.rent_mode.to_alipay_dict()
            else:
                params['rent_mode'] = self.rent_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderExtInfo()
        if 'rent_mode' in d:
            o.rent_mode = d['rent_mode']
        return o


