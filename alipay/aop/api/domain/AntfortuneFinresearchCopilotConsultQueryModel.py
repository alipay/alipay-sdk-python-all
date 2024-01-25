#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchCopilotConsultQueryModel(object):

    def __init__(self):
        self._consult_id = None

    @property
    def consult_id(self):
        return self._consult_id

    @consult_id.setter
    def consult_id(self, value):
        self._consult_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_id:
            if hasattr(self.consult_id, 'to_alipay_dict'):
                params['consult_id'] = self.consult_id.to_alipay_dict()
            else:
                params['consult_id'] = self.consult_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchCopilotConsultQueryModel()
        if 'consult_id' in d:
            o.consult_id = d['consult_id']
        return o


