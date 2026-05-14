#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleForceQueryCouponResponseDTO(object):

    def __init__(self):
        self._approval_status = None
        self._id = None
        self._process_url = None

    @property
    def approval_status(self):
        return self._approval_status

    @approval_status.setter
    def approval_status(self, value):
        self._approval_status = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def process_url(self):
        return self._process_url

    @process_url.setter
    def process_url(self, value):
        self._process_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.approval_status:
            if hasattr(self.approval_status, 'to_alipay_dict'):
                params['approval_status'] = self.approval_status.to_alipay_dict()
            else:
                params['approval_status'] = self.approval_status
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.process_url:
            if hasattr(self.process_url, 'to_alipay_dict'):
                params['process_url'] = self.process_url.to_alipay_dict()
            else:
                params['process_url'] = self.process_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleForceQueryCouponResponseDTO()
        if 'approval_status' in d:
            o.approval_status = d['approval_status']
        if 'id' in d:
            o.id = d['id']
        if 'process_url' in d:
            o.process_url = d['process_url']
        return o


