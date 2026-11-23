#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetPushItem import AssetPushItem


class AlipayDigitalmgmtAdassetsAssetsCreateModel(object):

    def __init__(self):
        self._app_code = None
        self._asset_list = None
        self._category = None
        self._tenant_id = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def asset_list(self):
        return self._asset_list

    @asset_list.setter
    def asset_list(self, value):
        if isinstance(value, list):
            self._asset_list = list()
            for i in value:
                if isinstance(i, AssetPushItem):
                    self._asset_list.append(i)
                else:
                    self._asset_list.append(AssetPushItem.from_alipay_dict(i))
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.asset_list:
            if isinstance(self.asset_list, list):
                for i in range(0, len(self.asset_list)):
                    element = self.asset_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_list[i] = element.to_alipay_dict()
            if hasattr(self.asset_list, 'to_alipay_dict'):
                params['asset_list'] = self.asset_list.to_alipay_dict()
            else:
                params['asset_list'] = self.asset_list
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtAdassetsAssetsCreateModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'asset_list' in d:
            o.asset_list = d['asset_list']
        if 'category' in d:
            o.category = d['category']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


