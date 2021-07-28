#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCommRuleShowInfo import KbdishCommRuleShowInfo


class KbdishCommRuleInfo(object):

    def __init__(self):
        self._biz_id = None
        self._comm_group_id = None
        self._create_user = None
        self._group_detail_id = None
        self._merchant_id = None
        self._rule_id = None
        self._rule_type = None
        self._show_rule_list = None
        self._syn_type = None
        self._update_user = None

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
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def group_detail_id(self):
        return self._group_detail_id

    @group_detail_id.setter
    def group_detail_id(self, value):
        self._group_detail_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
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
    @property
    def show_rule_list(self):
        return self._show_rule_list

    @show_rule_list.setter
    def show_rule_list(self, value):
        if isinstance(value, list):
            self._show_rule_list = list()
            for i in value:
                if isinstance(i, KbdishCommRuleShowInfo):
                    self._show_rule_list.append(i)
                else:
                    self._show_rule_list.append(KbdishCommRuleShowInfo.from_alipay_dict(i))
    @property
    def syn_type(self):
        return self._syn_type

    @syn_type.setter
    def syn_type(self, value):
        self._syn_type = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


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
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.group_detail_id:
            if hasattr(self.group_detail_id, 'to_alipay_dict'):
                params['group_detail_id'] = self.group_detail_id.to_alipay_dict()
            else:
                params['group_detail_id'] = self.group_detail_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
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
        if self.show_rule_list:
            if isinstance(self.show_rule_list, list):
                for i in range(0, len(self.show_rule_list)):
                    element = self.show_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.show_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.show_rule_list, 'to_alipay_dict'):
                params['show_rule_list'] = self.show_rule_list.to_alipay_dict()
            else:
                params['show_rule_list'] = self.show_rule_list
        if self.syn_type:
            if hasattr(self.syn_type, 'to_alipay_dict'):
                params['syn_type'] = self.syn_type.to_alipay_dict()
            else:
                params['syn_type'] = self.syn_type
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishCommRuleInfo()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'comm_group_id' in d:
            o.comm_group_id = d['comm_group_id']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'group_detail_id' in d:
            o.group_detail_id = d['group_detail_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'show_rule_list' in d:
            o.show_rule_list = d['show_rule_list']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


