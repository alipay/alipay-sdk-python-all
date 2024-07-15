#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrivateChargingOrder import PrivateChargingOrder


class AlipayCommerceTransportChargerPrivatefulfillmentSyncModel(object):

    def __init__(self):
        self._fulfillment = None

    @property
    def fulfillment(self):
        return self._fulfillment

    @fulfillment.setter
    def fulfillment(self, value):
        if isinstance(value, PrivateChargingOrder):
            self._fulfillment = value
        else:
            self._fulfillment = PrivateChargingOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment:
            if hasattr(self.fulfillment, 'to_alipay_dict'):
                params['fulfillment'] = self.fulfillment.to_alipay_dict()
            else:
                params['fulfillment'] = self.fulfillment
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerPrivatefulfillmentSyncModel()
        if 'fulfillment' in d:
            o.fulfillment = d['fulfillment']
        return o


