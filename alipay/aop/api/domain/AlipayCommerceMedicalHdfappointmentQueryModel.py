#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfappointmentQueryModel(object):

    def __init__(self):
        self._msgcontent = None
        self._type = None

    @property
    def msgcontent(self):
        return self._msgcontent

    @msgcontent.setter
    def msgcontent(self, value):
        self._msgcontent = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.msgcontent:
            if hasattr(self.msgcontent, 'to_alipay_dict'):
                params['msgcontent'] = self.msgcontent.to_alipay_dict()
            else:
                params['msgcontent'] = self.msgcontent
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfappointmentQueryModel()
        if 'msgcontent' in d:
            o.msgcontent = d['msgcontent']
        if 'type' in d:
            o.type = d['type']
        return o


