#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmSwTreeGetModel(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._id = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmSwTreeGetModel()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'id' in d:
            o.id = d['id']
        return o


