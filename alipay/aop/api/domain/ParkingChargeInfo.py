#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParkingChargeInfo(object):

    def __init__(self):
        self._charge_fee = None
        self._charge_node = None
        self._charge_time = None

    @property
    def charge_fee(self):
        return self._charge_fee

    @charge_fee.setter
    def charge_fee(self, value):
        self._charge_fee = value
    @property
    def charge_node(self):
        return self._charge_node

    @charge_node.setter
    def charge_node(self, value):
        self._charge_node = value
    @property
    def charge_time(self):
        return self._charge_time

    @charge_time.setter
    def charge_time(self, value):
        self._charge_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_fee:
            if hasattr(self.charge_fee, 'to_alipay_dict'):
                params['charge_fee'] = self.charge_fee.to_alipay_dict()
            else:
                params['charge_fee'] = self.charge_fee
        if self.charge_node:
            if hasattr(self.charge_node, 'to_alipay_dict'):
                params['charge_node'] = self.charge_node.to_alipay_dict()
            else:
                params['charge_node'] = self.charge_node
        if self.charge_time:
            if hasattr(self.charge_time, 'to_alipay_dict'):
                params['charge_time'] = self.charge_time.to_alipay_dict()
            else:
                params['charge_time'] = self.charge_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParkingChargeInfo()
        if 'charge_fee' in d:
            o.charge_fee = d['charge_fee']
        if 'charge_node' in d:
            o.charge_node = d['charge_node']
        if 'charge_time' in d:
            o.charge_time = d['charge_time']
        return o


