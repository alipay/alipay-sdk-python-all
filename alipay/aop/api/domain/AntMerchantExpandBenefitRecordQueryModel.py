#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandBenefitRecordQueryModel(object):

    def __init__(self):
        self._benefit_instance_id = None
        self._biz_ext = None
        self._out_user_id = None
        self._page_num = None
        self._page_size = None
        self._status = None
        self._user_id = None

    @property
    def benefit_instance_id(self):
        return self._benefit_instance_id

    @benefit_instance_id.setter
    def benefit_instance_id(self, value):
        self._benefit_instance_id = value
    @property
    def biz_ext(self):
        return self._biz_ext

    @biz_ext.setter
    def biz_ext(self, value):
        self._biz_ext = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_instance_id:
            if hasattr(self.benefit_instance_id, 'to_alipay_dict'):
                params['benefit_instance_id'] = self.benefit_instance_id.to_alipay_dict()
            else:
                params['benefit_instance_id'] = self.benefit_instance_id
        if self.biz_ext:
            if hasattr(self.biz_ext, 'to_alipay_dict'):
                params['biz_ext'] = self.biz_ext.to_alipay_dict()
            else:
                params['biz_ext'] = self.biz_ext
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AntMerchantExpandBenefitRecordQueryModel()
        if 'benefit_instance_id' in d:
            o.benefit_instance_id = d['benefit_instance_id']
        if 'biz_ext' in d:
            o.biz_ext = d['biz_ext']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


