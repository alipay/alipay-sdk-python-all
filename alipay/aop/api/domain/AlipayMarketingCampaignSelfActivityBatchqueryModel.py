#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignSelfActivityBatchqueryModel(object):

    def __init__(self):
        self._need_use_scope_info = None
        self._page_number = None
        self._page_size = None
        self._scene_code = None

    @property
    def need_use_scope_info(self):
        return self._need_use_scope_info

    @need_use_scope_info.setter
    def need_use_scope_info(self, value):
        if isinstance(value, list):
            self._need_use_scope_info = list()
            for i in value:
                self._need_use_scope_info.append(i)
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        if isinstance(value, list):
            self._scene_code = list()
            for i in value:
                self._scene_code.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.need_use_scope_info:
            if isinstance(self.need_use_scope_info, list):
                for i in range(0, len(self.need_use_scope_info)):
                    element = self.need_use_scope_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.need_use_scope_info[i] = element.to_alipay_dict()
            if hasattr(self.need_use_scope_info, 'to_alipay_dict'):
                params['need_use_scope_info'] = self.need_use_scope_info.to_alipay_dict()
            else:
                params['need_use_scope_info'] = self.need_use_scope_info
        if self.page_number:
            if hasattr(self.page_number, 'to_alipay_dict'):
                params['page_number'] = self.page_number.to_alipay_dict()
            else:
                params['page_number'] = self.page_number
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.scene_code:
            if isinstance(self.scene_code, list):
                for i in range(0, len(self.scene_code)):
                    element = self.scene_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_code[i] = element.to_alipay_dict()
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignSelfActivityBatchqueryModel()
        if 'need_use_scope_info' in d:
            o.need_use_scope_info = d['need_use_scope_info']
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


