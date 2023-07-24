#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoDetailInfoDTO(object):

    def __init__(self):
        self._activity_consult_id = None

    @property
    def activity_consult_id(self):
        return self._activity_consult_id

    @activity_consult_id.setter
    def activity_consult_id(self, value):
        self._activity_consult_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_consult_id:
            if hasattr(self.activity_consult_id, 'to_alipay_dict'):
                params['activity_consult_id'] = self.activity_consult_id.to_alipay_dict()
            else:
                params['activity_consult_id'] = self.activity_consult_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoDetailInfoDTO()
        if 'activity_consult_id' in d:
            o.activity_consult_id = d['activity_consult_id']
        return o


