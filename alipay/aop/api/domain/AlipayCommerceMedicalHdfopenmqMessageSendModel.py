#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfopenmqMessageSendModel(object):

    def __init__(self):
        self._hdfbody = None

    @property
    def hdfbody(self):
        return self._hdfbody

    @hdfbody.setter
    def hdfbody(self, value):
        self._hdfbody = value


    def to_alipay_dict(self):
        params = dict()
        if self.hdfbody:
            if hasattr(self.hdfbody, 'to_alipay_dict'):
                params['hdfbody'] = self.hdfbody.to_alipay_dict()
            else:
                params['hdfbody'] = self.hdfbody
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfopenmqMessageSendModel()
        if 'hdfbody' in d:
            o.hdfbody = d['hdfbody']
        return o


