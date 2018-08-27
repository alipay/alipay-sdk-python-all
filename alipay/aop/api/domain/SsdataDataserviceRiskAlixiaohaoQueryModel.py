#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskAlixiaohaoQueryModel(object):

    def __init__(self):
        self._mobile_no = None

    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskAlixiaohaoQueryModel()
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        return o


