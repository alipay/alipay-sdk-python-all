#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAlcagmprodAgreementQueryModel(object):

    def __init__(self):
        self._agreement_id = None
        self._open_id = None
        self._out_sign_no = None
        self._product_cd = None
        self._user_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_sign_no(self):
        return self._out_sign_no

    @out_sign_no.setter
    def out_sign_no(self, value):
        self._out_sign_no = value
    @property
    def product_cd(self):
        return self._product_cd

    @product_cd.setter
    def product_cd(self, value):
        self._product_cd = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_sign_no:
            if hasattr(self.out_sign_no, 'to_alipay_dict'):
                params['out_sign_no'] = self.out_sign_no.to_alipay_dict()
            else:
                params['out_sign_no'] = self.out_sign_no
        if self.product_cd:
            if hasattr(self.product_cd, 'to_alipay_dict'):
                params['product_cd'] = self.product_cd.to_alipay_dict()
            else:
                params['product_cd'] = self.product_cd
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAlcagmprodAgreementQueryModel()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_sign_no' in d:
            o.out_sign_no = d['out_sign_no']
        if 'product_cd' in d:
            o.product_cd = d['product_cd']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


