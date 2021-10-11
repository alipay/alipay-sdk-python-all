#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayerAccountDTO(object):

    def __init__(self):
        self._asset_display_name = None
        self._asset_type = None

    @property
    def asset_display_name(self):
        return self._asset_display_name

    @asset_display_name.setter
    def asset_display_name(self, value):
        self._asset_display_name = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_display_name:
            if hasattr(self.asset_display_name, 'to_alipay_dict'):
                params['asset_display_name'] = self.asset_display_name.to_alipay_dict()
            else:
                params['asset_display_name'] = self.asset_display_name
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayerAccountDTO()
        if 'asset_display_name' in d:
            o.asset_display_name = d['asset_display_name']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        return o


