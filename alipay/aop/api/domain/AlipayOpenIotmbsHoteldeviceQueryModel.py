#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsHoteldeviceQueryModel(object):

    def __init__(self):
        self._biztid = None

    @property
    def biztid(self):
        return self._biztid

    @biztid.setter
    def biztid(self, value):
        self._biztid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biztid:
            if hasattr(self.biztid, 'to_alipay_dict'):
                params['biztid'] = self.biztid.to_alipay_dict()
            else:
                params['biztid'] = self.biztid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsHoteldeviceQueryModel()
        if 'biztid' in d:
            o.biztid = d['biztid']
        return o


