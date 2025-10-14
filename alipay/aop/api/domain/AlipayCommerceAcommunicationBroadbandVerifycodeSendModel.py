#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationBroadbandVerifycodeSendModel(object):

    def __init__(self):
        self._contact_phone_number = None
        self._scene = None

    @property
    def contact_phone_number(self):
        return self._contact_phone_number

    @contact_phone_number.setter
    def contact_phone_number(self, value):
        self._contact_phone_number = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_phone_number:
            if hasattr(self.contact_phone_number, 'to_alipay_dict'):
                params['contact_phone_number'] = self.contact_phone_number.to_alipay_dict()
            else:
                params['contact_phone_number'] = self.contact_phone_number
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationBroadbandVerifycodeSendModel()
        if 'contact_phone_number' in d:
            o.contact_phone_number = d['contact_phone_number']
        if 'scene' in d:
            o.scene = d['scene']
        return o


