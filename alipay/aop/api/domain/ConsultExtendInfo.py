#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultExtendInfo(object):

    def __init__(self):
        self._campaign_type = None
        self._card_bin = None
        self._card_type = None
        self._inst_id = None

    @property
    def campaign_type(self):
        return self._campaign_type

    @campaign_type.setter
    def campaign_type(self, value):
        self._campaign_type = value
    @property
    def card_bin(self):
        return self._card_bin

    @card_bin.setter
    def card_bin(self, value):
        self._card_bin = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_type:
            if hasattr(self.campaign_type, 'to_alipay_dict'):
                params['campaign_type'] = self.campaign_type.to_alipay_dict()
            else:
                params['campaign_type'] = self.campaign_type
        if self.card_bin:
            if hasattr(self.card_bin, 'to_alipay_dict'):
                params['card_bin'] = self.card_bin.to_alipay_dict()
            else:
                params['card_bin'] = self.card_bin
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultExtendInfo()
        if 'campaign_type' in d:
            o.campaign_type = d['campaign_type']
        if 'card_bin' in d:
            o.card_bin = d['card_bin']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        return o


