#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantZmgoCumulateQueryModel(object):

    def __init__(self):
        self._agreement_id = None
        self._need_detail = None
        self._page_no = None
        self._page_size = None
        self._provider_pid = None
        self._user_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def need_detail(self):
        return self._need_detail

    @need_detail.setter
    def need_detail(self, value):
        self._need_detail = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def provider_pid(self):
        return self._provider_pid

    @provider_pid.setter
    def provider_pid(self, value):
        self._provider_pid = value
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
        if self.need_detail:
            if hasattr(self.need_detail, 'to_alipay_dict'):
                params['need_detail'] = self.need_detail.to_alipay_dict()
            else:
                params['need_detail'] = self.need_detail
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.provider_pid:
            if hasattr(self.provider_pid, 'to_alipay_dict'):
                params['provider_pid'] = self.provider_pid.to_alipay_dict()
            else:
                params['provider_pid'] = self.provider_pid
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
        o = ZhimaMerchantZmgoCumulateQueryModel()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'need_detail' in d:
            o.need_detail = d['need_detail']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'provider_pid' in d:
            o.provider_pid = d['provider_pid']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


