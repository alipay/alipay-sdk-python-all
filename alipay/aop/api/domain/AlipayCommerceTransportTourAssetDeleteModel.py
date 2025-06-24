#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetOutPutRequest import AssetOutPutRequest


class AlipayCommerceTransportTourAssetDeleteModel(object):

    def __init__(self):
        self._asset_out_put_list = None

    @property
    def asset_out_put_list(self):
        return self._asset_out_put_list

    @asset_out_put_list.setter
    def asset_out_put_list(self, value):
        if isinstance(value, list):
            self._asset_out_put_list = list()
            for i in value:
                if isinstance(i, AssetOutPutRequest):
                    self._asset_out_put_list.append(i)
                else:
                    self._asset_out_put_list.append(AssetOutPutRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset_out_put_list:
            if isinstance(self.asset_out_put_list, list):
                for i in range(0, len(self.asset_out_put_list)):
                    element = self.asset_out_put_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_out_put_list[i] = element.to_alipay_dict()
            if hasattr(self.asset_out_put_list, 'to_alipay_dict'):
                params['asset_out_put_list'] = self.asset_out_put_list.to_alipay_dict()
            else:
                params['asset_out_put_list'] = self.asset_out_put_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTourAssetDeleteModel()
        if 'asset_out_put_list' in d:
            o.asset_out_put_list = d['asset_out_put_list']
        return o


