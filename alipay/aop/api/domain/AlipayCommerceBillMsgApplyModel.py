#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MsgParams import MsgParams


class AlipayCommerceBillMsgApplyModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._institution_id = None
        self._msg_params = None
        self._msg_type = None
        self._out_biz_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def msg_params(self):
        return self._msg_params

    @msg_params.setter
    def msg_params(self, value):
        if isinstance(value, MsgParams):
            self._msg_params = value
        else:
            self._msg_params = MsgParams.from_alipay_dict(value)
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.msg_params:
            if hasattr(self.msg_params, 'to_alipay_dict'):
                params['msg_params'] = self.msg_params.to_alipay_dict()
            else:
                params['msg_params'] = self.msg_params
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceBillMsgApplyModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'msg_params' in d:
            o.msg_params = d['msg_params']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


