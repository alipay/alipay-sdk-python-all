#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoutingThresholdDTO(object):

    def __init__(self):
        self._offshore_to_onshore_bps = None
        self._onshore_to_offshore_bps = None

    @property
    def offshore_to_onshore_bps(self):
        return self._offshore_to_onshore_bps

    @offshore_to_onshore_bps.setter
    def offshore_to_onshore_bps(self, value):
        self._offshore_to_onshore_bps = value
    @property
    def onshore_to_offshore_bps(self):
        return self._onshore_to_offshore_bps

    @onshore_to_offshore_bps.setter
    def onshore_to_offshore_bps(self, value):
        self._onshore_to_offshore_bps = value


    def to_alipay_dict(self):
        params = dict()
        if self.offshore_to_onshore_bps:
            if hasattr(self.offshore_to_onshore_bps, 'to_alipay_dict'):
                params['offshore_to_onshore_bps'] = self.offshore_to_onshore_bps.to_alipay_dict()
            else:
                params['offshore_to_onshore_bps'] = self.offshore_to_onshore_bps
        if self.onshore_to_offshore_bps:
            if hasattr(self.onshore_to_offshore_bps, 'to_alipay_dict'):
                params['onshore_to_offshore_bps'] = self.onshore_to_offshore_bps.to_alipay_dict()
            else:
                params['onshore_to_offshore_bps'] = self.onshore_to_offshore_bps
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoutingThresholdDTO()
        if 'offshore_to_onshore_bps' in d:
            o.offshore_to_onshore_bps = d['offshore_to_onshore_bps']
        if 'onshore_to_offshore_bps' in d:
            o.onshore_to_offshore_bps = d['onshore_to_offshore_bps']
        return o


