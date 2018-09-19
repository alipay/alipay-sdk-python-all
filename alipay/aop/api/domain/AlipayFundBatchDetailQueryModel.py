#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundBatchDetailQueryModel(object):

    def __init__(self):
        self._batch_no = None
        self._biz_code = None
        self._biz_scene = None
        self._detail_no = None
        self._detail_status = None
        self._page_num = None
        self._payee_account = None
        self._sign_principal = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def detail_no(self):
        return self._detail_no

    @detail_no.setter
    def detail_no(self, value):
        self._detail_no = value
    @property
    def detail_status(self):
        return self._detail_status

    @detail_status.setter
    def detail_status(self, value):
        self._detail_status = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def sign_principal(self):
        return self._sign_principal

    @sign_principal.setter
    def sign_principal(self, value):
        self._sign_principal = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.detail_no:
            if hasattr(self.detail_no, 'to_alipay_dict'):
                params['detail_no'] = self.detail_no.to_alipay_dict()
            else:
                params['detail_no'] = self.detail_no
        if self.detail_status:
            if hasattr(self.detail_status, 'to_alipay_dict'):
                params['detail_status'] = self.detail_status.to_alipay_dict()
            else:
                params['detail_status'] = self.detail_status
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.sign_principal:
            if hasattr(self.sign_principal, 'to_alipay_dict'):
                params['sign_principal'] = self.sign_principal.to_alipay_dict()
            else:
                params['sign_principal'] = self.sign_principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBatchDetailQueryModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'detail_no' in d:
            o.detail_no = d['detail_no']
        if 'detail_status' in d:
            o.detail_status = d['detail_status']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'sign_principal' in d:
            o.sign_principal = d['sign_principal']
        return o


