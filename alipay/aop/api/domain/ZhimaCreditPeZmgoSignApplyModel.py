#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignExtendInfo import SignExtendInfo


class ZhimaCreditPeZmgoSignApplyModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._channel = None
        self._extend_params = None
        self._freeze_amount = None
        self._out_request_no = None
        self._partner_id = None
        self._preorder_no = None
        self._template_id = None
        self._timeout_express = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, SignExtendInfo):
            self._extend_params = value
        else:
            self._extend_params = SignExtendInfo.from_alipay_dict(value)
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def preorder_no(self):
        return self._preorder_no

    @preorder_no.setter
    def preorder_no(self, value):
        self._preorder_no = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.preorder_no:
            if hasattr(self.preorder_no, 'to_alipay_dict'):
                params['preorder_no'] = self.preorder_no.to_alipay_dict()
            else:
                params['preorder_no'] = self.preorder_no
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeZmgoSignApplyModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'preorder_no' in d:
            o.preorder_no = d['preorder_no']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        return o


