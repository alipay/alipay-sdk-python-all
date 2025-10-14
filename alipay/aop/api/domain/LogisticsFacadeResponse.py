#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsFacadeResponse(object):

    def __init__(self):
        self._delivery_status = None
        self._tracking_number = None

    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, value):
        self._tracking_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_status:
            if hasattr(self.delivery_status, 'to_alipay_dict'):
                params['delivery_status'] = self.delivery_status.to_alipay_dict()
            else:
                params['delivery_status'] = self.delivery_status
        if self.tracking_number:
            if hasattr(self.tracking_number, 'to_alipay_dict'):
                params['tracking_number'] = self.tracking_number.to_alipay_dict()
            else:
                params['tracking_number'] = self.tracking_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsFacadeResponse()
        if 'delivery_status' in d:
            o.delivery_status = d['delivery_status']
        if 'tracking_number' in d:
            o.tracking_number = d['tracking_number']
        return o


