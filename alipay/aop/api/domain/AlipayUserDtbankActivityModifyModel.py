#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankActivityModifyModel(object):

    def __init__(self):
        self._activity_id = None
        self._api_out_biz_no = None
        self._modify_type = None
        self._modify_value = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def api_out_biz_no(self):
        return self._api_out_biz_no

    @api_out_biz_no.setter
    def api_out_biz_no(self, value):
        self._api_out_biz_no = value
    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value
    @property
    def modify_value(self):
        return self._modify_value

    @modify_value.setter
    def modify_value(self, value):
        self._modify_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.api_out_biz_no:
            if hasattr(self.api_out_biz_no, 'to_alipay_dict'):
                params['api_out_biz_no'] = self.api_out_biz_no.to_alipay_dict()
            else:
                params['api_out_biz_no'] = self.api_out_biz_no
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
        if self.modify_value:
            if hasattr(self.modify_value, 'to_alipay_dict'):
                params['modify_value'] = self.modify_value.to_alipay_dict()
            else:
                params['modify_value'] = self.modify_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDtbankActivityModifyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'api_out_biz_no' in d:
            o.api_out_biz_no = d['api_out_biz_no']
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        if 'modify_value' in d:
            o.modify_value = d['modify_value']
        return o


