#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantOrderSnstradeQueryModel(object):

    def __init__(self):
        self._asset_access_id = None
        self._biz_date = None
        self._ch_info = None

    @property
    def asset_access_id(self):
        return self._asset_access_id

    @asset_access_id.setter
    def asset_access_id(self, value):
        self._asset_access_id = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_access_id:
            if hasattr(self.asset_access_id, 'to_alipay_dict'):
                params['asset_access_id'] = self.asset_access_id.to_alipay_dict()
            else:
                params['asset_access_id'] = self.asset_access_id
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantOrderSnstradeQueryModel()
        if 'asset_access_id' in d:
            o.asset_access_id = d['asset_access_id']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        return o


