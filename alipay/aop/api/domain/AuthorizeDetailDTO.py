#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthorizeDetailDTO(object):

    def __init__(self):
        self._authorized_principal_id = None

    @property
    def authorized_principal_id(self):
        return self._authorized_principal_id

    @authorized_principal_id.setter
    def authorized_principal_id(self, value):
        self._authorized_principal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_principal_id:
            if hasattr(self.authorized_principal_id, 'to_alipay_dict'):
                params['authorized_principal_id'] = self.authorized_principal_id.to_alipay_dict()
            else:
                params['authorized_principal_id'] = self.authorized_principal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthorizeDetailDTO()
        if 'authorized_principal_id' in d:
            o.authorized_principal_id = d['authorized_principal_id']
        return o


