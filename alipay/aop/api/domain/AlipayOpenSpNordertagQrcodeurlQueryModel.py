#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordertagQrcodeurlQueryModel(object):

    def __init__(self):
        self._coil_no = None

    @property
    def coil_no(self):
        return self._coil_no

    @coil_no.setter
    def coil_no(self, value):
        self._coil_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.coil_no:
            if hasattr(self.coil_no, 'to_alipay_dict'):
                params['coil_no'] = self.coil_no.to_alipay_dict()
            else:
                params['coil_no'] = self.coil_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordertagQrcodeurlQueryModel()
        if 'coil_no' in d:
            o.coil_no = d['coil_no']
        return o


