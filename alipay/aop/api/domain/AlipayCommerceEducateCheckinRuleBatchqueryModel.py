#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCheckinRuleBatchqueryModel(object):

    def __init__(self):
        self._enable_status = None
        self._inst_id = None
        self._page_num = None
        self._page_size = None
        self._rule_name = None

    @property
    def enable_status(self):
        return self._enable_status

    @enable_status.setter
    def enable_status(self, value):
        self._enable_status = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable_status:
            if hasattr(self.enable_status, 'to_alipay_dict'):
                params['enable_status'] = self.enable_status.to_alipay_dict()
            else:
                params['enable_status'] = self.enable_status
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCheckinRuleBatchqueryModel()
        if 'enable_status' in d:
            o.enable_status = d['enable_status']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        return o


