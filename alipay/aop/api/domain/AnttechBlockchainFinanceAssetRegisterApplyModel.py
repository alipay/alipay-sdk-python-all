#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceAssetRegisterApplyModel(object):

    def __init__(self):
        self._asset_info = None
        self._asset_type = None
        self._out_asset_id = None

    @property
    def asset_info(self):
        return self._asset_info

    @asset_info.setter
    def asset_info(self, value):
        self._asset_info = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def out_asset_id(self):
        return self._out_asset_id

    @out_asset_id.setter
    def out_asset_id(self, value):
        self._out_asset_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_info:
            if hasattr(self.asset_info, 'to_alipay_dict'):
                params['asset_info'] = self.asset_info.to_alipay_dict()
            else:
                params['asset_info'] = self.asset_info
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.out_asset_id:
            if hasattr(self.out_asset_id, 'to_alipay_dict'):
                params['out_asset_id'] = self.out_asset_id.to_alipay_dict()
            else:
                params['out_asset_id'] = self.out_asset_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAssetRegisterApplyModel()
        if 'asset_info' in d:
            o.asset_info = d['asset_info']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'out_asset_id' in d:
            o.out_asset_id = d['out_asset_id']
        return o


