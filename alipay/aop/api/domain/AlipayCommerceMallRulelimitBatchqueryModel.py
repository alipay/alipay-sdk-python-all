#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMallRulelimitBatchqueryModel(object):

    def __init__(self):
        self._biz_rule_id = None
        self._mall_id = None
        self._page_no = None
        self._page_size = None
        self._rule_scene = None

    @property
    def biz_rule_id(self):
        return self._biz_rule_id

    @biz_rule_id.setter
    def biz_rule_id(self, value):
        self._biz_rule_id = value
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def rule_scene(self):
        return self._rule_scene

    @rule_scene.setter
    def rule_scene(self, value):
        self._rule_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_rule_id:
            if hasattr(self.biz_rule_id, 'to_alipay_dict'):
                params['biz_rule_id'] = self.biz_rule_id.to_alipay_dict()
            else:
                params['biz_rule_id'] = self.biz_rule_id
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.rule_scene:
            if hasattr(self.rule_scene, 'to_alipay_dict'):
                params['rule_scene'] = self.rule_scene.to_alipay_dict()
            else:
                params['rule_scene'] = self.rule_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMallRulelimitBatchqueryModel()
        if 'biz_rule_id' in d:
            o.biz_rule_id = d['biz_rule_id']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'rule_scene' in d:
            o.rule_scene = d['rule_scene']
        return o


