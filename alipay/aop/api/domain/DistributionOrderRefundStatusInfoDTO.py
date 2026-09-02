#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DistributionOrderRefundStatusInfoDTO(object):

    def __init__(self):
        self._refund_status = None

    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistributionOrderRefundStatusInfoDTO()
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        return o


