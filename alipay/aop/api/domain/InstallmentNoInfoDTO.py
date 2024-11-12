#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstallmentNoInfoDTO(object):

    def __init__(self):
        self._installment_no = None
        self._stage_no = None

    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def stage_no(self):
        return self._stage_no

    @stage_no.setter
    def stage_no(self, value):
        self._stage_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.stage_no:
            if hasattr(self.stage_no, 'to_alipay_dict'):
                params['stage_no'] = self.stage_no.to_alipay_dict()
            else:
                params['stage_no'] = self.stage_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentNoInfoDTO()
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'stage_no' in d:
            o.stage_no = d['stage_no']
        return o


