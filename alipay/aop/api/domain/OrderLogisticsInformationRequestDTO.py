#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderLogisticsInformationRequestDTO(object):

    def __init__(self):
        self._logistics_code = None
        self._tracking_no = None

    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.tracking_no:
            if hasattr(self.tracking_no, 'to_alipay_dict'):
                params['tracking_no'] = self.tracking_no.to_alipay_dict()
            else:
                params['tracking_no'] = self.tracking_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderLogisticsInformationRequestDTO()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        return o


