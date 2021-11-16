#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeZmgoAgreementSignModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._partner_id = None
        self._preorder_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeZmgoAgreementSignModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'preorder_no' in d:
            o.preorder_no = d['preorder_no']
        return o


