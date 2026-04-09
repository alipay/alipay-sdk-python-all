#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPromotionlinkGetModel(object):

    def __init__(self):
        self._doctor_id = None
        self._promotion_u_id = None

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def promotion_u_id(self):
        return self._promotion_u_id

    @promotion_u_id.setter
    def promotion_u_id(self, value):
        self._promotion_u_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.promotion_u_id:
            if hasattr(self.promotion_u_id, 'to_alipay_dict'):
                params['promotion_u_id'] = self.promotion_u_id.to_alipay_dict()
            else:
                params['promotion_u_id'] = self.promotion_u_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPromotionlinkGetModel()
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'promotion_u_id' in d:
            o.promotion_u_id = d['promotion_u_id']
        return o


