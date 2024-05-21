#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtcDeviceMsgInfo import EtcDeviceMsgInfo


class AlipayCommerceTransportEtcDeivceinfoSendModel(object):

    def __init__(self):
        self._device_info = None

    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, EtcDeviceMsgInfo):
            self._device_info = value
        else:
            self._device_info = EtcDeviceMsgInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcDeivceinfoSendModel()
        if 'device_info' in d:
            o.device_info = d['device_info']
        return o


