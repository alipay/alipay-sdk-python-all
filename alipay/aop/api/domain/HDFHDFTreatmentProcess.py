#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFHDFTreatmentProcess(object):

    def __init__(self):
        self._treatment_process_desc = None

    @property
    def treatment_process_desc(self):
        return self._treatment_process_desc

    @treatment_process_desc.setter
    def treatment_process_desc(self, value):
        self._treatment_process_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.treatment_process_desc:
            if hasattr(self.treatment_process_desc, 'to_alipay_dict'):
                params['treatment_process_desc'] = self.treatment_process_desc.to_alipay_dict()
            else:
                params['treatment_process_desc'] = self.treatment_process_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFHDFTreatmentProcess()
        if 'treatment_process_desc' in d:
            o.treatment_process_desc = d['treatment_process_desc']
        return o


