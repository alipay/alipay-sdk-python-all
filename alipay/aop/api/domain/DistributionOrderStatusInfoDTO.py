#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DistributionOrderStatusInfoDTO(object):

    def __init__(self):
        self._close_reason = None
        self._source_status = None
        self._status = None

    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def source_status(self):
        return self._source_status

    @source_status.setter
    def source_status(self, value):
        self._source_status = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.source_status:
            if hasattr(self.source_status, 'to_alipay_dict'):
                params['source_status'] = self.source_status.to_alipay_dict()
            else:
                params['source_status'] = self.source_status
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
        o = DistributionOrderStatusInfoDTO()
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'source_status' in d:
            o.source_status = d['source_status']
        if 'status' in d:
            o.status = d['status']
        return o


