#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctoragentapprovalApproveModel(object):

    def __init__(self):
        self._avatar_id = None

    @property
    def avatar_id(self):
        return self._avatar_id

    @avatar_id.setter
    def avatar_id(self, value):
        self._avatar_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar_id:
            if hasattr(self.avatar_id, 'to_alipay_dict'):
                params['avatar_id'] = self.avatar_id.to_alipay_dict()
            else:
                params['avatar_id'] = self.avatar_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctoragentapprovalApproveModel()
        if 'avatar_id' in d:
            o.avatar_id = d['avatar_id']
        return o


