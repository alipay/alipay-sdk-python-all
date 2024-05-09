#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceapiBizuserDeleteModel(object):

    def __init__(self):
        self._biz_user_id = None
        self._leave_type = None
        self._reason = None
        self._tnt_inst_id = None

    @property
    def biz_user_id(self):
        return self._biz_user_id

    @biz_user_id.setter
    def biz_user_id(self, value):
        self._biz_user_id = value
    @property
    def leave_type(self):
        return self._leave_type

    @leave_type.setter
    def leave_type(self, value):
        self._leave_type = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_user_id:
            if hasattr(self.biz_user_id, 'to_alipay_dict'):
                params['biz_user_id'] = self.biz_user_id.to_alipay_dict()
            else:
                params['biz_user_id'] = self.biz_user_id
        if self.leave_type:
            if hasattr(self.leave_type, 'to_alipay_dict'):
                params['leave_type'] = self.leave_type.to_alipay_dict()
            else:
                params['leave_type'] = self.leave_type
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceapiBizuserDeleteModel()
        if 'biz_user_id' in d:
            o.biz_user_id = d['biz_user_id']
        if 'leave_type' in d:
            o.leave_type = d['leave_type']
        if 'reason' in d:
            o.reason = d['reason']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


