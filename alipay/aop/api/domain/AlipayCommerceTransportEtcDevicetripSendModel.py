#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtcDeviceTripInfo import EtcDeviceTripInfo


class AlipayCommerceTransportEtcDevicetripSendModel(object):

    def __init__(self):
        self._card_no = None
        self._device_no = None
        self._trip_ino = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def trip_ino(self):
        return self._trip_ino

    @trip_ino.setter
    def trip_ino(self, value):
        if isinstance(value, EtcDeviceTripInfo):
            self._trip_ino = value
        else:
            self._trip_ino = EtcDeviceTripInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.trip_ino:
            if hasattr(self.trip_ino, 'to_alipay_dict'):
                params['trip_ino'] = self.trip_ino.to_alipay_dict()
            else:
                params['trip_ino'] = self.trip_ino
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcDevicetripSendModel()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'trip_ino' in d:
            o.trip_ino = d['trip_ino']
        return o


