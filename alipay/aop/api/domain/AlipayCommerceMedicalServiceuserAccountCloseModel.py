#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServiceuserAccountCloseModel(object):

    def __init__(self):
        self._hdf_out_id = None

    @property
    def hdf_out_id(self):
        return self._hdf_out_id

    @hdf_out_id.setter
    def hdf_out_id(self, value):
        self._hdf_out_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.hdf_out_id:
            if hasattr(self.hdf_out_id, 'to_alipay_dict'):
                params['hdf_out_id'] = self.hdf_out_id.to_alipay_dict()
            else:
                params['hdf_out_id'] = self.hdf_out_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServiceuserAccountCloseModel()
        if 'hdf_out_id' in d:
            o.hdf_out_id = d['hdf_out_id']
        return o


