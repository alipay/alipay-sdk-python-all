#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorNamelistSyncModel(object):

    def __init__(self):
        self._biz_tid = None
        self._partner_block_id = None
        self._reason = None
        self._remark = None
        self._type = None
        self._type_sub_code = None
        self._user_block_id = None
        self._user_open_id = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def partner_block_id(self):
        return self._partner_block_id

    @partner_block_id.setter
    def partner_block_id(self, value):
        self._partner_block_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def type_sub_code(self):
        return self._type_sub_code

    @type_sub_code.setter
    def type_sub_code(self, value):
        self._type_sub_code = value
    @property
    def user_block_id(self):
        return self._user_block_id

    @user_block_id.setter
    def user_block_id(self, value):
        self._user_block_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.partner_block_id:
            if hasattr(self.partner_block_id, 'to_alipay_dict'):
                params['partner_block_id'] = self.partner_block_id.to_alipay_dict()
            else:
                params['partner_block_id'] = self.partner_block_id
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.type_sub_code:
            if hasattr(self.type_sub_code, 'to_alipay_dict'):
                params['type_sub_code'] = self.type_sub_code.to_alipay_dict()
            else:
                params['type_sub_code'] = self.type_sub_code
        if self.user_block_id:
            if hasattr(self.user_block_id, 'to_alipay_dict'):
                params['user_block_id'] = self.user_block_id.to_alipay_dict()
            else:
                params['user_block_id'] = self.user_block_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorNamelistSyncModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'partner_block_id' in d:
            o.partner_block_id = d['partner_block_id']
        if 'reason' in d:
            o.reason = d['reason']
        if 'remark' in d:
            o.remark = d['remark']
        if 'type' in d:
            o.type = d['type']
        if 'type_sub_code' in d:
            o.type_sub_code = d['type_sub_code']
        if 'user_block_id' in d:
            o.user_block_id = d['user_block_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        return o


