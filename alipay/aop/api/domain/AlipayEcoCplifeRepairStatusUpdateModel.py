#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCplifeRepairStatusUpdateModel(object):

    def __init__(self):
        self._biz_details = None
        self._biz_state = None
        self._req_id = None

    @property
    def biz_details(self):
        return self._biz_details

    @biz_details.setter
    def biz_details(self, value):
        self._biz_details = value
    @property
    def biz_state(self):
        return self._biz_state

    @biz_state.setter
    def biz_state(self, value):
        self._biz_state = value
    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, value):
        self._req_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_details:
            if hasattr(self.biz_details, 'to_alipay_dict'):
                params['biz_details'] = self.biz_details.to_alipay_dict()
            else:
                params['biz_details'] = self.biz_details
        if self.biz_state:
            if hasattr(self.biz_state, 'to_alipay_dict'):
                params['biz_state'] = self.biz_state.to_alipay_dict()
            else:
                params['biz_state'] = self.biz_state
        if self.req_id:
            if hasattr(self.req_id, 'to_alipay_dict'):
                params['req_id'] = self.req_id.to_alipay_dict()
            else:
                params['req_id'] = self.req_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeRepairStatusUpdateModel()
        if 'biz_details' in d:
            o.biz_details = d['biz_details']
        if 'biz_state' in d:
            o.biz_state = d['biz_state']
        if 'req_id' in d:
            o.req_id = d['req_id']
        return o


