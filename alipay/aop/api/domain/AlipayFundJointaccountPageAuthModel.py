#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundJointaccountPageAuthModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._biz_scene = None
        self._channel = None
        self._identity = None
        self._identity_type = None
        self._invitee_id = None
        self._invitee_open_id = None
        self._open_id = None
        self._page = None
        self._product_code = None
        self._relation_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
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
    def invitee_id(self):
        return self._invitee_id

    @invitee_id.setter
    def invitee_id(self, value):
        self._invitee_id = value
    @property
    def invitee_open_id(self):
        return self._invitee_open_id

    @invitee_open_id.setter
    def invitee_open_id(self, value):
        self._invitee_open_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, value):
        self._relation_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        if self.invitee_id:
            if hasattr(self.invitee_id, 'to_alipay_dict'):
                params['invitee_id'] = self.invitee_id.to_alipay_dict()
            else:
                params['invitee_id'] = self.invitee_id
        if self.invitee_open_id:
            if hasattr(self.invitee_open_id, 'to_alipay_dict'):
                params['invitee_open_id'] = self.invitee_open_id.to_alipay_dict()
            else:
                params['invitee_open_id'] = self.invitee_open_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.relation_id:
            if hasattr(self.relation_id, 'to_alipay_dict'):
                params['relation_id'] = self.relation_id.to_alipay_dict()
            else:
                params['relation_id'] = self.relation_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundJointaccountPageAuthModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'invitee_id' in d:
            o.invitee_id = d['invitee_id']
        if 'invitee_open_id' in d:
            o.invitee_open_id = d['invitee_open_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page' in d:
            o.page = d['page']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'relation_id' in d:
            o.relation_id = d['relation_id']
        return o


