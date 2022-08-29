#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperatorModifyVO import OperatorModifyVO


class AlipayOpenAuthOperatorInfoModifyModel(object):

    def __init__(self):
        self._modify_vo = None
        self._operator_id = None
        self._tenant_id = None

    @property
    def modify_vo(self):
        return self._modify_vo

    @modify_vo.setter
    def modify_vo(self, value):
        if isinstance(value, OperatorModifyVO):
            self._modify_vo = value
        else:
            self._modify_vo = OperatorModifyVO.from_alipay_dict(value)
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.modify_vo:
            if hasattr(self.modify_vo, 'to_alipay_dict'):
                params['modify_vo'] = self.modify_vo.to_alipay_dict()
            else:
                params['modify_vo'] = self.modify_vo
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthOperatorInfoModifyModel()
        if 'modify_vo' in d:
            o.modify_vo = d['modify_vo']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


