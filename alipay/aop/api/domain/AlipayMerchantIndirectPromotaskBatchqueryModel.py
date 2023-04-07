#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectPromotaskBatchqueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._group_mid = None
        self._page_size = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def group_mid(self):
        return self._group_mid

    @group_mid.setter
    def group_mid(self, value):
        self._group_mid = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.group_mid:
            if hasattr(self.group_mid, 'to_alipay_dict'):
                params['group_mid'] = self.group_mid.to_alipay_dict()
            else:
                params['group_mid'] = self.group_mid
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectPromotaskBatchqueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'group_mid' in d:
            o.group_mid = d['group_mid']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


