#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmLcsServicemodelSetModel(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._service_mode = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def service_mode(self):
        return self._service_mode

    @service_mode.setter
    def service_mode(self, value):
        self._service_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.service_mode:
            if hasattr(self.service_mode, 'to_alipay_dict'):
                params['service_mode'] = self.service_mode.to_alipay_dict()
            else:
                params['service_mode'] = self.service_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmLcsServicemodelSetModel()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'service_mode' in d:
            o.service_mode = d['service_mode']
        return o


