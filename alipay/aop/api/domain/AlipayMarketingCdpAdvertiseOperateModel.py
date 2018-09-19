#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCdpAdvertiseOperateModel(object):

    def __init__(self):
        self._ad_id = None
        self._operate_type = None

    @property
    def ad_id(self):
        return self._ad_id

    @ad_id.setter
    def ad_id(self, value):
        self._ad_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_id:
            if hasattr(self.ad_id, 'to_alipay_dict'):
                params['ad_id'] = self.ad_id.to_alipay_dict()
            else:
                params['ad_id'] = self.ad_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCdpAdvertiseOperateModel()
        if 'ad_id' in d:
            o.ad_id = d['ad_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


