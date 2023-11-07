#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FxiaokeCreateLeadsParams import FxiaokeCreateLeadsParams


class AnttechOceanbaseObglobalFxiaokeleadsCreateModel(object):

    def __init__(self):
        self._fxiaoke_create_leads_request = None

    @property
    def fxiaoke_create_leads_request(self):
        return self._fxiaoke_create_leads_request

    @fxiaoke_create_leads_request.setter
    def fxiaoke_create_leads_request(self, value):
        if isinstance(value, FxiaokeCreateLeadsParams):
            self._fxiaoke_create_leads_request = value
        else:
            self._fxiaoke_create_leads_request = FxiaokeCreateLeadsParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fxiaoke_create_leads_request:
            if hasattr(self.fxiaoke_create_leads_request, 'to_alipay_dict'):
                params['fxiaoke_create_leads_request'] = self.fxiaoke_create_leads_request.to_alipay_dict()
            else:
                params['fxiaoke_create_leads_request'] = self.fxiaoke_create_leads_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalFxiaokeleadsCreateModel()
        if 'fxiaoke_create_leads_request' in d:
            o.fxiaoke_create_leads_request = d['fxiaoke_create_leads_request']
        return o


