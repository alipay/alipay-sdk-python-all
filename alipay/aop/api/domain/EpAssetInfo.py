#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpAssetInfo(object):

    def __init__(self):
        self._asset_type = None
        self._contents = None

    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        self._contents = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.contents:
            if hasattr(self.contents, 'to_alipay_dict'):
                params['contents'] = self.contents.to_alipay_dict()
            else:
                params['contents'] = self.contents
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAssetInfo()
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'contents' in d:
            o.contents = d['contents']
        return o


