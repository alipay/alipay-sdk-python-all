#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdBudgetcutModifyModel(object):

    def __init__(self):
        self._after_principal_amount_yuan = None
        self._alipay_pid = None
        self._amount_yuan = None
        self._assign_mod = None
        self._benefit_amount = None
        self._biz_scene = None
        self._biz_token = None
        self._marketing_amount_yuan = None
        self._principal_amount_yuan = None
        self._principal_tag = None

    @property
    def after_principal_amount_yuan(self):
        return self._after_principal_amount_yuan

    @after_principal_amount_yuan.setter
    def after_principal_amount_yuan(self, value):
        self._after_principal_amount_yuan = value
    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def amount_yuan(self):
        return self._amount_yuan

    @amount_yuan.setter
    def amount_yuan(self, value):
        self._amount_yuan = value
    @property
    def assign_mod(self):
        return self._assign_mod

    @assign_mod.setter
    def assign_mod(self, value):
        self._assign_mod = value
    @property
    def benefit_amount(self):
        return self._benefit_amount

    @benefit_amount.setter
    def benefit_amount(self, value):
        self._benefit_amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def marketing_amount_yuan(self):
        return self._marketing_amount_yuan

    @marketing_amount_yuan.setter
    def marketing_amount_yuan(self, value):
        self._marketing_amount_yuan = value
    @property
    def principal_amount_yuan(self):
        return self._principal_amount_yuan

    @principal_amount_yuan.setter
    def principal_amount_yuan(self, value):
        self._principal_amount_yuan = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_principal_amount_yuan:
            if hasattr(self.after_principal_amount_yuan, 'to_alipay_dict'):
                params['after_principal_amount_yuan'] = self.after_principal_amount_yuan.to_alipay_dict()
            else:
                params['after_principal_amount_yuan'] = self.after_principal_amount_yuan
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.amount_yuan:
            if hasattr(self.amount_yuan, 'to_alipay_dict'):
                params['amount_yuan'] = self.amount_yuan.to_alipay_dict()
            else:
                params['amount_yuan'] = self.amount_yuan
        if self.assign_mod:
            if hasattr(self.assign_mod, 'to_alipay_dict'):
                params['assign_mod'] = self.assign_mod.to_alipay_dict()
            else:
                params['assign_mod'] = self.assign_mod
        if self.benefit_amount:
            if hasattr(self.benefit_amount, 'to_alipay_dict'):
                params['benefit_amount'] = self.benefit_amount.to_alipay_dict()
            else:
                params['benefit_amount'] = self.benefit_amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.marketing_amount_yuan:
            if hasattr(self.marketing_amount_yuan, 'to_alipay_dict'):
                params['marketing_amount_yuan'] = self.marketing_amount_yuan.to_alipay_dict()
            else:
                params['marketing_amount_yuan'] = self.marketing_amount_yuan
        if self.principal_amount_yuan:
            if hasattr(self.principal_amount_yuan, 'to_alipay_dict'):
                params['principal_amount_yuan'] = self.principal_amount_yuan.to_alipay_dict()
            else:
                params['principal_amount_yuan'] = self.principal_amount_yuan
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdBudgetcutModifyModel()
        if 'after_principal_amount_yuan' in d:
            o.after_principal_amount_yuan = d['after_principal_amount_yuan']
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'amount_yuan' in d:
            o.amount_yuan = d['amount_yuan']
        if 'assign_mod' in d:
            o.assign_mod = d['assign_mod']
        if 'benefit_amount' in d:
            o.benefit_amount = d['benefit_amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'marketing_amount_yuan' in d:
            o.marketing_amount_yuan = d['marketing_amount_yuan']
        if 'principal_amount_yuan' in d:
            o.principal_amount_yuan = d['principal_amount_yuan']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        return o


