#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcBindModifyModel(object):

    def __init__(self):
        self._bind_agreement_no = None
        self._binded_mobile = None
        self._card_no = None
        self._device_no = None

    @property
    def bind_agreement_no(self):
        return self._bind_agreement_no

    @bind_agreement_no.setter
    def bind_agreement_no(self, value):
        self._bind_agreement_no = value
    @property
    def binded_mobile(self):
        return self._binded_mobile

    @binded_mobile.setter
    def binded_mobile(self, value):
        self._binded_mobile = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.bind_agreement_no:
            if hasattr(self.bind_agreement_no, 'to_alipay_dict'):
                params['bind_agreement_no'] = self.bind_agreement_no.to_alipay_dict()
            else:
                params['bind_agreement_no'] = self.bind_agreement_no
        if self.binded_mobile:
            if hasattr(self.binded_mobile, 'to_alipay_dict'):
                params['binded_mobile'] = self.binded_mobile.to_alipay_dict()
            else:
                params['binded_mobile'] = self.binded_mobile
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcBindModifyModel()
        if 'bind_agreement_no' in d:
            o.bind_agreement_no = d['bind_agreement_no']
        if 'binded_mobile' in d:
            o.binded_mobile = d['binded_mobile']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'device_no' in d:
            o.device_no = d['device_no']
        return o


