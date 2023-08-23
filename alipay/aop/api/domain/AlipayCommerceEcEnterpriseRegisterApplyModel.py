#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEnterpriseRegisterApplyModel(object):

    def __init__(self):
        self._enterprise_alias = None
        self._enterprise_email = None
        self._enterprise_name = None
        self._out_biz_no = None
        self._parent_enterprise_id = None

    @property
    def enterprise_alias(self):
        return self._enterprise_alias

    @enterprise_alias.setter
    def enterprise_alias(self, value):
        self._enterprise_alias = value
    @property
    def enterprise_email(self):
        return self._enterprise_email

    @enterprise_email.setter
    def enterprise_email(self, value):
        self._enterprise_email = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def parent_enterprise_id(self):
        return self._parent_enterprise_id

    @parent_enterprise_id.setter
    def parent_enterprise_id(self, value):
        self._parent_enterprise_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_alias:
            if hasattr(self.enterprise_alias, 'to_alipay_dict'):
                params['enterprise_alias'] = self.enterprise_alias.to_alipay_dict()
            else:
                params['enterprise_alias'] = self.enterprise_alias
        if self.enterprise_email:
            if hasattr(self.enterprise_email, 'to_alipay_dict'):
                params['enterprise_email'] = self.enterprise_email.to_alipay_dict()
            else:
                params['enterprise_email'] = self.enterprise_email
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.parent_enterprise_id:
            if hasattr(self.parent_enterprise_id, 'to_alipay_dict'):
                params['parent_enterprise_id'] = self.parent_enterprise_id.to_alipay_dict()
            else:
                params['parent_enterprise_id'] = self.parent_enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEnterpriseRegisterApplyModel()
        if 'enterprise_alias' in d:
            o.enterprise_alias = d['enterprise_alias']
        if 'enterprise_email' in d:
            o.enterprise_email = d['enterprise_email']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'parent_enterprise_id' in d:
            o.parent_enterprise_id = d['parent_enterprise_id']
        return o


