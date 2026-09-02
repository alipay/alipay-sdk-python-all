#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsPetOrgprofileverifyConsultModel(object):

    def __init__(self):
        self._check_record_no = None

    @property
    def check_record_no(self):
        return self._check_record_no

    @check_record_no.setter
    def check_record_no(self, value):
        self._check_record_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_record_no:
            if hasattr(self.check_record_no, 'to_alipay_dict'):
                params['check_record_no'] = self.check_record_no.to_alipay_dict()
            else:
                params['check_record_no'] = self.check_record_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsPetOrgprofileverifyConsultModel()
        if 'check_record_no' in d:
            o.check_record_no = d['check_record_no']
        return o


