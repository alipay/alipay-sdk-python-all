#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingUsercertificateBatchqueryModel(object):

    def __init__(self):
        self._certificate_code = None
        self._open_id = None
        self._page_num = None
        self._page_size = None
        self._user_certificate_code = None
        self._user_id = None

    @property
    def certificate_code(self):
        return self._certificate_code

    @certificate_code.setter
    def certificate_code(self, value):
        self._certificate_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def user_certificate_code(self):
        return self._user_certificate_code

    @user_certificate_code.setter
    def user_certificate_code(self, value):
        self._user_certificate_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_code:
            if hasattr(self.certificate_code, 'to_alipay_dict'):
                params['certificate_code'] = self.certificate_code.to_alipay_dict()
            else:
                params['certificate_code'] = self.certificate_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.user_certificate_code:
            if hasattr(self.user_certificate_code, 'to_alipay_dict'):
                params['user_certificate_code'] = self.user_certificate_code.to_alipay_dict()
            else:
                params['user_certificate_code'] = self.user_certificate_code
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
        o = AlipayEbppIndustryCareertrainingUsercertificateBatchqueryModel()
        if 'certificate_code' in d:
            o.certificate_code = d['certificate_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'user_certificate_code' in d:
            o.user_certificate_code = d['user_certificate_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


