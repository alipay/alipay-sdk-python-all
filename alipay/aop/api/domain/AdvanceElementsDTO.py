#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdvanceElementsDTO(object):

    def __init__(self):
        self._advance_account_no = None
        self._advance_account_type = None
        self._advance_user_id = None
        self._auto_advance = None

    @property
    def advance_account_no(self):
        return self._advance_account_no

    @advance_account_no.setter
    def advance_account_no(self, value):
        self._advance_account_no = value
    @property
    def advance_account_type(self):
        return self._advance_account_type

    @advance_account_type.setter
    def advance_account_type(self, value):
        self._advance_account_type = value
    @property
    def advance_user_id(self):
        return self._advance_user_id

    @advance_user_id.setter
    def advance_user_id(self, value):
        self._advance_user_id = value
    @property
    def auto_advance(self):
        return self._auto_advance

    @auto_advance.setter
    def auto_advance(self, value):
        self._auto_advance = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_account_no:
            if hasattr(self.advance_account_no, 'to_alipay_dict'):
                params['advance_account_no'] = self.advance_account_no.to_alipay_dict()
            else:
                params['advance_account_no'] = self.advance_account_no
        if self.advance_account_type:
            if hasattr(self.advance_account_type, 'to_alipay_dict'):
                params['advance_account_type'] = self.advance_account_type.to_alipay_dict()
            else:
                params['advance_account_type'] = self.advance_account_type
        if self.advance_user_id:
            if hasattr(self.advance_user_id, 'to_alipay_dict'):
                params['advance_user_id'] = self.advance_user_id.to_alipay_dict()
            else:
                params['advance_user_id'] = self.advance_user_id
        if self.auto_advance:
            if hasattr(self.auto_advance, 'to_alipay_dict'):
                params['auto_advance'] = self.auto_advance.to_alipay_dict()
            else:
                params['auto_advance'] = self.auto_advance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdvanceElementsDTO()
        if 'advance_account_no' in d:
            o.advance_account_no = d['advance_account_no']
        if 'advance_account_type' in d:
            o.advance_account_type = d['advance_account_type']
        if 'advance_user_id' in d:
            o.advance_user_id = d['advance_user_id']
        if 'auto_advance' in d:
            o.auto_advance = d['auto_advance']
        return o


