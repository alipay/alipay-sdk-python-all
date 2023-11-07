#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FxiaokeUpdateLeadsRequest import FxiaokeUpdateLeadsRequest


class AnttechOceanbaseObglobalLeadsModifyModel(object):

    def __init__(self):
        self._fxiaoke_update_leads_request = None

    @property
    def fxiaoke_update_leads_request(self):
        return self._fxiaoke_update_leads_request

    @fxiaoke_update_leads_request.setter
    def fxiaoke_update_leads_request(self, value):
        if isinstance(value, FxiaokeUpdateLeadsRequest):
            self._fxiaoke_update_leads_request = value
        else:
            self._fxiaoke_update_leads_request = FxiaokeUpdateLeadsRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fxiaoke_update_leads_request:
            if hasattr(self.fxiaoke_update_leads_request, 'to_alipay_dict'):
                params['fxiaoke_update_leads_request'] = self.fxiaoke_update_leads_request.to_alipay_dict()
            else:
                params['fxiaoke_update_leads_request'] = self.fxiaoke_update_leads_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalLeadsModifyModel()
        if 'fxiaoke_update_leads_request' in d:
            o.fxiaoke_update_leads_request = d['fxiaoke_update_leads_request']
        return o


