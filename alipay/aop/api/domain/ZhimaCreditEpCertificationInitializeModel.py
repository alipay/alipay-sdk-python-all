#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCertificationInitializeModel(object):

    def __init__(self):
        self._alipay_account = None
        self._certify_category = None
        self._certify_return_url = None
        self._customize_content = None
        self._ep_cert_no = None
        self._ep_name = None
        self._open_id = None
        self._org_biz_no = None
        self._product_code = None
        self._user_cert_no = None
        self._user_id = None
        self._user_name = None
        self._user_type = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def certify_category(self):
        return self._certify_category

    @certify_category.setter
    def certify_category(self, value):
        self._certify_category = value
    @property
    def certify_return_url(self):
        return self._certify_return_url

    @certify_return_url.setter
    def certify_return_url(self, value):
        self._certify_return_url = value
    @property
    def customize_content(self):
        return self._customize_content

    @customize_content.setter
    def customize_content(self, value):
        self._customize_content = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_biz_no(self):
        return self._org_biz_no

    @org_biz_no.setter
    def org_biz_no(self, value):
        self._org_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.certify_category:
            if hasattr(self.certify_category, 'to_alipay_dict'):
                params['certify_category'] = self.certify_category.to_alipay_dict()
            else:
                params['certify_category'] = self.certify_category
        if self.certify_return_url:
            if hasattr(self.certify_return_url, 'to_alipay_dict'):
                params['certify_return_url'] = self.certify_return_url.to_alipay_dict()
            else:
                params['certify_return_url'] = self.certify_return_url
        if self.customize_content:
            if hasattr(self.customize_content, 'to_alipay_dict'):
                params['customize_content'] = self.customize_content.to_alipay_dict()
            else:
                params['customize_content'] = self.customize_content
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_biz_no:
            if hasattr(self.org_biz_no, 'to_alipay_dict'):
                params['org_biz_no'] = self.org_biz_no.to_alipay_dict()
            else:
                params['org_biz_no'] = self.org_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.user_cert_no:
            if hasattr(self.user_cert_no, 'to_alipay_dict'):
                params['user_cert_no'] = self.user_cert_no.to_alipay_dict()
            else:
                params['user_cert_no'] = self.user_cert_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCertificationInitializeModel()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'certify_category' in d:
            o.certify_category = d['certify_category']
        if 'certify_return_url' in d:
            o.certify_return_url = d['certify_return_url']
        if 'customize_content' in d:
            o.customize_content = d['customize_content']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_biz_no' in d:
            o.org_biz_no = d['org_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_cert_no' in d:
            o.user_cert_no = d['user_cert_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


