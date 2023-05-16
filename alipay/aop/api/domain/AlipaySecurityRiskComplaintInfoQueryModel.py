#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskComplaintInfoQueryModel(object):

    def __init__(self):
        self._complain_id = None

    @property
    def complain_id(self):
        return self._complain_id

    @complain_id.setter
    def complain_id(self, value):
        self._complain_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.complain_id:
            if hasattr(self.complain_id, 'to_alipay_dict'):
                params['complain_id'] = self.complain_id.to_alipay_dict()
            else:
                params['complain_id'] = self.complain_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskComplaintInfoQueryModel()
        if 'complain_id' in d:
            o.complain_id = d['complain_id']
        return o


