#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemMiniAppUseGuideInfo import AppItemMiniAppUseGuideInfo


class AppItemVoucherUseGuideInfo(object):

    def __init__(self):
        self._app_item_mini_app_use_guide_info = None
        self._use_guide_mode = None

    @property
    def app_item_mini_app_use_guide_info(self):
        return self._app_item_mini_app_use_guide_info

    @app_item_mini_app_use_guide_info.setter
    def app_item_mini_app_use_guide_info(self, value):
        if isinstance(value, AppItemMiniAppUseGuideInfo):
            self._app_item_mini_app_use_guide_info = value
        else:
            self._app_item_mini_app_use_guide_info = AppItemMiniAppUseGuideInfo.from_alipay_dict(value)
    @property
    def use_guide_mode(self):
        return self._use_guide_mode

    @use_guide_mode.setter
    def use_guide_mode(self, value):
        if isinstance(value, list):
            self._use_guide_mode = list()
            for i in value:
                self._use_guide_mode.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_mini_app_use_guide_info:
            if hasattr(self.app_item_mini_app_use_guide_info, 'to_alipay_dict'):
                params['app_item_mini_app_use_guide_info'] = self.app_item_mini_app_use_guide_info.to_alipay_dict()
            else:
                params['app_item_mini_app_use_guide_info'] = self.app_item_mini_app_use_guide_info
        if self.use_guide_mode:
            if isinstance(self.use_guide_mode, list):
                for i in range(0, len(self.use_guide_mode)):
                    element = self.use_guide_mode[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.use_guide_mode[i] = element.to_alipay_dict()
            if hasattr(self.use_guide_mode, 'to_alipay_dict'):
                params['use_guide_mode'] = self.use_guide_mode.to_alipay_dict()
            else:
                params['use_guide_mode'] = self.use_guide_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherUseGuideInfo()
        if 'app_item_mini_app_use_guide_info' in d:
            o.app_item_mini_app_use_guide_info = d['app_item_mini_app_use_guide_info']
        if 'use_guide_mode' in d:
            o.use_guide_mode = d['use_guide_mode']
        return o


