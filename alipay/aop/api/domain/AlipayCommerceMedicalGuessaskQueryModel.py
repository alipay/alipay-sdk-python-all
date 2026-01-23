#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalGuessaskQueryModel(object):

    def __init__(self):
        self._hdf_user_id = None
        self._total = None

    @property
    def hdf_user_id(self):
        return self._hdf_user_id

    @hdf_user_id.setter
    def hdf_user_id(self, value):
        self._hdf_user_id = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.hdf_user_id:
            if hasattr(self.hdf_user_id, 'to_alipay_dict'):
                params['hdf_user_id'] = self.hdf_user_id.to_alipay_dict()
            else:
                params['hdf_user_id'] = self.hdf_user_id
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalGuessaskQueryModel()
        if 'hdf_user_id' in d:
            o.hdf_user_id = d['hdf_user_id']
        if 'total' in d:
            o.total = d['total']
        return o


