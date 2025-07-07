#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandAeactivityPlatformQueryModel(object):

    def __init__(self):
        self._ele_shopid = None

    @property
    def ele_shopid(self):
        return self._ele_shopid

    @ele_shopid.setter
    def ele_shopid(self, value):
        self._ele_shopid = value


    def to_alipay_dict(self):
        params = dict()
        if self.ele_shopid:
            if hasattr(self.ele_shopid, 'to_alipay_dict'):
                params['ele_shopid'] = self.ele_shopid.to_alipay_dict()
            else:
                params['ele_shopid'] = self.ele_shopid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAeactivityPlatformQueryModel()
        if 'ele_shopid' in d:
            o.ele_shopid = d['ele_shopid']
        return o


