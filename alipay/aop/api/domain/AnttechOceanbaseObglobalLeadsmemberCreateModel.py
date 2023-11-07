#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FxiaokeOperateLeadsMemberParams import FxiaokeOperateLeadsMemberParams


class AnttechOceanbaseObglobalLeadsmemberCreateModel(object):

    def __init__(self):
        self._fxiaoke_create_leads_member_request = None

    @property
    def fxiaoke_create_leads_member_request(self):
        return self._fxiaoke_create_leads_member_request

    @fxiaoke_create_leads_member_request.setter
    def fxiaoke_create_leads_member_request(self, value):
        if isinstance(value, FxiaokeOperateLeadsMemberParams):
            self._fxiaoke_create_leads_member_request = value
        else:
            self._fxiaoke_create_leads_member_request = FxiaokeOperateLeadsMemberParams.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fxiaoke_create_leads_member_request:
            if hasattr(self.fxiaoke_create_leads_member_request, 'to_alipay_dict'):
                params['fxiaoke_create_leads_member_request'] = self.fxiaoke_create_leads_member_request.to_alipay_dict()
            else:
                params['fxiaoke_create_leads_member_request'] = self.fxiaoke_create_leads_member_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalLeadsmemberCreateModel()
        if 'fxiaoke_create_leads_member_request' in d:
            o.fxiaoke_create_leads_member_request = d['fxiaoke_create_leads_member_request']
        return o


