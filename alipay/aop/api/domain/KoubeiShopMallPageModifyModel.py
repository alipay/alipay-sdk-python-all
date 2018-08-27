#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiShopMallPageModifyModel(object):

    def __init__(self):
        self._mall_id = None
        self._mall_url = None
        self._out_biz_id = None

    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def mall_url(self):
        return self._mall_url

    @mall_url.setter
    def mall_url(self, value):
        self._mall_url = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.mall_url:
            if hasattr(self.mall_url, 'to_alipay_dict'):
                params['mall_url'] = self.mall_url.to_alipay_dict()
            else:
                params['mall_url'] = self.mall_url
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiShopMallPageModifyModel()
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'mall_url' in d:
            o.mall_url = d['mall_url']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        return o


