#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetInfoForm(object):

    def __init__(self):
        self._asset_no = None
        self._asset_type = None

    @property
    def asset_no(self):
        return self._asset_no

    @asset_no.setter
    def asset_no(self, value):
        self._asset_no = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_no:
            if hasattr(self.asset_no, 'to_alipay_dict'):
                params['asset_no'] = self.asset_no.to_alipay_dict()
            else:
                params['asset_no'] = self.asset_no
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
        o = AssetInfoForm()
        if 'asset_no' in d:
            o.asset_no = d['asset_no']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        return o


