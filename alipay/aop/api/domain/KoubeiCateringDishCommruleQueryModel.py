#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishCommruleQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._comm_group_id = None
        self._group_detail_id = None
        self._page_no = None
        self._page_size = None
        self._rule_id = None
        self._rule_type = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def comm_group_id(self):
        return self._comm_group_id

    @comm_group_id.setter
    def comm_group_id(self, value):
        self._comm_group_id = value
    @property
    def group_detail_id(self):
        return self._group_detail_id

    @group_detail_id.setter
    def group_detail_id(self, value):
        self._group_detail_id = value
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
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.comm_group_id:
            if hasattr(self.comm_group_id, 'to_alipay_dict'):
                params['comm_group_id'] = self.comm_group_id.to_alipay_dict()
            else:
                params['comm_group_id'] = self.comm_group_id
        if self.group_detail_id:
            if hasattr(self.group_detail_id, 'to_alipay_dict'):
                params['group_detail_id'] = self.group_detail_id.to_alipay_dict()
            else:
                params['group_detail_id'] = self.group_detail_id
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
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishCommruleQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'comm_group_id' in d:
            o.comm_group_id = d['comm_group_id']
        if 'group_detail_id' in d:
            o.group_detail_id = d['group_detail_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        return o


