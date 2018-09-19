#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingVoucherConfirmModel(object):

    def __init__(self):
        self._need_redirect = None
        self._out_biz_no = None
        self._redirect_uri = None
        self._template_id = None
        self._theme = None
        self._user_id = None

    @property
    def need_redirect(self):
        return self._need_redirect

    @need_redirect.setter
    def need_redirect(self, value):
        self._need_redirect = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def redirect_uri(self):
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, value):
        self._redirect_uri = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, value):
        self._theme = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_redirect:
            if hasattr(self.need_redirect, 'to_alipay_dict'):
                params['need_redirect'] = self.need_redirect.to_alipay_dict()
            else:
                params['need_redirect'] = self.need_redirect
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.redirect_uri:
            if hasattr(self.redirect_uri, 'to_alipay_dict'):
                params['redirect_uri'] = self.redirect_uri.to_alipay_dict()
            else:
                params['redirect_uri'] = self.redirect_uri
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.theme:
            if hasattr(self.theme, 'to_alipay_dict'):
                params['theme'] = self.theme.to_alipay_dict()
            else:
                params['theme'] = self.theme
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
        o = AlipayMarketingVoucherConfirmModel()
        if 'need_redirect' in d:
            o.need_redirect = d['need_redirect']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'redirect_uri' in d:
            o.redirect_uri = d['redirect_uri']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'theme' in d:
            o.theme = d['theme']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


