#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode


class AnttechBlockchainFinanceEnergyaggrInvitedeclareApplyModel(object):

    def __init__(self):
        self._declare_flag = None
        self._product_agreement_code = None
        self._sub_invite_id = None
        self._target_adjustment = None

    @property
    def declare_flag(self):
        return self._declare_flag

    @declare_flag.setter
    def declare_flag(self, value):
        self._declare_flag = value
    @property
    def product_agreement_code(self):
        return self._product_agreement_code

    @product_agreement_code.setter
    def product_agreement_code(self, value):
        self._product_agreement_code = value
    @property
    def sub_invite_id(self):
        return self._sub_invite_id

    @sub_invite_id.setter
    def sub_invite_id(self, value):
        self._sub_invite_id = value
    @property
    def target_adjustment(self):
        return self._target_adjustment

    @target_adjustment.setter
    def target_adjustment(self, value):
        if isinstance(value, list):
            self._target_adjustment = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._target_adjustment.append(i)
                else:
                    self._target_adjustment.append(LoadInfoNode.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.declare_flag:
            if hasattr(self.declare_flag, 'to_alipay_dict'):
                params['declare_flag'] = self.declare_flag.to_alipay_dict()
            else:
                params['declare_flag'] = self.declare_flag
        if self.product_agreement_code:
            if hasattr(self.product_agreement_code, 'to_alipay_dict'):
                params['product_agreement_code'] = self.product_agreement_code.to_alipay_dict()
            else:
                params['product_agreement_code'] = self.product_agreement_code
        if self.sub_invite_id:
            if hasattr(self.sub_invite_id, 'to_alipay_dict'):
                params['sub_invite_id'] = self.sub_invite_id.to_alipay_dict()
            else:
                params['sub_invite_id'] = self.sub_invite_id
        if self.target_adjustment:
            if isinstance(self.target_adjustment, list):
                for i in range(0, len(self.target_adjustment)):
                    element = self.target_adjustment[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_adjustment[i] = element.to_alipay_dict()
            if hasattr(self.target_adjustment, 'to_alipay_dict'):
                params['target_adjustment'] = self.target_adjustment.to_alipay_dict()
            else:
                params['target_adjustment'] = self.target_adjustment
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergyaggrInvitedeclareApplyModel()
        if 'declare_flag' in d:
            o.declare_flag = d['declare_flag']
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        if 'sub_invite_id' in d:
            o.sub_invite_id = d['sub_invite_id']
        if 'target_adjustment' in d:
            o.target_adjustment = d['target_adjustment']
        return o


