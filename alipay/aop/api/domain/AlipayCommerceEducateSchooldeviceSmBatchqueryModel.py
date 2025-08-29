#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSchooldeviceSmBatchqueryModel(object):

    def __init__(self):
        self._activity_code = None
        self._biz_code = None
        self._page_num = None
        self._page_size = None
        self._sm_cn_name = None
        self._sm_id = None
        self._status = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
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
    def sm_cn_name(self):
        return self._sm_cn_name

    @sm_cn_name.setter
    def sm_cn_name(self, value):
        self._sm_cn_name = value
    @property
    def sm_id(self):
        return self._sm_id

    @sm_id.setter
    def sm_id(self, value):
        self._sm_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
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
        if self.sm_cn_name:
            if hasattr(self.sm_cn_name, 'to_alipay_dict'):
                params['sm_cn_name'] = self.sm_cn_name.to_alipay_dict()
            else:
                params['sm_cn_name'] = self.sm_cn_name
        if self.sm_id:
            if hasattr(self.sm_id, 'to_alipay_dict'):
                params['sm_id'] = self.sm_id.to_alipay_dict()
            else:
                params['sm_id'] = self.sm_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSchooldeviceSmBatchqueryModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sm_cn_name' in d:
            o.sm_cn_name = d['sm_cn_name']
        if 'sm_id' in d:
            o.sm_id = d['sm_id']
        if 'status' in d:
            o.status = d['status']
        return o


