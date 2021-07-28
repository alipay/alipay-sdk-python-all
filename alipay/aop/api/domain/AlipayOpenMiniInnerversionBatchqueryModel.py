#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppVersionQueryInfo import MiniAppVersionQueryInfo


class AlipayOpenMiniInnerversionBatchqueryModel(object):

    def __init__(self):
        self._bundle_id = None
        self._mini_app_id = None
        self._version_list = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def version_list(self):
        return self._version_list

    @version_list.setter
    def version_list(self, value):
        if isinstance(value, list):
            self._version_list = list()
            for i in value:
                if isinstance(i, MiniAppVersionQueryInfo):
                    self._version_list.append(i)
                else:
                    self._version_list.append(MiniAppVersionQueryInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.version_list:
            if isinstance(self.version_list, list):
                for i in range(0, len(self.version_list)):
                    element = self.version_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.version_list[i] = element.to_alipay_dict()
            if hasattr(self.version_list, 'to_alipay_dict'):
                params['version_list'] = self.version_list.to_alipay_dict()
            else:
                params['version_list'] = self.version_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionBatchqueryModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'version_list' in d:
            o.version_list = d['version_list']
        return o


