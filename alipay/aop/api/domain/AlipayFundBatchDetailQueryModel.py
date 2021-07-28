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
        self._out_batch_no = None
        self._out_biz_no = None
        self._page_num = None
        self._page_size = None
        self._payee_account = None
        self._product_code = None
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
    def out_batch_no(self):
        return self._out_batch_no

    @out_batch_no.setter
    def out_batch_no(self, value):
        self._out_batch_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
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
        if self.out_batch_no:
            if hasattr(self.out_batch_no, 'to_alipay_dict'):
                params['out_batch_no'] = self.out_batch_no.to_alipay_dict()
            else:
                params['out_batch_no'] = self.out_batch_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
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
        if 'out_batch_no' in d:
            o.out_batch_no = d['out_batch_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sign_principal' in d:
            o.sign_principal = d['sign_principal']
        return o


