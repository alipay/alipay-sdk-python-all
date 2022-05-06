#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JointAccountQuotaDTO import JointAccountQuotaDTO
from alipay.aop.api.domain.AuthorizeDetailDTO import AuthorizeDetailDTO
from alipay.aop.api.domain.AuthorizedRuleDTO import AuthorizedRuleDTO
from alipay.aop.api.domain.InviteMemberForm import InviteMemberForm


class AlipayFundJointaccountSignModel(object):

    def __init__(self):
        self._account_name = None
        self._account_quota = None
        self._authorized_detail_list = None
        self._authorized_rule = None
        self._biz_scene = None
        self._identity = None
        self._identity_type = None
        self._invitee_list = None
        self._name = None
        self._open_timeout = None
        self._out_biz_no = None
        self._out_entity_id = None
        self._out_source = None
        self._product_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_quota(self):
        return self._account_quota

    @account_quota.setter
    def account_quota(self, value):
        if isinstance(value, list):
            self._account_quota = list()
            for i in value:
                if isinstance(i, JointAccountQuotaDTO):
                    self._account_quota.append(i)
                else:
                    self._account_quota.append(JointAccountQuotaDTO.from_alipay_dict(i))
    @property
    def authorized_detail_list(self):
        return self._authorized_detail_list

    @authorized_detail_list.setter
    def authorized_detail_list(self, value):
        if isinstance(value, list):
            self._authorized_detail_list = list()
            for i in value:
                if isinstance(i, AuthorizeDetailDTO):
                    self._authorized_detail_list.append(i)
                else:
                    self._authorized_detail_list.append(AuthorizeDetailDTO.from_alipay_dict(i))
    @property
    def authorized_rule(self):
        return self._authorized_rule

    @authorized_rule.setter
    def authorized_rule(self, value):
        if isinstance(value, AuthorizedRuleDTO):
            self._authorized_rule = value
        else:
            self._authorized_rule = AuthorizedRuleDTO.from_alipay_dict(value)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def invitee_list(self):
        return self._invitee_list

    @invitee_list.setter
    def invitee_list(self, value):
        if isinstance(value, list):
            self._invitee_list = list()
            for i in value:
                if isinstance(i, InviteMemberForm):
                    self._invitee_list.append(i)
                else:
                    self._invitee_list.append(InviteMemberForm.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_timeout(self):
        return self._open_timeout

    @open_timeout.setter
    def open_timeout(self, value):
        self._open_timeout = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_entity_id(self):
        return self._out_entity_id

    @out_entity_id.setter
    def out_entity_id(self, value):
        self._out_entity_id = value
    @property
    def out_source(self):
        return self._out_source

    @out_source.setter
    def out_source(self, value):
        self._out_source = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_quota:
            if isinstance(self.account_quota, list):
                for i in range(0, len(self.account_quota)):
                    element = self.account_quota[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.account_quota[i] = element.to_alipay_dict()
            if hasattr(self.account_quota, 'to_alipay_dict'):
                params['account_quota'] = self.account_quota.to_alipay_dict()
            else:
                params['account_quota'] = self.account_quota
        if self.authorized_detail_list:
            if isinstance(self.authorized_detail_list, list):
                for i in range(0, len(self.authorized_detail_list)):
                    element = self.authorized_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authorized_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.authorized_detail_list, 'to_alipay_dict'):
                params['authorized_detail_list'] = self.authorized_detail_list.to_alipay_dict()
            else:
                params['authorized_detail_list'] = self.authorized_detail_list
        if self.authorized_rule:
            if hasattr(self.authorized_rule, 'to_alipay_dict'):
                params['authorized_rule'] = self.authorized_rule.to_alipay_dict()
            else:
                params['authorized_rule'] = self.authorized_rule
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.invitee_list:
            if isinstance(self.invitee_list, list):
                for i in range(0, len(self.invitee_list)):
                    element = self.invitee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invitee_list[i] = element.to_alipay_dict()
            if hasattr(self.invitee_list, 'to_alipay_dict'):
                params['invitee_list'] = self.invitee_list.to_alipay_dict()
            else:
                params['invitee_list'] = self.invitee_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_timeout:
            if hasattr(self.open_timeout, 'to_alipay_dict'):
                params['open_timeout'] = self.open_timeout.to_alipay_dict()
            else:
                params['open_timeout'] = self.open_timeout
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_entity_id:
            if hasattr(self.out_entity_id, 'to_alipay_dict'):
                params['out_entity_id'] = self.out_entity_id.to_alipay_dict()
            else:
                params['out_entity_id'] = self.out_entity_id
        if self.out_source:
            if hasattr(self.out_source, 'to_alipay_dict'):
                params['out_source'] = self.out_source.to_alipay_dict()
            else:
                params['out_source'] = self.out_source
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundJointaccountSignModel()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_quota' in d:
            o.account_quota = d['account_quota']
        if 'authorized_detail_list' in d:
            o.authorized_detail_list = d['authorized_detail_list']
        if 'authorized_rule' in d:
            o.authorized_rule = d['authorized_rule']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'invitee_list' in d:
            o.invitee_list = d['invitee_list']
        if 'name' in d:
            o.name = d['name']
        if 'open_timeout' in d:
            o.open_timeout = d['open_timeout']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_entity_id' in d:
            o.out_entity_id = d['out_entity_id']
        if 'out_source' in d:
            o.out_source = d['out_source']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


