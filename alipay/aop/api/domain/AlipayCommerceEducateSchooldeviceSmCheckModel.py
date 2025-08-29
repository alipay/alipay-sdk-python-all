#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSchooldeviceSmCheckModel(object):

    def __init__(self):
        self._activity_code = None
        self._biz_code = None
        self._sm_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def sm_id(self):
        return self._sm_id

    @sm_id.setter
    def sm_id(self, value):
        self._sm_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.sm_id:
            if hasattr(self.sm_id, 'to_alipay_dict'):
                params['sm_id'] = self.sm_id.to_alipay_dict()
            else:
                params['sm_id'] = self.sm_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSchooldeviceSmCheckModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'sm_id' in d:
            o.sm_id = d['sm_id']
        return o


