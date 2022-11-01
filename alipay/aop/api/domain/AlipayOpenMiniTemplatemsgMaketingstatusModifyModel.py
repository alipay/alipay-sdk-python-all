#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniTemplatemsgMaketingstatusModifyModel(object):

    def __init__(self):
        self._detail_id = None
        self._status = None

    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniTemplatemsgMaketingstatusModifyModel()
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'status' in d:
            o.status = d['status']
        return o


